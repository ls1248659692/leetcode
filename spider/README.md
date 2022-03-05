## 概述

爬取 LeetCode 题目及提交的 AC 代码的工具，存入到本地 Sqlite 数据库中，并支持生成相应的 README.md 文件。支持爬取指定状态、难度以及标签的题目以及 AC 代码。

## 运行环境

基于 Python3 运行，依赖 Python 库：

* requests
* requests_toolbelt
* html2text

## 使用说明

```
positional arguments:
  output

optional arguments:
  -h, --help            show this help message and exit
  -d {Easy,Medium,Hard} [{Easy,Medium,Hard} ...], --difficulty {Easy,Medium,Hard} [{Easy,Medium,Hard} ...]
                        Specify the difficulty. If not specified, all problems
                        will be grasped.
  -t TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        Specify the tag
  -v, --verbose         Verbose output
  -s {ac,notac,none} [{ac,notac,none} ...], --status {ac,notac,none} [{ac,notac,none} ...]
                        Specify the probelms statu. If not specified, all
                        problems will be grasped.
  -c CODE [CODE ...], --code CODE [CODE ...]
                        Code solution output path.
  -u USERNAME [USERNAME ...], --username USERNAME [USERNAME ...]
                        username
  -p PASSWORD [PASSWORD ...], --password PASSWORD [PASSWORD ...]
                        password
```

可选参数说明

| Name  | Full Name  | Type | Description   |
| ----  | ----       | ---- | ----          |
| d     | difficulty | str  | 难度：Easy，Medium，Hard |
| t     | tags       | str  | 题目标签  |
| s     | status     | str  | 题目状态， ac： 通过，notac：未通过，none：未尝试 |
| c     | code       | str  | 生成AC代码文件存入路径 |
| u     | username   | str  | Leetcode 账号名       |
| p     | password   | str  | Leetcode 密码         |
| v     | problems     | bool | 是否输出配置，默认不输出 |

**注：若指定了题目状态或者要爬取 AC 代码，必须要提供用户账号密码信息参数**

## 示例

有些会员题需要权限才能爬取题目，每次爬取前需要获取下 LEETCODE_SESSION 避免权限认证失败，生成 README.md 到 problems 目录中

``` shell
python3 leetcode_crawler.py problems -v -u username -p password
```


爬取所有 AC 的题目，生成文档到 problems 目录中，生成代码文件到 code 目录中

``` shell
python3 leetcode_crawler.py problems -s ac -c code -u username -p password
```
