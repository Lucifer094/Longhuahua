[toc]

# 1.任务描述：

为了实现中文文本在不同语言转换后，重新变为中文文本的过程，使用了三种方式进行，最终决定使用baidu的翻译接口进行实现，具体文件为TranslateBaidu.py。

# 2.文件描述：

* `TranslateBaidu.py` ：完成了从中文-小语种-中文的过程。
* `Baidu_Text_transAPI.py`:百度翻译的官方使用文档。
* `TranslateYouDao.py`:使用有道网页爬虫翻译，但是仅限于中英文互译功能。
* `TranslatePack.py`:一个python的translate包，不好用，翻译出来的结果有问题，并且不是所有话都可以进行翻译，很不推荐。

# 3.代码使用：

后台直接挂起`TranslateBaidu.py` 脚本文件即可实现将中文文本-中文文本，中间的小语种转换过程省略不输出。

*注*：暂时实现的输入文本只能为一整段没有换行符的文本，如果有会崩掉。

*注*：需要按照[百度翻译平台](https://api.fanyi.baidu.com/)的注册流程进行注册，并将下面的内容替换为自己的id和key才能运行脚本。

appid = 'INPUT_YOUR_APPID'
appkey = 'INPUT_YOUR_APPKEY'