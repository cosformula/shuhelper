# 上海大学便民查询系统 (SHUhelper) (Version 0.1.3)

## 简介
网站基于python flask 框架开发，python版本2.7.13。同时使用了python requests模块。

实例:(http://tool.dumbrabbit.com)
开发博客:(https://cosformula.github.io/)
## 使用

* 安装必要的模块 flask/requests/Pillow
* 运行 shu.py
* 打开浏览器访问 127.0.0.1:5000
# 更新记录

* ## 2016-09-01 (Version 0.1.0)
    * 第一个发布版本，目前功能有体育查询(晨跑及课外活动)、财务查询(财务处缴费)、校历查询(2016-2017)。

* ## 2016-09-02 (Version 0.1.1)
    * 增加了一卡通余额及最近流水查询的功能，通过乐乎社区的接口实现。
    * 网页排版的一点点微小修改。

* ## 2016-09-03 (Version 0.1.2)
    * 改掉了一个会导致乐乎一卡通查询崩溃的bug
    * 增加了财务处查询接口。
    * 半夜发现学校启用了新的财务处网站，连夜加了新版查询接口。
    * 增加了一个凑个数的按钮
    * 现在开始可以支持访问带验证码的接口了。
    * 网页排版的一点点微小修改。
* ## 2016-09-04 (Version 0.1.4)
    * 界面完全改版(但是有很大的兼容性问题，下一般会改正)
    * 增加了物理实验查询接口
    * 又增加了一个凑个数的按钮
    * 更改了error提示的样式

# 样式更新记录
* 第一版

* 第二版![Aaron Swartz](https://raw.githubusercontent.com/cosformula/shuhelper/master/img/version2.png)