# -*- coding: utf-8 -*-
import shutil
import sqlite3
import pymysql
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

hql_params = {"operationName": "mySubmissionDetail",
              'variables': {"id": 0},
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

class LeetcodeCrawler():
    def __init__(self,leetcname='.'):
        self.session = requests.Session()
        self.csrftoken = ''
        self.is_login = False
        self.lcusr=leetcname
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
        print(username,password)
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
        login_result = self.session.post(url, headers=headers, data=m, timeout=10)
        # todo 由于会员题目需要LEETCODE_SESSION 需要手动更新，避免获取不到会员题目
        self.session.cookies.set('LEETCODE_SESSION',
                                 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDI3MDkyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGhlbnRpY2F0aW9uLmF1dGhfYmFja2VuZHMuUGhvbmVBdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGJmYzVhMmQ2NDJmYTZiN2FhNTI3MjAxOTJiM2EyODg1NjE4ZjdjYjZmZDY0MzRlN2MwMmQ1NTFjYWVjMGMzIiwiaWQiOjQyNzA5MjEsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJsdW1vbi1mIiwidXNlcl9zbHVnIjoibHVtb24tZiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLWNuLmNvbS9hbGl5dW4tbGMtdXBsb2FkL2RlZmF1bHRfYXZhdGFyLnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjUxMDQ3NDEyLjM0NDQxNTQsImV4cGlyZWRfdGltZV8iOjE2NTM1OTE2MDAsInZlcnNpb25fa2V5XyI6MSwibGF0ZXN0X3RpbWVzdGFtcF8iOjE2NTEwNDc1Mzd9.J84BderPqWSv3Q92nZeN9JE5rBR64yUN-H4CP7CsWH8') # Luken
                                # 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTE3NTgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYXV0aGVudGljYXRpb24uYXV0aF9iYWNrZW5kcy5QaG9uZUF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjM4ZjMyZDcwOWFmNzM3Mjg3MjBlMWM1NzFjZTYxMGUxNDRlYWJkM2EwOTg1MzM1YjQwMGNmMWFlYWNmMzZmNzEiLCJpZCI6NTE3NTgyLCJlbWFpbCI6InpoYW5neXV4aW45N0BidWFhLmVkdS5jbiIsInVzZXJuYW1lIjoid2J5LTciLCJ1c2VyX3NsdWciOiJ3YnktNyIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLWNuLmNvbS9hbGl5dW4tbGMtdXBsb2FkL3VzZXJzL3dieS03L2F2YXRhcl8xNTU3MDA4NjI4LnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjUxMTA5NTU2LjI2OTYyNjYsImV4cGlyZWRfdGltZV8iOjE2NTM2NzgwMDB9.S3XTrM8PXMNfXA99Jb2z6OMu3hwUMbfyzjHTPBbRa8Y') # bowen 6.51


        print(login_result.text)
        self.is_login = login_result.ok
        return self.is_login

    def get_problems_describe(self, filters=None):
        url = "https://leetcode-cn.com/api/problems/all/"
        headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive'}
        resp = self.session.get(url, headers=headers, timeout=10)

        question_list = json.loads(resp.content.decode('utf-8'))
        question_statnum_list,q_acstat_updatelist = [],[]

        cursor = self.conn.cursor()
        cursor.execute('SELECT question_id,ac_status FROM question_acstat WHERE user = %s', ( self.lcusr))
        all_ques=cursor.fetchall()
        print(all_ques[:10])
        dic_q={r[0]:r[1] for r in all_ques}
        print('self.is_login=%s question_nums %s' %( self.is_login,len(question_list['stat_status_pairs'])))
        for question in question_list['stat_status_pairs']:
            if question['status']:
                if len(question_statnum_list)%100==0:
                    print(question['stat']['question__title_slug'],question['status'],'qnum',len(question_statnum_list), 'ac_changed',len(q_acstat_updatelist))
            #else:
            #    print(question)
            question_id = question['stat']['question_id']
            question_slug = question['stat']['question__title_slug']
            question_status = 'need_commit' if question['status'] is None else question['status']
            question_acs = question['stat']['total_acs']
            question_submits = question['stat']['total_submitted']
            question_articles = question['stat']['total_column_articles']
            question_progress = question['progress']
            question_frequency = question['frequency']

            # 用于题目去重
            # cursor.execute('SELECT ac_status FROM question_acstat WHERE question_id = %s AND user = %s', (question_id,self.lcusr))
            # result = cursor.fetchone()
            qid_ac=dic_q.get(question_id,None)

            if qid_ac is None:
                #print('new_question_httpfetch', question_id, question_slug, question_status)
                continue
                IS_SUCCESS,req_retry = False,0
                # conn = sqlite3.connect(DB_PATH, timeout=10)
                print('sqlite ',IS_SUCCESS)
                while not IS_SUCCESS and req_retry<3:
                    # try:
                        # 爬虫休眠随机 1 - 2 秒，爬取频率过高会被服务器检测到访问频率过快而禁掉ip的问题
                        time.sleep(random.randint(1, 5))
                        req_retry+=1
                        cursor = conn.cursor()

                        headers = {'User-Agent': self.user_agent, 'Connection':
                            'keep-alive', 'Content-Type': 'application/json','Referer': 'https://leetcode-cn.com/problems/' + question_slug}


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
                        print(content['data']['question']['questionTitleSlug'],content['data']['question']['content'],req_retry)
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
                                'INSERT INTO question (id, frontend_id, title, slug, difficulty, content, ac_num, submit_num, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                question_detail)
                            for tag in tags:
                                question_tag = (questionId, tag)
                                cursor.execute('INSERT INTO question_tag (question_id, tag) VALUES (%s,%s)',question_tag)
                                print("insert question [%s] success" % (question_slug))
                            conn.commit()
                            IS_SUCCESS = True
                    # 若出现连接超时或连接错误则继续获取
                    # except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as error:
                    # except Exception as error:
                    #     print('error====>>', str(error))
                        print('httpfetch okay')
            if self.is_login:
                #print('slug %s question_status %s'%(question_slug,question_status))
                if question_status !=dic_q.get(question_id,'need_commit'): q_acstat_updatelist.append((question_status,question_id,self.lcusr))
                question_statnum_list.append((question_frequency,question_progress,question_articles, question_id))

        #cursor.executemany("UPDATE question SET frequency = ?, progress= ?, articles =? , updatets=strftime('%Y-%m-%d %H:%M:%fZ', 'now') WHERE id = ?", question_statnum_list)
        if q_acstat_updatelist: cursor.executemany("UPDATE question_acstat SET ac_status = %s WHERE question_id = %s and user = %s", q_acstat_updatelist)


        self.conn.commit()
        cursor.close()
        print('question_status finished')

    def connect_mysql(self):
        self.conn = pymysql.connect(host='192.168.6.99',user='admin',password='Admin1234!',database='capcode')
        #cursor = self.conn.cursor()


    def generate_questions_markdown(self, path, filters):
        if not os.path.isdir(path):
            os.mkdir(path)
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id,q.frontend_id,q.title,q.slug,q.difficulty,q.content,a.ac_status FROM question q join question_acstat a on q.id=a.question_id")
        for row in cursor:
            question_detail = {
                'id': row[0],
                'frontedId': row[1],
                'title': row[2],
                'slug': row[3],
                'difficulty': row[4],
                'content': row[5],
                'acstatus': row[6]
            }

            if not self.filter_question(question_detail, filters): continue

            print('new_question_README',question_detail)

            tags = ''
            tag_cursor = self.conn.cursor()
            tag_cursor.execute('SELECT tag FROM question_tag WHERE question_id = %s', (row[0],))
            tag_list = tag_cursor.fetchall()

            for tag in tag_list: tags += tag[0] + ', '

            if len(tags) > 2: tags = tags[:-2]

            question_detail['tags'] = tags

            has_get_code = filters.__contains__('code')
            question=question_detail
            # self.generate_question_markdown(question_detail, path, has_get_code)
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
                    sql = "SELECT code, language FROM lastac_submission_record WHERE question_slug = %s ORDER BY timestamp"
                    cursor = self.conn.cursor()
                    cursor.execute(sql, (question['slug'],))
                    submission = cursor.fetchone()
                    cursor.close()

                    if submission != None:
                        f.write("\n``` %s\n" % (submission[1]))
                        f.write(submission[0].encode('utf-8').decode('unicode_escape'))

                        f.write("\n```\n")

                f.write("\n[title]: https://leetcode-cn.com/problems/{}\n".format(question['slug']))
        cursor.close()

    def filter_question(self, question_detail, filters):
        if filters.get('difficulty'):
            if filters['difficulty'] != question_detail['difficulty']:
                return False
        if filters.get('acstatus'):
            if filters['acstatus'] != question_detail['acstatus']:
                return False
        if filters.get('slug'):
            if filters['slug'] != question_detail['slug']:
                return False

        tag_cursor = self.conn.cursor()
        tag_cursor.execute('SELECT tag FROM question_tag WHERE question_id = (%s)', (question_detail['id'],))
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
            submission_record = (record_id, question_id, status_display, language, runtime, timestamp,self.lcusr)

            # 用于提交日志去重
            cursor.execute('SELECT timestamp FROM submission_record_log WHERE id = (%s)', (record_id,))
            result = cursor.fetchone()
            if not result:
                cursor.execute(
                    'INSERT INTO submission_record_log (id, question_id, status_display, language, runtime, timestamp,user) VALUES (%s, %s, %s, %s, %s, %s,%s)',
                    submission_record
                )
                print("insert submission_record_log[%s] success" % (record_id))
                self.conn.commit()


    def get_ac_questions_submission_json(self, filters,skipsubm=True):
        print('...get_ac_questions_submission_json')
        if not self.is_login:
            print('not login')
            return
        sql = "SELECT q.id,q.slug,q.difficulty,s.ac_status,q.frontend_id FROM question q join question_acstat s on q.id =s.question_id and s.user='%s' WHERE ac_status = 'ac' ;"%self.lcusr
        print(sql)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(results)

        for row in results:
            question_detail = {
                'id': row[0],
                'slug': row[1],
                'difficulty': row[2],
                'acstatus': row[3],
                'frontend_id':row[4],
            }

            if not self.filter_question(question_detail, filters):
                continue

            question_id = question_detail['id']
            slug = question_detail['slug']
            # if question_id<3000:
            #     subdir='%s-%s'%(question_detail['frontend_id'],slug)
            #     if os.path.exists('raw/%s'%subdir) and not os.path.exists('luken/tree/%s'%subdir):
            #         shutil.copytree('raw/%s'%subdir,'luken/tree/%s'%subdir)
            # continue
            cursor.execute("SELECT timestamp FROM lastac_submission_record WHERE question_slug = %s and user = %s", (slug,self.lcusr))
            result = cursor.fetchone()
            if result:
                print('%s lastac_submission_record ts=%s'%(slug,result))
                continue

            IS_SUCCESS,req_retry = False,0
            while not IS_SUCCESS and req_retry<3:
                req_retry+=1
                time.sleep(random.randint(2, 4))
                try:
                    url = "https://leetcode-cn.com/graphql"
                    params = {'operationName': "Submissions",
                              'variables': {"offset": 0, "limit": 100, "lastKey": '', "questionSlug": slug},
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
                    submissions = content['data']['submissionList']['submissions']
                    print('%s req_retry %s submit_num %s'%( slug,req_retry,len(submissions)))

                    # 保存每题提交的日志记录
                    # self.save_ac_question_submission_log(question_id,submissions)
                    # if skipsubm:
                    #     IS_SUCCESS = True
                    #     continue
                    for submission in submissions:
                        if submission['statusDisplay'] == "Accepted":
                            cursor.execute("SELECT COUNT(*) FROM lastac_submission_record WHERE id =" + str(submission['id']))
                            if cursor.fetchone()[0] == 0:
                                IS_GET_SUBMISSION_SUCCESS = False
                                code = ''
                                while not IS_GET_SUBMISSION_SUCCESS:
                                    url = "https://leetcode-cn.com/graphql"
                                    hql_params['variables']['id']=submission['id']

                                    json_data = json.dumps(dict(hql_params)).encode('utf-8')
                                    headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive', 'Referer': 'https://leetcode-cn.com/accounts/login/',
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
                                cursor.execute('SELECT timestamp FROM lastac_submission_record WHERE id = %s', (submission['id'],))
                                result = cursor.fetchone()
                                if not result:
                                    submission_detail = (submission['id'], slug, submission['timestamp'], submission['lang'],submission['runtime'], code,self.lcusr)

                                    cursor.execute(
                                        "INSERT INTO lastac_submission_record (id, question_slug, timestamp, language, runtime, code,user) VALUES(%s,%s,%s,%s,%s,%s,%s)",submission_detail)
                                    print("insert submission[%s] success" % (submission['id']))
                                    self.conn.commit()
                                IS_SUCCESS = True
                                break
                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as error:
                    print(str(error))
        cursor.close()


    def generate_questions_submission(self, path, filters):
        sql = """
            SELECT q.title, l.code,l.language, q.frontend_id, l.question_slug,max(l.timestamp) mxts,q.id,q.slug,q.difficulty,ac.ac_status 
            FROM lastac_submission_record as l,question q,question_acstat as ac
            WHERE l.question_slug = q.slug and q.id=ac.question_id and ac.ac_status = 'ac' and l.user= '%s' and ac.user= '%s' GROUP BY l.question_slug
        """%(self.lcusr,self.lcusr)

        cursor = self.conn.cursor()
        cursor.execute(sql)
        submissions= cursor.fetchall()
        for submission in submissions:
            #print(submission)
            question_detail = {'id': submission[6], 'slug': submission[7], 'difficulty': submission[8], 'acstatus': submission[9]  }
            if not self.filter_question(question_detail, filters): continue

            if not os.path.isdir(path): os.mkdir(path)

            title = submission[0].strip().replace(' ','-').replace('\'','').replace('?','').replace('/','-').replace(':','-')
            text_path = os.path.join(path, "{}-{}".format(submission[3], title))

            if not os.path.isdir(text_path): os.mkdir(text_path)
            print(text_path)

            with open(os.path.join(text_path, "solution.py"), 'w', encoding='utf-8') as f:
                f.write(submission[1].encode('utf-8').decode('unicode_escape'))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("problems", nargs='?', default="note")
    parser.add_argument('-d', '--difficulty',
                        nargs='+',
                        choices=['Easy', 'Medium', 'Hard'],
                        help="Specify the difficulty.\n"
                             "If not specified, all problems will be grasped.")
    parser.add_argument('-s', '--slug',
                        nargs='+',
                        help="Specify slug")

    parser.add_argument('-t', '--tags',
                        nargs='+',
                        help="Specify the tag")

    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        default=False,
                        help="Verbose output")

    parser.add_argument('-a', '--acstatus',
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

    leetcname = {'18201031103': 'luken','18906191216':'bowen','18901944496':'pedro'}[args.username[0]]
    leetcr = LeetcodeCrawler(leetcname)
    leetcr.get_csrftoken()

    if args_dict.get('code') or args_dict.get('acstatus'):
        if not (args_dict.get('username') and args_dict.get('password')):
            print("ERROR: choice problem by statu or generate submission code must set username and password!")
            sys.exit()
        else:

            is_login = leetcr.login(args.username[0], args.password[0])
            print("INFO: login account success!")
            if not is_login:
                print("ERROR: login account fail!")
                sys.exit()
        if args_dict.get('code'):
            filters['code'] = args.code
            if args.verbose:
                print('Specified code path is: {}'.format(args.code))
        if args_dict.get('acstatus'):
            filters['acstatus'] = args.acstatus[0]
            if args.verbose:
                print('Specified status is: {}'.format(args.status))
        if args_dict.get('slug'):
            filters['slug'] = args.slug[0]
            if args.verbose:
                print('Specified slug is: {}'.format(args.slug))

    if args_dict.get('difficulty') or args_dict.get('tags'):
        if args_dict.get('difficulty'):
            filters["difficulty"] = args.difficulty[0]
            if args.verbose:
                print('Specified difficulty is: {}'.format(args.difficulty))
        if args_dict.get('tags'):
            filters['tags'] = args.tags
            if args.verbose:
                print('Specified tag is: {}'.format(args.tags))

    leetcr.connect_mysql()
    # leetcr.get_problems_describe()
    # leetcr.get_ac_questions_submission_json(filters,skipsubm=True)
    if args_dict.get('code'):
        leetcr.get_ac_questions_submission_json(filters,skipsubm=False)
        leetcr.generate_questions_markdown(args.code[0], filters)
        # leetcr.generate_questions_submission(args.code[0], filters)

