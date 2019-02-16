# 乘风龙王的代码库(python)
主要是一些随便写写的东西，其中有很多没写完的半成品，有的甚至从来没运行过。代码文件的编码为**utf-8无bom**。

此代码库所引用的其他第三方库在代码文件开头导入语句后面用注释给出库名，可通过pip安装。

### 文章
按时间顺序排列
* [用python编写小说网站爬虫](https://zhuanlan.zhihu.com/p/51309019)
* [用python编写控制网络设备的自动化脚本1：框架设计](https://zhuanlan.zhihu.com/p/53641620)
* [用python编写控制网络设备的自动化脚本2：显示](https://zhuanlan.zhihu.com/p/56108138)
* [用python编写控制网络设备的自动化脚本3：启动](https://zhuanlan.zhihu.com/p/56833809)

## 内容包含
### 工具
* **cflw字符串**：用来判断中文的函数和正则表达式，和一些计算处理字符串的函数。
* **cflw时间**：一些时间类。
* **cflw辅助**：一些装饰器，*没什么用*。
* **cflw工具_运算**：一些小函数

### 数学
* **cflw数学**：常用数学函数
* **cflw数学_向量**
* **cflw数学_平面几何**
* **cflw数学_图形**：颜色
* **cflw数学_矩阵**
* **cflw数学_随机**：抄袭c++标准库的\<random\>

### 网络
* **cflw网络地址**：提供对互联网协议(Internet Protocol)第4版和第6版(IPv4/IPv6)地址的解析与计算，提供对物理(Media Access Control，MAC)地址的解析与计算
* **cflw网络连接**：提供统一的接口，通过Telnet、SSH、Console等方式连接到网络设备。
* **cflw网络设备**：提供统一的接口对路由器、交换机等网络设备进行控制。
* **cflw网络设备_(品牌)**：控制不同品牌的网络设备
	* 已支持：思科（Cisco）、华为（Huawei）、华三（H3C）
	* 对不同品牌不同型号设备的支持程度取决于有没有模拟器或者我能否拿到真机做实验。有时候没法做实验，很多代码写出来没法验证是否可用。

### 爬虫
* **cflw爬虫**：提供爬虫相关实用工具
* **cflw爬虫_代理列表**：获取可用的HTTP代理
* **cflw小说下载**：从一些盗版小说网站上下载小说(～￣▽￣)～ 。

### 其他
* **cflw英语**：包含常用单词的字符串数组