from django.shortcuts import render
import requests
import urllib3
import threading
import re

#初始化get方式头文件
urllib3.disable_warnings()
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 (4309704352)',
'Authorization': ''}
#注：Authorization需要自行获取，原理为手机发送验证码后，登陆后U净所返回的内容
#这个源码不能直接debug在于此处的验证必须自己获取，获取教程请查看read.me
cookies={'acw_tc':'76b20fe815729591967326897e55cfbbd5557a69128a6e3a8e529467c8dc33'}


#九斋洗衣机二维码识别数据
nineuuidata=['0000000000000A0007555201812140077551',
'0000000000000A0007555201812140077997',
'0000000000000A0007555201812030076296',
'0000000000000A0007555201812140077648',
'0000000000000A0007555201812030075994',
'0000000000000A0007555201812140077558',
'0000000000000A0007555201812140078073',
'0000000000000A0007555201812140077634',
'0000000000000A0007555201812140077807',
'0000000000000A0007555201812140077965',
'0000000000000A0007555201812150078272',
'0000000000000A0007555201812150078601',
'0000000000000A0007555201812140077804',
'0000000000000A0007555201812140077815',
'0000000000000A0007555201812150078134',
'0000000000000A0007555201812150078430',
'0000000000000A0007555201812140077880',
'0000000000000A0007555201812140077828',
]
#一斋洗衣机二维码识别数据
uuidata=[
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201906200104902',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077774',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077790',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077866',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077562',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077770',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077649',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077737',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077545',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077890',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077591',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077885',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fapp.littleswan.com%2Fu_download.html%3Ftype%3DUjing%26%20uuid%3D0000000000000A0007555201808270055313',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201906090104533',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201906200104787',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812030076385',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140078002',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077812',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077891',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077631',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077881',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812140077907',
'https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http%3A%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D0000000000000A0007555201812030076006',
    ]

# Create your views here.
def home(request):
	return render(request, 'home.html')


#查询九斋信息
def nine(request):
	#获取洗衣机信息函数
	def GetWashinfo( data):
		#发起get请求
		a=requests.get('https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http:%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D'+data,verify=False,headers=headers,cookies=cookies)
		#将get返回的内容加入total列表
		total.append(a)
		#正则表达提取机器运行状态
		b=re.search(r'(?<=switch":).+(?=,"wash")',a.json()['result']['statusAll']).group()
		if(re.search(r'\d+',b).group()=='1'):
			Onlytime[a.json()['result']['no']]=str(a.json()['result']['remainTime'])
		else:
			Onlytime[a.json()['result']['no']]='0'

	#多线程实现
	thread=[]
	try:
		#初始化变量
		total=[]
		Onlytime={}
		#将所有洗衣机的查询同时进行，加快运行速度
		for i in range(len(nineuuidata)):
			a=threading.Thread(target=GetWashinfo, args=(nineuuidata[i],))
			thread.append(a)
			a.start()
		#等待所有线程执行完毕
		for t in thread:
			t.join()
		
	except:
			print('error')
	#输出结果，kong为当前空闲机器数量
	kong=0
	for i in range(len(nineuuidata)):        
		b=re.search(r'(?<=switch":).+(?=,"wash")',total[i].json()['result']['statusAll']).group()
		if(re.search(r'\d+',b).group()=='0'):
			kong=kong+1
	return render(request, 'nine.html',{"Onlytime":Onlytime,"kong":kong,})

#查询一斋信息
def one(request):
	def GetWashinfo1( data, only):
		a=requests.get(data,verify=False,headers=headers,cookies=cookies)
		total.append(a)
		b=re.search(r'(?<=switch":).+(?=,"wash")',a.json()['result']['statusAll']).group()
		if(re.search(r'\d+',b).group()=='1'):
			Onlytime[only]=str(a.json()['result']['remainTime'])
		else:
			Onlytime[only]='0'
	'''
	#单线程实现
	for i in range(len(uuidata)):
		t=requests.get('https://u.zhinengxiyifang.cn/api/LbUsers/5505567/getDeviceByQRCode?qrCode=http:%2F%2Fweixin.qq.com%2Fr%2FEj8rM5LE1M-rrdZQ92oAl%3Fuuid%3D'+uuidata[i],verify=False,headers=headers,cookies=cookies)
		total.append(t)
	'''
	#多线程实现
	thread=[]
	try:
		total=[]
		
		Onlytimelist=[
				  '1-01',
				  '2-01',
				  '2-02',
				  '3-01',
				  '3-02',
				  '4-01',
				  '4-02',
				  '5-01',
				  '5-02',
				  '6-01',
				  '6-02',
				  '7-01',
				  '7-02',
				  '8-01',
				  '8-02',
				  '9-01',
				  '9-02',
				  '10-01',
				  '10-02',
				  '11-01',
				  '11-02',
				  '12-01',
				  '12-02',
				  ]
		Onlytime={
				  '1-01':'',
				  '2-01':'',
				  '2-02':'',
				  '3-01':'',
				  '3-02':'',
				  '4-01':'',
				  '4-02':'',
				  '5-01':'',
				  '5-02':'',
				  '6-01':'',
				  '6-02':'',
				  '7-01':'',
				  '7-02':'',
				  '8-01':'',
				  '8-02':'',
				  '9-01':'',
				  '9-02':'',
				  '10-01':'',
				  '10-02':'',
				  '11-01':'',
				  '11-02':'',
				  '12-01':'',
				  '12-02':''}
		
		for i in range(len(Onlytimelist)):
			a=threading.Thread(target=GetWashinfo1, args=(uuidata[i],Onlytimelist[i]))
			thread.append(a)
			a.start()
		

		for t in thread:
			t.join()
	except:
		print('error')
	kong=0
	for i in range(len(total)):        
		b=re.search(r'(?<=switch":).+(?=,"wash")',total[i].json()['result']['statusAll']).group()
		if(re.search(r'\d+',b).group()=='0'):
			kong=kong+1
	return render(request, 'one.html',{"Onlytime":Onlytime,"kong":kong,})
