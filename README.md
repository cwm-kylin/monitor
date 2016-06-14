
说明：通过采集业务线实现邮件，微信报警，利用rrdtool工具出图展示页面监控，前端画图展示不如Highcharts，有待改进。
# monitor 项目：业务线分布式监控程序
#主程序包含webmonitor和publicclass
启动monitor后，实现监控页面展示。

#detector是监控采集程序 ，利用计划任务定时检查业务线网站，将探测结果存入mysql数据库中。

###特别注意地方： 程序monitor是部署在linux服务器/opt中的，settings中的变量根据自己的需要修改，以及RRD画图的shell脚本RRD中的路径。

=======
