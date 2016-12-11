
import CrawserManager
import time
import DatabaseModule
from pyquery import PyQuery as pyq

print "Start"

startNumber = 0

databaseStartNumber = 0

databaseStartNumber = DatabaseModule.getDatabaseTopLine()

databaseStartNumber = 591304

sss = CrawserManager.pk10GetLaterestData('http://www.bwlc.net/bulletin/trax.html')
if len(sss):
	jq = pyq(sss)
	li = jq(".tb td")
	content = li[0]
	print pyq(content).text()
	arr =  pyq(content).text().split(' ')
        qishu = arr[0]
        print qishu
        startNumber = int(qishu)
	startNumber = 591305
totalCount = 6000
currentNumber = startNumber

print startNumber,totalCount,databaseStartNumber

while startNumber - currentNumber <= totalCount:
	if currentNumber <= databaseStartNumber:
		break
	url = 'http://www.bwlc.net/bulletin/prevtrax.html?num={0}'.format(currentNumber)
	print url
	content = CrawserManager.crawserWithTarget(url)
	if len(content):
		jq = pyq(content)
		content = jq('.tb td').text()
		arr =  content.split(' ')
        if len(arr)<3:
		print 'none data'
		url = 'http://bbs.zhcw.com/kaijiang/bjpk10/{0}.html'.format(currentNumber)
		content = CrawserManager.pk10GetTargetData(url)
		if(len(content)):
			qishu = currentNumber
                	numbers = content
                	t = 'inset'
                	DatabaseModule.writeToDatabaseWith(qishu,numbers,t)
                	time.sleep(1)
                	currentNumber -= 1
		else:
			time.sleep(120)
	else:
		qishu = arr[0]
		numbers = arr[1]
		t = arr[2]+' '+arr[3]
		print qishu
		DatabaseModule.writeToDatabaseWith(qishu,numbers,t)
		time.sleep(1)
		currentNumber -= 1
else:
	print('end----------')
