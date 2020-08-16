from django.shortcuts import render
#from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

class News:
    title=""
    link=""

'''******for times of india******'''
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
#print(r.content)
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')
toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[2:-13]
head_check=[]
toi_obj=[]

for h in toi_headings:
     x=News()
     x.title=h.text
     head_check.append(h.text)
     x.link=h.find('a').get('href')
     toi_obj.append(x)

'''******for the hitavada******'''

headers={"User-Agent":"Mozilla/5.0"}
h_r = requests.get("https://www.thehitavada.com/National.html",headers=headers)
h_soup = BeautifulSoup(h_r.content, 'html.parser')
h_headings = h_soup.findAll('h2')
h_links= h_soup.findAll("a")
#print(h_headings)
h_headings = h_headings[1:50]
h_obj=[]

for h,l in zip(h_headings,h_links):
    x =News()
    if h.text not in head_check:
        x.title = h.text
        x.link = l.get('href')
        h_obj.append(x)
#print(h_obj)

def pract(request):
    return render(request,'prac_app/pract.html',{'toi_obj':toi_obj,'h_obj':h_obj})
