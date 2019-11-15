# Ucshell-Wash
这是一个有关查询贝壳洗衣机是否处于空闲状态的网站的源码，框架django+bootstrap

这也是一个有关查询贝壳洗衣机是否处于空闲状态的python程序，例程内仅有一斋与九斋，其他斋请自行修改

##源码
1、如果你只需要查询功能的源码，那么你只需要进入/GetWashinfo/views.py即可，我相信你会在里面找到你想要的。

2、如有任何不明白的地方，欢迎发送邮件至作者邮件candleshadow@qq.com

3、网站演示**http://47.98.242.45/**

##Authorization获取教程
###[写在前面]
可能会比较难，如果不想研究原理，那么欢迎直接进入我的网站
###http://47.98.242.45/ 注：手机端浏览
####准备工具：charles、一台安装了U净app的手机

###1、查看电脑ip地址
运行cmd，输入ipconfig
![Alt text](/readmeimg/1.1.png)
可以看到此时的ip地址是**10.18.146.186**
  
###2、修改charles的设置
打开charles
![Alt text](/readmeimg/2.1.png)
点击Proxy setting，将端口设置为6666


![Alt text](/readmeimg/2.2.png)
  
再点击Help -> SSL proxying -> Install charles root certificate on a Mobile Device or remote browser…

![Alt text](/readmeimg/2.3.png)

###3、打开手机wifi设置（我这里以ios为例子，安卓系统自行百度）
<img src="/readmeimg/3.1.jpg"  height="330" width="400">
<img src="/readmeimg/3.2.jpg"  height="330" width="400">

###4、安装证书并打开
打开手机浏览器，输入chls.pro/ssl安装证书（备注，校园网用户请先登陆后再修改代理）
<img src="/readmeimg/4.1.jpg"  height="330" width="400">
<img src="/readmeimg/4.2.jpg"  height="330" width="400">

###5、至此，前期准备到此完成

###6、当你在手机登陆完你的账号后，电脑端会捕获这样一个页面
![Alt text](/readmeimg/6.1.png)

**id:内的东西就是你的Authorization**
###写在最后，我怎么得出这个id就是Authorization的，这个就涉及抓包的分析了，碍于篇幅与为了不给大家增加额外的学习成本，我这里就不说了
###本教程仅供交流学习，禁止用于任何商业用途，谢谢
###[转载注明出处]
###Copyright©️ 鱼摆烛潮



