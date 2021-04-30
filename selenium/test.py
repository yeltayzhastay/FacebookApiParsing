from bs4 import BeautifulSoup
html = open("divs.html").read()
soup = BeautifulSoup(html)
print soup.find(id='abc1')