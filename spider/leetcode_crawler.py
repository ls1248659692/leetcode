#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import json
import traceback
import html2text
import os
import requests
from requests_toolbelt import MultipartEncoder
import random,time
import re
import argparse,sys
import threading

db_path = 'leetcode.db'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

def initLock(l):
	global lock
	lock = l


threadLock = threading.Lock()

class insetQuestionThread(threading.Thread):
    def __init__(self, title_slug, *args):
        threading.Thread.__init__(self)
        self.title_slug = title_slug
        self.status = None
        if len(args) == 1:
            self.status = args[0]
    def run(self):
        IS_SUCCESS = False
        conn = sqlite3.connect(db_path, timeout=10)
        while not IS_SUCCESS:
            try:
                # 休眠随机 1-3 秒，以免爬去频率过高被服务器禁掉
                time.sleep(random.randint(1, 3))        
                cursor = conn.cursor()

                session = requests.Session()
                headers = {'User-Agent': user_agent, 'Connection': 
                    'keep-alive', 'Content-Type': 'application/json',
                    'Referer': 'https://leetcode-cn.com/problems/' + self.title_slug}

                url = "https://leetcode-cn.com/graphql"
                params = {'operationName': "getQuestionDetail",
                    'variables': {'titleSlug': self.title_slug},
                    'query': '''query getQuestionDetail($titleSlug: String!) {
                        question(titleSlug: $titleSlug) {
                            questionId
                            questionFrontendId
                            questionTitle
                            questionTitleSlug
                            content
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
                    
                question_detail = ()
                resp = session.post(url, data = json_data, headers = headers, timeout = 10)
                content = resp.json()
                questionId = content['data']['question']['questionId']
                tags = []
                for tag in content['data']['question']['topicTags']:
                    tags.append(tag['name'])

                if content['data']['question']['content'] != None:
                    question_detail = (questionId, 
                                content['data']['question']['questionFrontendId'], 
                                content['data']['question']['questionTitle'],
                                content['data']['question']['questionTitleSlug'],
                                content['data']['question']['difficulty'],
                                content['data']['question']['content'],
                                self.status)
                    threadLock.acquire()
                    cursor.execute('INSERT INTO question (id, frontend_id, title, slug, difficulty, content, status) VALUES (?, ?, ?, ?, ?, ?, ?)', question_detail)
                    for tag in tags:
                        question_tag = (questionId, tag)
                        cursor.execute('INSERT INTO question_tag (question_id, tag) VALUES (?, ?)', question_tag)
                    conn.commit()
                    print("insert question [%s] success" %(self.title_slug))
                    threadLock.release()
                    IS_SUCCESS = True
            # 若出现连接超时或连接错误则继续获取
            except (requests.exceptions.Timeout,requests.exceptions.ConnectionError) as error:
                print(str(error))
        cursor.close()
        conn.close()
    
class LeetcodeCrawler():
    def __init__(self):
        self.session = requests.Session()      
        self.csrftoken = ''
        self.is_login = False
    
    # 获取到 token
    def get_csrftoken(self):
        url = 'https://leetcode-cn.com'
        cookies = self.session.get(url).cookies
        for cookie in cookies:
            if cookie.name == 'csrftoken':
                self.csrftoken = cookie.value
                break

    # 登陆 leetcode 账号
    def login(self, username, password):
        url = "https://leetcode-cn.com/accounts/login"
        
        params_data = {
            'csrfmiddlewaretoken': self.csrftoken,
            'login': username,
            'password':password,
            'next': 'problems'
        }
        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive', 'Referer': 'https://leetcode-cn.com/accounts/login/',
        "origin": "https://leetcode-cn.com"}
        m = MultipartEncoder(params_data)   

        headers['Content-Type'] = m.content_type
        self.session.post(url, headers = headers, data = m, timeout = 10, allow_redirects = False)
        self.is_login = self.session.cookies.get('LEETCODE_SESSION') != None
        return self.is_login

    def get_problems(self, filters):
    
        url = "https://leetcode-cn.com/api/problems/all/"

        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
        resp = self.session.get(url, headers = headers, timeout = 10)
       
        question_list = json.loads(resp.content.decode('utf-8'))

        question_update_list = []
        threads = []

        cursor = self.conn.cursor()

        for question in question_list['stat_status_pairs']:
            question_id = question['stat']['question_id']
            question_slug = question['stat']['question__title_slug']
            question_status = question['status']

            question_difficulty  = "None"
            level = question['difficulty']['level']
            
            if level == 1:
                question_difficulty = "Easy"
            elif level == 2:
                question_difficulty = "Medium"
            elif level == 3:
                question_difficulty = "Hard"


            if filters.get('difficulty'):
                if filters['difficulty'] != question_difficulty:
                    continue

            if filters.get('status'):
                if filters['status'] != question_status:
                     continue

            if question['paid_only']:
                continue
            
            cursor.execute('SELECT status FROM question WHERE id = ?', (question_id,))
            result = cursor.fetchone()
            if not result:
                thread = insetQuestionThread(question_slug, question_status)
                thread.start()
                while True:  
                    #判断正在运行的线程数量,如果小于5则退出while循环,  
                    #进入for循环启动新的进程.否则就一直在while循环进入死循环  
                    if(len(threading.enumerate()) < 60):  
                        break  
            
                # 添加线程到线程列表
                threads.append(thread)  
            elif self.is_login and question_status != result[0]:
                question_update_list.append((question_status, question_id))
        for t in threads:
            t.join()
        
        cursor.executemany('UPDATE question SET status = ? WHERE id = ?', question_update_list)
        self.conn.commit()
        cursor.close()
        

    def connect_db(self, db_path):
        self.conn = sqlite3.connect(db_path, timeout = 10)
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
                    tag      CHAR(30)    NOT NULL);''')

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
                

    def get_ac_question_submission(self, filters):
        if not self.is_login:
            return 
        sql = "SELECT id,slug,difficulty,status FROM question WHERE status = 'ac';"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        threads = []

        slug_list = []
        for row in results:
            question_detail = {
                'id': row[0],
                'slug': row[1],
                'difficulty': row[2],
                'status': row[3]
            }  

            if not self.filter_question(question_detail, filters):
                continue
            slug = question_detail['slug']
            slug_list.append(question_detail['slug'])
            IS_SUCCESS = False
            while not IS_SUCCESS:
                try:
                    url = "https://leetcode-cn.com/graphql"
                    params = {'operationName': "Submissions",
                        'variables':{"offset":0, "limit":20, "lastKey": '', "questionSlug": slug},
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

                    json_data = json.dumps(params).encode('utf8')

                    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive', 'Referer': 'https://leetcode-cn.com/accounts/login/',
                        "Content-Type": "application/json", 'x-csrftoken': self.csrftoken}  
                    resp = self.session.post(url, data = json_data, headers = headers, timeout = 10)
                    content = resp.json()
                    for submission in content['data']['submissionList']['submissions']:
                        if submission['statusDisplay'] == "Accepted":   
                            cursor.execute("SELECT COUNT(*) FROM last_ac_submission_record WHERE id =" + str(submission['id']))
                            if cursor.fetchone()[0] == 0:
                                IS_GET_SUBMISSION_SUCCESS = False
                                while not IS_GET_SUBMISSION_SUCCESS:
                                    code_content = self.session.get("https://leetcode-cn.com" + submission['url'], headers = headers, timeout = 10)

                                    pattern = re.compile(
                                        r'submissionCode: \'(?P<code>.*)\',\n  editCodeUrl', re.S
                                    )
                                    m1 = pattern.search(code_content.text)
                                    code = m1.groupdict()['code'] if m1 else None
                                    if not code:
                                        print('WARN: Can not get [{}] solution code'.format(slug))
                                        continue
                                    IS_GET_SUBMISSION_SUCCESS = True
                                                
                                submission_detail = (submission['id'], slug, submission['timestamp'], submission['lang'], submission['runtime'], code)
                                cursor.execute("INSERT INTO last_ac_submission_record (id, question_slug, timestamp, language, runtime, code) VALUES(?, ?, ?, ?, ?, ?)", submission_detail)
                                print("insert submission[%s] success" % (submission['id']))
                                self.conn.commit()                         
                            IS_SUCCESS = True
                            break   
                except (requests.exceptions.Timeout,requests.exceptions.ConnectionError) as error:
                    print(str(error))
                finally:
                    pass            
        cursor.close()

    def generate_question_markdown(self, question, path, has_get_code):    
        text_path = os.path.join(path, "{:0>3d}-{}".format(question['frontedId'], question['slug']))
        if not os.path.isdir(text_path):
            os.mkdir(text_path)   
        with open(os.path.join(text_path, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# [{}][title]\n".format(question['title']))
            f.write("\n## Description\n\n")
            text = question['content']

            content = html2text.html2text(text).replace("**Input:**", "Input:").replace("**Output:**", "Output:").replace('**Explanation:**', 'Explanation:').replace('\n    ', '    ')
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
                    f.write("\n``` %s\n" %(submission[1]))
                    f.write(submission[0].encode('utf-8').decode('unicode_escape'))
                    f.write("\n```\n")

            
            f.write("\n[title]: https://leetcode-cn.com/problems/{}\n".format(question['slug']))
            
    def generate_questions_submission(self, path, filters):  
        if not self.is_login:
            return 
        
        sql = """
            SELECT l.question_slug, l.code,l.language, q.frontend_id,max(l.timestamp) FROM last_ac_submission_record as l,question as q 
            WHERE l.question_slug == q.slug and q.status = 'ac' GROUP BY l.question_slug
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)

        filter_cursor = self.conn.cursor()
        for submission in cursor:
            filter_cursor.execute("SELECT id,slug,difficulty,status FROM question WHERE slug = ?", (submission[0],))
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

        text_path = os.path.join(path, "{:0>3d}-{}".format(submission[3], submission[0]))
        
        if not os.path.isdir(text_path):
            os.mkdir(text_path)   
        with open(os.path.join(text_path, "solution.class"), 'w', encoding='utf-8') as f:
            f.write(submission[1].encode('utf-8').decode('unicode_escape'))

    def close_db(self):
        self.conn.close()
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs = '?', default="note")
    parser.add_argument('-d', '--difficulty',
                            nargs = '+',
                            choices = ['Easy', 'Medium', 'Hard'],
                            help = "Specify the difficulty.\n"
                            "If not specified, all problems will be grasped.")

    parser.add_argument('-t', '--tags',
                            nargs = '+',
                            help = "Specify the tag")
    
    parser.add_argument('-v', '--verbose',
                            action = "store_true",
                            default = False,
                            help = "Verbose output")
    
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
    argsDict = vars(args)
    filters = {}


    test = LeetcodeCrawler()
    test.get_csrftoken()
    
    login_flag = True

    if argsDict.get('code') or argsDict.get('status'):
        if not (argsDict.get('username') and argsDict.get('password')):
            print("ERROR: choice problem by statu or generate submission code must set username and password!")
            sys.exit()
        else:
            is_login = test.login(args.username[0], args.password[0])
            if not is_login:
                print("ERROR: login account fail!")
                sys.exit()
        if argsDict.get('code'):
            filters['code'] = args.code
            if args.verbose:
                print('Specified code path is: {}'.format(args.code))
        if argsDict.get('status'):
            filters['status'] = args.status[0]
            if args.verbose:
                print('Specified statu is: {}'.format(args.status))


    if argsDict.get('difficulty') or argsDict.get('tags'):
        if argsDict.get('difficulty'):
            filters["difficulty"] = args.difficulty[0]
            if args.verbose:
                print('Specified difficulty is: {}'.format(args.difficulty))
        if argsDict.get('tags'):
            filters['tags'] = args.tags
            if args.verbose:
                print('Specified tag is: {}'.format(args.tags))


    test.connect_db(db_path)
    test.get_problems(filters)
    if argsDict.get('code'):
        test.get_ac_question_submission(filters)
        test.generate_questions_submission(args.output, filters)
      
    test.generate_questions_markdown(args.output, filters)
   
    test.close_db()
