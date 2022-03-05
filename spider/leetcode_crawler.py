#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import json
import traceback
import html2text
import os
import requests
from requests_toolbelt import MultipartEncoder
import random, time
import re
import argparse, sys

DB_PATH = 'leetcode.sqlite3'


class LeetcodeCrawler():
    def __init__(self):
        self.session = requests.Session()
        self.csrftoken = ''
        self.is_login = False
        self.user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    # 获取到 token
    def get_csrftoken(self):
        url = 'https://leetcode-cn.com'
        cookies = self.session.get(url).cookies
        for cookie in cookies:
            if cookie.name == 'csrftoken':
                self.csrftoken = cookie.value

    # 登陆 leetcode 账号
    def login(self, username, password):
        url = "https://leetcode-cn.com/accounts/login"

        params_data = {
            'csrfmiddlewaretoken': self.csrftoken,
            'login': username,
            'password': password,
            'next': 'problems'
        }
        headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive',
                   'Referer': 'https://leetcode-cn.com/accounts/login/',
                   "origin": "https://leetcode-cn.com"}
        m = MultipartEncoder(params_data)

        headers['Content-Type'] = m.content_type
        result = self.session.post(url, headers=headers, data=m, timeout=10)
        # todo 由于会员题目需要LEETCODE_SESSION 需要手动更新，避免获取不到会员题目
        self.session.cookies.set('LEETCODE_SESSION',
                                 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDI3MDkyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGhlbnRpY2F0aW9uLmF1dGhfYmFja2VuZHMuUGhvbmVBdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGJmYzVhMmQ2NDJmYTZiN2FhNTI3MjAxOTJiM2EyODg1NjE4ZjdjYjZmZDY0MzRlN2MwMmQ1NTFjYWVjMGMzIiwiaWQiOjQyNzA5MjEsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJsdW1vbi1mIiwidXNlcl9zbHVnIjoibHVtb24tZiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLWNuLmNvbS9hbGl5dW4tbGMtdXBsb2FkL2RlZmF1bHRfYXZhdGFyLnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjQ2NDUxMzYzLjYwOTE1MTgsImV4cGlyZWRfdGltZV8iOjE2NDkwMTI0MDAsInZlcnNpb25fa2V5XyI6MX0.-iMtta465ZsUeMVcWrgZZH1wKUoc4XdIRBxIIF3_uVk')
        self.is_login = result.ok
        return self.is_login

    def get_problems(self, filters):
        url = "https://leetcode-cn.com/api/problems/all/"
        headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive'}
        resp = self.session.get(url, headers=headers, timeout=10)

        question_list = json.loads(resp.content.decode('utf-8'))
        question_update_list = []

        cursor = self.conn.cursor()
        for question in question_list['stat_status_pairs']:
            question_id = question['stat']['question_id']
            question_slug = question['stat']['question__title_slug']
            question_status = question['status']
            question_acs = question['stat']['total_acs']
            question_submits = question['stat']['total_submitted']

            # 用于题目去重
            cursor.execute('SELECT status FROM question WHERE id = ?', (question_id,))
            result = cursor.fetchone()
            print(question_id, question_status)
            if not result:
                IS_SUCCESS = False
                conn = sqlite3.connect(DB_PATH, timeout=10)
                while not IS_SUCCESS:
                    try:
                        # 休眠随机 1 - 2 秒，以免爬去频率过高被服务器禁掉
                        time.sleep(random.randint(1, 2))
                        cursor = conn.cursor()

                        headers = {'User-Agent': self.user_agent, 'Connection':
                            'keep-alive', 'Content-Type': 'application/json',
                                   'Referer': 'https://leetcode-cn.com/problems/' + question_slug}

                        url = "https://leetcode-cn.com/graphql"
                        params = {'operationName': "getQuestionDetail",
                                  'variables': {'titleSlug': question_slug},
                                  'query': '''query getQuestionDetail($titleSlug: String!) {
                                    question(titleSlug: $titleSlug) {
                                        questionId
                                        questionFrontendId
                                        questionTitle
                                        questionTitleSlug
                                        content
                                        translatedContent
                                        difficulty
                                        stats
                                        similarQuestions
                                        categoryTitle
                                        topicTags {
                                        name
                                        slug
                                    }
                                }
                            }'''
                                  }

                        json_data = json.dumps(params).encode('utf8')

                        resp = self.session.post(url, data=json_data, headers=headers, timeout=10)
                        content = resp.json()
                        questionId = content['data']['question']['questionId']
                        tags = []
                        for tag in content['data']['question']['topicTags']:
                            tags.append(tag['name'])

                        if content['data']['question']['content']:
                            if content['data']['question']['translatedContent']:
                                question_content = content['data']['question']['translatedContent']
                            else:
                                question_content = content['data']['question']['content']
                            question_detail = (questionId,
                                               content['data']['question']['questionFrontendId'],
                                               content['data']['question']['questionTitle'],
                                               content['data']['question']['questionTitleSlug'],
                                               content['data']['question']['difficulty'],
                                               question_content,
                                               question_acs,
                                               question_submits,
                                               question_status)
                            cursor.execute(
                                'INSERT INTO question (id, frontend_id, title, slug, difficulty, content, ac_num, submit_num, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                question_detail)
                            for tag in tags:
                                question_tag = (questionId, tag)
                                cursor.execute('INSERT INTO question_tag (question_id, tag) VALUES (?, ?)',
                                               question_tag)
                                print("insert question [%s] success" % (question_slug))
                            conn.commit()
                            IS_SUCCESS = True
                    # 若出现连接超时或连接错误则继续获取
                    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as error:
                        print('error====>>', str(error))

            elif self.is_login:
                if not question_status:
                    question_status = 'need_commit'
                question_update_list.append((question_status, question_id))

        cursor.executemany('UPDATE question SET status = ? WHERE id = ?', question_update_list)
        self.conn.commit()
        cursor.close()

    def connect_db(self, DB_PATH):
        self.conn = sqlite3.connect(DB_PATH, timeout=10)
        cursor = self.conn.cursor()

        query_table_exists = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name = 'question';"
        cursor.execute(query_table_exists)
        if cursor.fetchone()[0] == 0:
            cursor.execute('''CREATE TABLE question
                    (id      INT PRIMARY KEY       NOT NULL,
                    frontend_id         INT        NOT NULL,
                    title              CHAR(50)    NOT NULL,
                    slug               CHAR(50)    NOT NULL,
                    difficulty         CHAR(10)    NOT NULL,
                    content            TEXT        NOT NULL,
                    ac_num             INT         NOT NULL,
                    submit_num         INT         NOT NULL,
                    status             CHAR(10));''')

        query_table_exists = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name = 'last_ac_submission_record';"
        cursor.execute(query_table_exists)
        if cursor.fetchone()[0] == 0:
            cursor.execute('''CREATE TABLE last_ac_submission_record
                    (id      INT PRIMARY KEY       NOT NULL,
                    question_slug      CHAR(50)    NOT NULL,
                    timestamp          INT         NOT NULL,
                    language         CHAR(10)      NOT NULL,
                    code               TEXT,
                    runtime            CHAR(10));''')

        query_table_exists = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name = 'question_tag';"
        cursor.execute(query_table_exists)
        if cursor.fetchone()[0] == 0:
            cursor.execute('''CREATE TABLE question_tag
                    (question_id      INT       NOT NULL,
                      tag         CHAR(30)      NOT NULL);''')

        query_table_exists = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name = 'submission_record_log';"
        cursor.execute(query_table_exists)
        if cursor.fetchone()[0] == 0:
            cursor.execute('''CREATE TABLE submission_record_log
                    (id      INT PRIMARY KEY       NOT NULL,
                     question_id      INT       NOT NULL,
                     status_display         CHAR(20)      NOT NULL,
                     language         CHAR(10)      NOT NULL,
                     runtime            CHAR(10),
                     timestamp          INT         NOT NULL);''')

        cursor.close()

    def generate_questions_markdown(self, path, filters):
        if not os.path.isdir(path):
            os.mkdir(path)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM question")
        for row in cursor:
            question_detail = {
                'id': row[0],
                'frontedId': row[1],
                'title': row[2],
                'slug': row[3],
                'difficulty': row[4],
                'content': row[5],
                'status': row[6]
            }

            if not self.filter_question(question_detail, filters):
                continue

            tags = ''
            tag_cursor = self.conn.cursor()
            tag_cursor.execute('SELECT tag FROM question_tag WHERE question_id = ?', (row[0],))
            tag_list = tag_cursor.fetchall()

            for tag in tag_list:
                tags += tag[0] + ', '

            if len(tags) > 2:
                tags = tags[:-2]
            question_detail['tags'] = tags

            has_get_code = filters.__contains__('code')
            self.generate_question_markdown(question_detail, path, has_get_code)
        cursor.close()

    def filter_question(self, question_detail, filters):

        if filters.get('difficulty'):
            if filters['difficulty'] != question_detail['difficulty']:
                return False
        if filters.get('status'):
            if filters['status'] != question_detail['status']:
                return False

        tag_cursor = self.conn.cursor()
        tag_cursor.execute('SELECT tag FROM question_tag WHERE question_id = ?', (question_detail['id'],))
        tag_list = tag_cursor.fetchall()
        tag_cursor.close()
        if filters.get('tags'):
            tag_count = 0
            for tag in tag_list:
                if tag[0] in filters['tags']:
                    tag_count += 1
            if tag_count != len(filters['tags']):
                return False
        return True

    def save_ac_question_submission_log(self, question_id, submissions):
        cursor = self.conn.cursor()

        for submission in submissions:
            record_id = submission['id']
            status_display = submission['statusDisplay']
            language = submission['lang']
            runtime = submission['runtime']
            timestamp = submission['timestamp']
            submission_record = (record_id, question_id, status_display, language, runtime, timestamp)

            # 用于提交日志去重
            cursor.execute('SELECT timestamp FROM submission_record_log WHERE id = ?', (record_id,))
            result = cursor.fetchone()
            if not result:
                cursor.execute(
                    'INSERT INTO submission_record_log (id, question_id, status_display, language, runtime, timestamp) VALUES (?, ?, ?, ?, ?, ?)',
                    submission_record
                )
                print("insert submission_record_log[%s] success" % (record_id))
                self.conn.commit()


    def get_ac_question_submission(self, filters):
        if not self.is_login:
            return
        sql = "SELECT id,slug,difficulty,status FROM question WHERE status = 'ac' ;"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

        for row in results:
            question_detail = {
                'id': row[0],
                'slug': row[1],
                'difficulty': row[2],
                'status': row[3]
            }

            if not self.filter_question(question_detail, filters):
                continue

            question_id = question_detail['id']
            slug = question_detail['slug']
            cursor.execute('SELECT timestamp FROM last_ac_submission_record WHERE question_slug = ?', (slug,))
            result = cursor.fetchone()
            if result:
                print(result)
                continue

            IS_SUCCESS = False
            while not IS_SUCCESS:
                time.sleep(random.randint(2, 4))
                try:
                    url = "https://leetcode-cn.com/graphql"
                    params = {'operationName': "Submissions",
                              'variables': {"offset": 0, "limit": 20, "lastKey": '', "questionSlug": slug},
                              'query': '''query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {
                                submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
                                lastKey
                                hasNext
                                submissions {
                                    id
                                    statusDisplay
                                    lang
                                    runtime
                                    timestamp
                                    url
                                    isPending
                                    __typename
                                }
                                __typename
                            }
                        }'''
                              }

                    json_data = json.dumps(params).encode('utf-8')
                    headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive',
                               'Referer': 'https://leetcode-cn.com/accounts/login/',
                               "Content-Type": "application/json", 'x-csrftoken': self.csrftoken}
                    resp = self.session.post(url, data=json_data, headers=headers, timeout=10)
                    content = resp.json()
                    print(content)
                    submissions = content['data']['submissionList']['submissions']
                    # 保存每题提交的日志记录
                    self.save_ac_question_submission_log(question_id,submissions)

                    for submission in submissions:
                        if submission['statusDisplay'] == "Accepted":
                            cursor.execute(
                                "SELECT COUNT(*) FROM last_ac_submission_record WHERE id =" + str(submission['id']))
                            if cursor.fetchone()[0] == 0:
                                IS_GET_SUBMISSION_SUCCESS = False
                                code = ''
                                while not IS_GET_SUBMISSION_SUCCESS:
                                    url = "https://leetcode-cn.com/graphql"
                                    params = {"operationName": "mySubmissionDetail",
                                              'variables': {"id": submission['id']},
                                              'query': '''query mySubmissionDetail($id: ID!) {
                                              submissionDetail(submissionId: $id) {
                                                id
                                                code
                                                runtime
                                                memory
                                                rawMemory
                                                statusDisplay
                                                timestamp
                                                lang
                                                passedTestCaseCnt
                                                totalTestCaseCnt
                                                sourceUrl
                                                question {
                                                  titleSlug
                                                  title
                                                  translatedTitle
                                                  questionId
                                                  __typename
                                                }
                                                ... on GeneralSubmissionNode {
                                                  outputDetail {
                                                    codeOutput
                                                    expectedOutput
                                                    input
                                                    compileError
                                                    runtimeError
                                                    lastTestcase
                                                    __typename
                                                  }
                                                  __typename
                                                }
                                                submissionComment {
                                                  comment
                                                  flagType
                                                  __typename
                                                }
                                                __typename
                                              }
                                            }'''}

                                    json_data = json.dumps(params).encode('utf-8')
                                    headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive',
                                               'Referer': 'https://leetcode-cn.com/accounts/login/',
                                               "Content-Type": "application/json", 'x-csrftoken': self.csrftoken}
                                    time.sleep(random.randint(3, 4))
                                    resp = self.session.post(url, data=json_data, headers=headers, timeout=10)
                                    content = resp.json()
                                    print(content)
                                    code = content['data']['submissionDetail']['code']

                                    if not code:
                                        print('WARN: Can not get [{}] solution code'.format(slug))
                                        time.sleep(random.randint(2, 4))
                                        continue
                                    IS_GET_SUBMISSION_SUCCESS = True

                                # 用于提交通过记录去重
                                cursor.execute('SELECT timestamp FROM last_ac_submission_record WHERE id = ?', (submission['id'],))
                                result = cursor.fetchone()
                                if not result:
                                    submission_detail = (
                                        submission['id'], slug, submission['timestamp'], submission['lang'],
                                        submission['runtime'], code)
                                    cursor.execute(
                                        "INSERT INTO last_ac_submission_record (id, question_slug, timestamp, language, runtime, code) VALUES(?, ?, ?, ?, ?, ?)",
                                        submission_detail)
                                    print("insert submission[%s] success" % (submission['id']))
                                    self.conn.commit()
                            IS_SUCCESS = True
                            break
                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as error:
                    print(str(error))
        cursor.close()

    def generate_question_markdown(self, question, path, has_get_code):
        title = question['title'].strip().replace(' ','-').replace('\'','').replace('?','').replace('/','-').replace(':','-')
        text_path = os.path.join(path, "{}-{}".format(question['frontedId'], title))
        if not os.path.isdir(text_path):
            os.mkdir(text_path)
        with open(os.path.join(text_path, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# [{}][title]\n".format(question['title']))
            f.write("\n## Description\n\n")
            text = question['content']

            content = html2text.html2text(text).replace("**Input:**", "Input:").replace("**Output:**",
                                                                                        "Output:").replace(
                '**Explanation:**', 'Explanation:').replace('\n    ', '    ')
            f.write(content)

            f.write("\n**Tags:** {}\n".format(question['tags']))
            f.write("\n**Difficulty:** {}\n".format(question['difficulty']))
            f.write("\n## 思路\n")

            if self.is_login and has_get_code:
                sql = "SELECT code, language FROM last_ac_submission_record WHERE question_slug = ? ORDER BY timestamp"
                cursor = self.conn.cursor()
                cursor.execute(sql, (question['slug'],))
                submission = cursor.fetchone()
                cursor.close()

                if submission != None:
                    f.write("\n``` %s\n" % (submission[1]))
                    f.write(submission[0].encode('utf-8').decode('unicode_escape'))

                    f.write("\n```\n")

            f.write("\n[title]: https://leetcode-cn.com/problems/{}\n".format(question['slug']))

    def generate_questions_submission(self, path, filters):
        if not self.is_login:
            return

        sql = """
            SELECT q.title, l.code,l.language, q.frontend_id, l.question_slug,max(l.timestamp) FROM last_ac_submission_record as l,question as q
            WHERE l.question_slug == q.slug and q.status = 'ac' GROUP BY l.question_slug
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)

        filter_cursor = self.conn.cursor()
        for submission in cursor:
            filter_cursor.execute("SELECT id,slug,difficulty,status FROM question WHERE slug = ?", (submission[4],))
            result = filter_cursor.fetchone()
            question_detail = {
                'id': result[0],
                'slug': result[1],
                'difficulty': result[2],
                'status': result[3]
            }
            if not self.filter_question(question_detail, filters):
                continue
            self.generate_question_submission(path, submission)

        cursor.close()
        filter_cursor.close()

    def generate_question_submission(self, path, submission):
        if not os.path.isdir(path):
            os.mkdir(path)
        title = submission[0].strip().replace(' ','-').replace('\'','').replace('?','').replace('/','-').replace(':','-')
        text_path = os.path.join(path, "{}-{}".format(submission[3], title))

        if not os.path.isdir(text_path):
            os.mkdir(text_path)
        with open(os.path.join(text_path, "solution.py"), 'w', encoding='utf-8') as f:
            f.write(submission[1].encode('utf-8').decode('unicode_escape'))

    def close_db(self):
        self.conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("problems", nargs='?', default="note")
    parser.add_argument('-d', '--difficulty',
                        nargs='+',
                        choices=['Easy', 'Medium', 'Hard'],
                        help="Specify the difficulty.\n"
                             "If not specified, all problems will be grasped.")

    parser.add_argument('-t', '--tags',
                        nargs='+',
                        help="Specify the tag")

    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        default=False,
                        help="Verbose output")

    parser.add_argument('-s', '--status',
                        nargs='+',
                        choices=['ac', 'notac', 'none'],
                        help="Specify the probelms statu.\n"
                             "If not specified, all problems will be grasped.")
    parser.add_argument('-c', '--code',
                        nargs='+',
                        help="Code solution output path.")
    parser.add_argument('-u', '--username',
                        nargs='+',
                        help="username")
    parser.add_argument('-p', '--password',
                        nargs='+',
                        help="password")

    if len(sys.argv) > 1:
        args = parser.parse_args()
    else:
        parser.print_help()
        sys.exit(1)

    print("start leetcode spider...")
    args_dict = vars(args)
    filters = {}

    test = LeetcodeCrawler()
    test.get_csrftoken()

    if args_dict.get('code') or args_dict.get('status'):
        if not (args_dict.get('username') and args_dict.get('password')):
            print("ERROR: choice problem by statu or generate submission code must set username and password!")
            sys.exit()
        else:
            is_login = test.login(args.username[0], args.password[0])
            print("INFO: login account success!")
            if not is_login:
                print("ERROR: login account fail!")
                sys.exit()
        if args_dict.get('code'):
            filters['code'] = args.code
            if args.verbose:
                print('Specified code path is: {}'.format(args.code))
        if args_dict.get('status'):
            filters['status'] = args.status[0]
            if args.verbose:
                print('Specified status is: {}'.format(args.status))

    if args_dict.get('difficulty') or args_dict.get('tags'):
        if args_dict.get('difficulty'):
            filters["difficulty"] = args.difficulty[0]
            if args.verbose:
                print('Specified difficulty is: {}'.format(args.difficulty))
        if args_dict.get('tags'):
            filters['tags'] = args.tags
            if args.verbose:
                print('Specified tag is: {}'.format(args.tags))

    test.connect_db(DB_PATH)
    test.get_problems(filters)
    test.generate_questions_markdown(args.problems, filters)
    if args_dict.get('code'):
        test.get_ac_question_submission(filters)
        test.generate_questions_submission(args.problems, filters)

    test.close_db()
