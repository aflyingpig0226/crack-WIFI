# @Author  : ShiRui
import pywifi
from pywifi import const


class DetectionOfWifi:  # 创建扫描wifi的对象

	def gic(self):

		wifi = pywifi.PyWiFi()  # 获取网卡
		ifaces = wifi.interfaces()[0]  # 获取网卡的接口
		if ifaces.status() == const.IFACE_CONNECTED:  # 判断时候WiFi已经连接

			print("已经连接。")

		else:

			pass

	def bies(self):

		wifi = pywifi.PyWiFi()  # 获取网卡
		ifaces = wifi.interfaces()[0]  # 获取网卡的接口
		ifaces.scan()  # 扫描周围的wifi信号
		result = ifaces.scan_results()  # 接收扫描的结果
		for name in result:

			print(name.ssid)  # 遍历扫描的结果


if __name__ == "__main__":

	wifi = DetectionOfWifi()
	wifi.gic()
	wifi.bie()
