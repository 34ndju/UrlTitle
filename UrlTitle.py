import urllib.request
from bs4 import BeautifulSoup

print("Give me a URL, I'll give you the title. Input an empty string to stop")

URL = input("URL: \n")

while(URL != ""):
	req = urllib.request.urlopen(URL)

	contents = req.read()
	req.close()

	soup = BeautifulSoup(contents, 'html.parser')

	print(soup.title.string)

	URL = input("URL: \n")