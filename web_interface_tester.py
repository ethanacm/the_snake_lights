import urllib2
import time
'''
for i in range(100):
    urllib2.urlopen("http://10.10.10.107:8080/colors/green")
    urllib2.urlopen("http://10.10.10.107:8080/colors/red")
'''



for i in range(300):
    urllib2.urlopen("http://10.10.10.107:8080/led/" + str(i) + '&r=255&g=0&b=255')
    time.sleep(50 / 1000.0)