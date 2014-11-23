from bs4 import BeautifulSoup
import requests
import unicodedata

r  = requests.get("https://docs.python.org/2/library/functions.html")
data = r.text
soup = BeautifulSoup(data)
names = []
descs = []
for name in soup.findAll("tt", {"class" : "descname"}):
	names.append(str(''.join(name.findAll(text=True))))
descs = soup.select('div dl dd p')
for desc in descs:
	print desc

print names
print descs
