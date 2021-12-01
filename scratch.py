import requests
from bs4 import BeautifulSoup


YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

# Does not execute JavaScript
response = requests.get(YOUTUBE_TRENDING_URL)

with open('trending.html', 'w') as f:
  f.write(response.text)

page = BeautifulSoup(response.text, 'html.parser')

# print('Page Title:', page.title.text)

# Find all the video divs
video_divs = page.find_all('div', class_ = 'ytd-video-renderer')