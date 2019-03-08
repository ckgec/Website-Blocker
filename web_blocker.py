import time
from datetime import datetime as dt

website_list=["www.facebook.com","www.fb.com","web.whatsapp.com"] #Enter the websites to be blocked

host_temp="hosts"
host_path="C:\Windows\System32\drivers\etc\hosts" #The file location of 'hosts' file in windows[To be changed as per your preference]
redirect="127.0.0.1" #localhost

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,21) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):  #Time to block website is between 21 (9:00P.M.) and 23(11:00 P.M.)[To be changed as per your need]
		print("Working Hours...")
		with open(host_path,'r+') as file:  #opening 'hosts' file with read and write permission
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+ website+"\n")  #Attaching the mentioned website in the hosts' file
	else:
		print("Fun Hours...")
		with open(host_path,'r+') as file:  #opening 'hosts' file with read and write permission
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):  #when current time is not between specified range then delete the website lists from 'hosts' file
					file.write(line)
				file.truncate()
	time.sleep(5) #Execute while loop after every 5 seconds
