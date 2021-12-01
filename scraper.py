from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')

  driver = webdriver.Chrome(options=chrome_options)

  return driver


def get_videos(driver):

  driver.get(YOUTUBE_TRENDING_URL)

  VIDEO_DIV_TAG = 'ytd-video-renderer'
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)

  return videos


def get_details(videos):
  titles = []
  urls = []
  thumbnail_urls = []
  channel_names = []
  views = []
  uploads = []
  descriptions = []
  for video in videos:
    title_tag = video.find_element(By.ID, 'video-title')
    url = title_tag.get_attribute('href')
    urls.append(url)
    title = title_tag.text
    titles.append(title)

    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')
    thumbnail_urls.append(thumbnail_url)

    channel_tag = video.find_element(By.TAG_NAME, 'ytd-channel-name')
    channel_name = channel_tag.text
    channel_names.append(channel_name)

    misc_tag = video.find_element(By.ID, 'metadata-line')
    view = misc_tag.find_elements(By.TAG_NAME, 'span')[0].text
    views.append(view)
    upload = misc_tag.find_elements(By.TAG_NAME, 'span')[1].text
    uploads.append(upload)

    description = video.find_element(By.ID, 'description-text').text
    descriptions.append(description)

  videos_dict = {
    'Title': titles,
    'URL': urls,
    'Views': views,
    'Channel': channel_names,
    'Uploaded': uploads,
    'Description': descriptions,
    'Thumbnail': thumbnail_urls
  }

  return videos_dict




if __name__ == "__main__":
  print('Creating driver...')
  driver = get_driver()

  print('Fetching videos...')
  videos = get_videos(driver)

  print(f"Found {len(videos)} videos")

  # title, url, thumbnail_url, channel, views, uploaded, description
  print('Fetching videos data...')
  videos_dict = get_details(videos)
  
  videos_df = pd.DataFrame(videos_dict)

  print('saving to CSV')
  videos_df.to_csv('videos.csv', index = False)



