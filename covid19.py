from bs4 import BeautifulSoup
import requests
import time
from time import sleep
import datetime
from urllib import request

url="https://www.worldometers.info/coronavirus/"

logo = '''
╔═╗┌─┐┬─┐┌─┐┌┐┌┌─┐┬  ┬┬┬─┐┬ ┬┌─┐
║  │ │├┬┘│ ││││├─┤└┐┌┘│├┬┘│ │└─┐
╚═╝└─┘┴└─└─┘┘└┘┴ ┴ └┘ ┴┴└─└─┘└─┘
╔╦╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
 ║ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
 ╩ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─
'''
print(logo)

time = datetime.datetime.now().strftime('%d %B %Y @ %H:%M')

print("Checked on: ",time)

#Get Global Statistics

response = requests.get(url)

data = BeautifulSoup(response.text, "html.parser")

gcases=data.find(id="maincounter-wrap")
print(gcases.get_text())

gdeaths = gcases.find_next_sibling('div', id="maincounter-wrap")
print(gdeaths.get_text())

grecovered = gdeaths.find_next_sibling('div', id="maincounter-wrap")
print(grecovered.get_text())


web = request.urlopen(url).read().decode('utf8')
soup = BeautifulSoup(web, 'html.parser')


table = soup.find("table")
body = table.find('tbody')
rows = body.find_all('tr')

#Get Country Wise Statistics

print("\n\n")

print("Country\tTotal Cases\tNew Cases\tTotal Deaths\tNew Deaths\tRecovered\tActive Case\tCritical\tCases/Million POP\n")

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text for ele in cols]
    for col in cols:
        if col=="" or col==None:
            col=0
        print(str(col), end="\t\t")
    sleep(0.25)
    print("\n")


