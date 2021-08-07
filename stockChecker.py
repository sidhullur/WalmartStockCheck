from bs4 import BeautifulSoup
import requests
import webbrowser
import time

# Defines headers to enable full html access
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

url = "https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/994712501"

print("Monitoring item stock. The buy page will be opened immediately on restock.")

while True: # Looping the stock check procedure
    try: # Continues looping through spam detection
        res = requests.get(url, headers=HEADERS) # Scrapes html. Uses headers to receive all html code.
        soup = BeautifulSoup(res.text, "html5lib") # Parsing the html text
        info = soup.find_all("link", {"itemprop": "availability"}) # Extracting html code which conveys availability

        availability = info[0]["href"] # Extracting availability status

        if availability == "//schema.org/InStock": # Checking if item in stock
            print("ALERT! The item has been restocked. Please purchase quickly.") # Alerting restock
            webbrowser.open(url) # Opening broswer for purchase
            break

        time.sleep(10) # runs procedure in 10 second intervals to prevent spamming
    except:
        time.sleep(10) # 10 second cooldown to prevent spam
        continue