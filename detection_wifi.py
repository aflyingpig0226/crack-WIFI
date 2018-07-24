# @Author  : ShiRui
import pywifi
from pywifi import const


class DetectionOfWifi:

	def gic(self):

		wifi = pywifi.PyWiFi()
		ifaces = wifi.interfaces()[0]
		if ifaces.status() == const.IFACE_CONNECTED:

			print("已经连接。")

		else:

			pass

	def bies(self):

		wifi = pywifi.PyWiFi()
		ifaces = wifi.interfaces()[0]
		ifaces.scan()
		result = ifaces.scan_results()
		for name in result:

			print(name.ssid)


if __name__ == "__main__":

	wifi = DetectionOfWifi()
	wifi.gic()
	wifi.bies()
