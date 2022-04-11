 
## Leetcode editor简介  
  在IDE中解决LeetCode问题,支持`leetcode.com`与`leetcode-cn.com`,满足基本的做题需求。  
  理论上支持: IntelliJ IDEA  PhpStorm  WebStorm  PyCharm  RubyMine  AppCode  CLion  GoLand  DataGrip  Rider MPS  Android Studio。  


### 安装  
- **通过插件库安装** 

![leetcode-editor](https://user-images.githubusercontent.com/33345911/162762222-857a72f1-4635-493e-8b20-cc2ba89dbfb1.png)

### 配置(第一次安装需要先配置)  
- **插件打开leetcode** 

![leetcode-editor](https://user-images.githubusercontent.com/33345911/162762446-e3b2d76d-fd05-43e7-9c41-de59ee70f53a.png)
 
- **配置路径**: `File` -> `settings`->`tools`->`leetcode plugin` 

![leetcode-config](https://user-images.githubusercontent.com/33345911/162762858-7ccf082e-39ab-4222-934d-f2a2970ebee9.png)
 
  - **`URL可选项`**: `leetcode.com`与`leetcode-cn.com`  
  - **`Code Type`**: `Java`,`Python`,`C++`,`Python3`,`C`,`C#`,`JavaScript`,`Ruby`,`Swift`,`Go` ,`Scala`,`Kotlin`,`Rust`,`PHP`,`Bash`,`SQL`   
  - **`LoginName`**: 登录用户名
  - **`Password`**: 登录密码  
  - **`Temp File Path`**: 临时文件存放目录  
  - **`proxy(HTTP Proxy)`**: 使用http代理,配置路径:`File` -> `settings`->`Appearance & Behavior`->`System Settings`->`HTTP Proxy`
  - **`Custom code template`**: 自定义代码生成模板 
  - **`LevelColour`**: 自定义题目难度颜色,重启后生效  
  - **`English Content`**: 题目显示英文描述  
  
### 窗口(主窗口右下角

![icon](https://user-images.githubusercontent.com/33345911/162762629-34aa1095-81aa-475e-90d4-597a9e502bec.png)
  
- **工具栏**:  
  - **`登录`**:两个网站的登录帐号不互通，切换网站需配置对应的用户  
  - **`退出`**:退出当前账户,如遇到登录错误,尝试先进行退出  
  - **`刷新`**:在未登录的情况下也可查看刷新加载题目，但是无法提交  
  - **`查找`**:输入内容后回车搜索，再次回车搜索下一个，只会搜索题库节点下  
  - **`折叠`**:折叠全部节点.  
  - **`配置`**:快捷跳转到配置界面  
  - **`清理`**:清理配置的缓存目录下的文件，两个网站对应的缓存目录不同，只会清理当前配置的网站下的。部分题目未提交的情况下慎重清理  

- **树**:  

![Problems](https://user-images.githubusercontent.com/33345911/162762982-f8bea8c2-7141-4064-a0dc-1339a14b2065.png)

  - **`Problems`**:全部题目  
  - **`Difficulty`**:难度分类  
  - **`Tags`**:类型分类  
  - **`Explore`**:探索内容,只包含题目,收费内容不支持;部分题目加载有顺序限制   
  - **`颜色`**:题目颜色代表题目难度  
  - **`符号`**:题目前`√`与`？`代表当前题目解答状态,探索下有 `$` 开头的为付费或者其他情况下无法查看的   
  
### 菜单   

- **菜单(在题目上右击出现)**:  

![upload-leetcode-code](https://user-images.githubusercontent.com/33345911/162763081-5149c9e4-6158-44b1-8343-b6a5435cbf56.png)

  - **`open question`**:打开题目,在题目上双击也可以打开  
  - **`open content`**:查看描述，包含图片(依赖 Markdown)  
  - **`Submit`**:提交题目  
  - **`Submissions`**:查看提交记录,在弹出的窗口上选择记录查看详情(`Show detail`)  
  - **`Run Code`**:运行代码,默认使用题目的测试用例  
  - **`Testcase`**:自定义测试用例  
  - **`favorite`**:添加或移除收藏
  - **`Clear cache`**:清理当前题目  
  - **`Timer`**:计时器,开启后在右下角状态栏提示解题时间    
