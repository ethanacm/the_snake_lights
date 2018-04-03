import urllib2
import time
'''
for i in range(100):
    urllib2.urlopen("http://10.10.10.107:8080/colors/green")
    urllib2.urlopen("http://10.10.10.107:8080/colors/red")
'''



for i in range(5,300):
    urllib2.urlopen('http://10.10.10.107:8080/led/' + str(i) + '?r=0&g=0&b=0')
    #time.sleep(50 / 1000.0)