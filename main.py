import math
import speedtest

wifi = speedtest.Speedtest()


download = wifi.download()

upload = wifi.upload()

print(download)
print(upload)
