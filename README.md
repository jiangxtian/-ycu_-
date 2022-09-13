# ***！！！此版本并非全自动打卡！！！*** 
***
## **一.&emsp;需要自己手动抓包获取Cookie**
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1. 可以用手机客户端APP HttpCanary 抓取:&emsp; http://jkttb.ycu.edu.cn:8082/microapp/health_daily/login &emsp;下的请求cookie或者响应的Setcookie
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2. Cookie 期限大概在一小时，可以上午11点之后抓取，上下午打卡公用一个Cookie节省抓包时间
## **二.&emsp;解决全自动打卡的方式**
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1. 知道 &emsp; http://jkttb.ycu.edu.cn:8082/microapp/health_daily/login &emsp; 的参数code的变化规律，获取Set Cookie
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2. 模拟点击链接之后，抓包获取cookie
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;3. 欢迎大家提供更多的想法以及建议意见，可联系QQ:1918303695
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 最后可将代码上传至云函数，开启定时触发器实现全自动打卡
