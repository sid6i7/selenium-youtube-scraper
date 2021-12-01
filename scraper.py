from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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


if __name__ == "__main__":
  print('Creating driver...')
  driver = get_driver()

  print('Fetching videos...')
  videos = get_videos(driver)

  print(f"Found {len(videos)} videos")

  print('Parsing the first video..')

  # title, url, thumbnail_url, channel, views, uploaded, description

  video = videos[0]

  title_tag = video.find_element(By.ID, 'video-title')
  url = title_tag.get_attribute('href')
  title = title_tag.text

  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_tag = video.find_element(By.TAG_NAME, 'ytd-channel-name')
  channel_name = channel_tag.text

  misc_tag = video.find_element(By.ID, 'metadata-line')
  views = misc_tag.find_elements(By.TAG_NAME, 'span')[0].text
  uploaded = misc_tag.find_elements(By.TAG_NAME, 'span')[1].text

  description = video.find_element(By.ID, 'description-text').text
  print(' ')
  print("Title: ",title)
  print("URL: ",url)
  print('Thumbnail URL: ', thumbnail_url)
  print('Channel name: ', channel_name)
  print('Views: ', views)
  print('Uploaded: ', uploaded)
  print('Description: ', description)



