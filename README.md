Introduction:

Visiting many separate websites frequently to find out if content on the site has been updated can take a long time. Aggregation technology helps to consolidate many websites into one page that can show only the new or updated information from many sites. At its most basic, a news aggregator is a website that takes information from multiple sources and displays it in a single place.

Purpose:

Aggregators reduce the time and effort needed to regularly check websites for updates, creating a unique information space or personal newspaper. News aggregators give you the ability to read through the latest news stories that have an impact on you and your business, all from one convenient location.

Steps:

The first part of that workflow deals with determining news sources and gathering data from previously determined websites. This involves crawling a web page. The next part extracts articles from that gathered data. Next thedjango server is setup and then integrating everything together.

Features:

•	The objective of the web app is to present top news headlines to end users at the click of a button.

•	Hyperlink original news publication website- the user can beredirected to the source website for reading the complete news article.

•	Contents will be refreshed by clicking on the refresh button.

•	It has a simple and clean UI.

•	The web app requires no login details or credentials to view it.

Algorithms used:

•	Html Parsingis an Automated Scraping Technique done with JavaScript which targets linear or nested HTML pages is used. It is a fast and robust method that is used for text extraction, screen scraping, and resource extraction among others.

•	In scraping data from a website, the popular Python package BeautifulSoup is used. It parses the web page into the individual HTML/CSS components (right-click on web page and click on “Inspect” to see the HTML/CSS components). The web page hyperlink is given as an argument to create the “Soup” element from BeautifulSoup. The “Soup” element is used to select the components of the web page.

•	The template contains the static parts of the desired HTML output describing how the dynamic content will be inserted. Rendering them from the views.py file is done to show them on the screen.

How to use:

1.	Software Requirements:
PythonVersion3.7.4
Django Version3.0.8

2.	Install the above software and clone the repository to your local machine.

3.	Install the dependencies by running:
	pip install bs4
	pip install requests
  
4.	Navigate to the manage.py file then run the run the development serveron cmd
    python manage.py runserver
    
5.	The site will be available at 127.0.0.1:8000.
Please consider that a live web-scraping process is carried out every time you run the app, so there may be some crashes due to the failing status of some requests.

References:

•	https://www.youtube.com/watch?v=XEIV1ngG3c&list=PLgPJX9sVy92yWUMgLpWrXtegKxrWLRnRv

•	https://www.youtube.com/watch?v=OTmQOjsl0eg

•	https://www.youtube.com/watch?v=JT80XhYJdBw

•	https://www.youtube.com/watch?v=gvdSkBmjpbY&feature=emb_title

•	https://limeproxies.com/blog/top-10-web-scraping-techniques/

•	https://medium.com/@adeoyewole/scraping-news-articles-in-python-53c567282e25

•	https://github.com/miguelfzafra/Latest-News-Classifier

