import socket
import requests
import urllib.request
import urllib.parse
import os
import time
import sys
banner = '''  
  
   __    __    __      ____  _  _    _____  _  _  ____ 
  /__\  (  )  (  )    (_  _)( \( )  (  _  )( \( )( ___)
 /(__)\  )(__  )(__    _)(_  )  (    )(_)(  )  (  )__) 
(__)(__)(____)(____)  (____)(_)\_)  (_____)(_)\_)(____)
 _   _    __    ___  _  _  ____  ____/ ___             
( )_( )  /__\  / __)( )/ )( ___)(  _ \/ __)            
 ) _ (  /(__)\( (__  )  (  )__)  )   /\__ \            
(_) (_)(__)(__)\___)(_)\_)(____)(_)\_)(___/            
 ____  _____  _____  __                                
(_  _)(  _  )(  _  )(  )                               
  )(   )(_)(  )(_)(  )(__                              
 (__) (_____)(_____)(____)                                                                                                

Coded by Abartan Dhakal 
Facebook : /abartandhakal
Twitter : /Imhaxormad'''
print(banner)

def usetool():	
	while True:
		try:
			options = int(input('''
				Available Options are: 

				1. Http header extract
				2. Pagelink extracter
				3. Dns Lookup (NS,A record)
				4. Reverse IPLookup Tool
				5. ClickJacking Finder
				6. X-XSS Header Checker

				Enter the Desired Options : '''))
			break
		except:
			print("Enter the Desired Options:")

	if int(options) == 1 :
		httpheader = input("Enter the Target:")
		h = requests.get("http://api.hackertarget.com/httpheaders/?q="+httpheader)
		print(h.text)

	elif int(options) == 2 :
		pagelink = input("Enter the Target:")
		r = requests.get("http://api.hackertarget.com/pagelinks/?q="+pagelink)
		print(r.text)

	elif int(options) == 3 :
		reversedns = input("Enter the Target:")
		d = requests.get("http://api.hackertarget.com/dnslookup/?q="+reversedns)
		print(d.text)

	elif int(options) == 4 :
		reverseip = input("Enter the Target:")
		x = requests.get("http://api.hackertarget.com/reverseiplookup/?q="+reverseip)
		print(x.text)

	elif int(options) == 5 : 
		site = input("Enter the Target:")
		r = urllib.request.urlopen("http://"+site)
		x= r.getheader('X-Frame-Options') 
		if (x== "ALLOW" or x == "allow"):
			print("[*] Bingo! You caught Clickjacking, now exploit it ;) ")
		else:
			print("[-] Not Vulnerable to ClickJacking")
	elif int(options) == 6 :
		xss = input("Enter the Target:")
		c = urllib.request.urlopen("http://"+xss)
		b = c.getheader("X-XSS-Protection")
		if b == 0 :
			print("[*] Browser based XSS might be possible")
		else :
			print("[-] Browser Based XSS protection header is present")

		
	else : 
		print("[!] Sorry No Options than those available")

	# Ask if they want to perform further tests
	decision = input("[*] Do you want to perform other tests? (yes/no)")

	if(decision == "yes" or decision == "YES" or decision == "Yes"):
		usetool()

	else:
		print("[+] Thank you for using the tool")

usetool()
