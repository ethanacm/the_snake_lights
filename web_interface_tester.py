import urllib2
for i in range(100):
    urllib2.urlopen("http://10.10.10.107:8080/colors/green")
    urllib2.urlopen("http://10.10.10.107:8080/colors/red")