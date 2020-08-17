from selenium import webdriver
import time
from bs4 import BeautifulSoup
from pprint import pprint
import time
import json
chrome_path = "/home/umesh/Desktop/chrome/chromedriver"
driver = webdriver.Chrome(chrome_path)
url = 'https://www.flipkart.com/search?q=oppo%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
data=driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML;")
driver.close()
page=BeautifulSoup(html,"html.parser")	

# empty list

phone_details=[]

# This div contain all mobile data

all_div=page.find_all("div",class_="bhgxx2 col-12-12")
for u in all_div:

# empty dictionary

	mobile_dict={}

# This div is containing oppo mobile name

	names=u.find_all('div',class_="_3wU53n")
	for j in names:

# it will convert into text format

		oppo=(j.get_text())

		# print(oppo)

# it will append all name in dictionary by name key

		mobile_dict["Name"]=oppo

# it will give ram and rom into text format

		ram=u.find("li",class_="tVe95H").text

		# print(ram)

# it will give ram in dicitonary by ram key

		mobile_dict["Ram"]=(ram[0:5])

# it will give rom in dicitonary by rom key

		mobile_dict["Rom"]=(ram[11:17])

# it will give processor in dicitonary by processor key

		processor=u.find_all("li",class_="tVe95H")
		pro=(processor[4].text)

		# print(pro)

		mobile_dict["Processor"]=pro[:-10]

# it will give price in dicitonary by price key

		price=u.find("div",class_="_1vC4OE _2rQ-NK").text

		# print(price)

		mobile_dict["Price"]=price

# it will give display in dictionary by display key

		display=u.find_all("li",class_="tVe95H")
		dis=(display[1].text)

		# print(dis)

		mobile_dict["Display"]=dis[:-8]

# it will give camera in dictionary by camera key

		camera=u.find_all("li",class_="tVe95H")
		cam=(camera[2].text)

		# print(cam)

		mobile_dict["Camera"]=cam

# it will give battery in dictionary by battery key

		battery=u.find_all("li",class_="tVe95H")
		batt=(battery[3].text)

		# print(batt)

		mobile_dict["Battery"]=batt[:-8]

# it will give warrenty in dictionary by warranty key

		warranty=u.find_all("li",class_="tVe95H")
		warr=(warranty[5].text)

		# print(warr)

		mobile_dict["Warranty"]=warr

# it will give rating in dictionary by rating key

		rating=u.find("div",class_="hGSR34").text

		# print(ratting)

		mobile_dict["Rating"]=float(rating)

# this is for images

		image=u.find("img")["src"]
		mobile_dict["Image"]=image

		# print(image)
		# pprint(mobile_dict)

# it is appending mobile_dict into list 

		phone_details.append(mobile_dict)

		# pprint(phone_details)

# it is used to write phone_details in json file

	op=open('opp.json','w+')
	du=json.dump(phone_details,op)
	op.close()
	po=open('opp.json','r+')
	lo=json.load(po)
	time.sleep(2)

# This in html format,it will write phone_details in html file oppo_phone.html 

mobile_detail = open("oppo_phone.html", "w+")
mobile_detail.write("<html>\n")
mobile_detail.write("<head>\n")
mobile_detail.write("<title>Oppo mobiles</title>\n")
mobile_detail.write("</head>\n")
mobile_detail.write("<body>\n")
mobile_detail.write("<table border=1 style=text-align: center;>")
mobile_detail.write("<tr>\n<td>S.No.</td>\n<td>Image</td>\n<td>Name</td>\n<td>Ram</td>\n<td>Rom</td>\n<td>Battery</td><td>Display</td><td>Rating</td><td>Processor</td><td>Warranty</td></tr>\n")
c=1

# Here it will pickup all value of key from phone_details 

for oppo in phone_details :
	image1 = oppo["Image"]
	name1 = oppo["Name"]
	ram1=oppo["Ram"]
	rom1=oppo["Rom"]
	battery1=oppo["Battery"]
	display1=oppo["Display"]
	rating1=oppo["Rating"]
	processor1=oppo["Processor"]
	warranty1=oppo["Warranty"]
	a = ' style="width:100px;height:200px"'
	mobile_detail.write("<tr>")
	mobile_detail.write("<td>"+str(c)+"."+"</td>"+"<td>"+'<img src="'+image1+'"'+a+'>'+"<td>"+name1+"</td>"+"</td>"+"<td>"+"Ram"+ram1+"</td>"+"<td>"+rom1+"</td>"+"<td>"+battery1+"</td>"+"<td>"+display1+"</td>"+"<td>"+str(rating1)+"</td>"+"<td>"+processor1+"</td>"+"<td>"+warranty1+"</td>")
	mobile_detail.write("/<tr>")
	c+=1
mobile_detail.write("</table>\n</body>\n</html>")




		


