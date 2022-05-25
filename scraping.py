# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Set your executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
# First scrape, the news title and paragraph summary
def mars_news(browser):
    url = 'https://redplanetscience.com'
    browser.visit(url)
# Optional delay for loading the page
# searching for elements with a specific combination of tag (div) and attribute (list_text
# also telling our browser to wait one second before searching for components
    browser.is_element_present_by_css('div.list_text', wait_time=1)

# Set up the HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    try:
        slide_elem = news_soup.select_one('div.list_text')

# Begin Scraping
# Output should be the HTML containing the content title 
# and anything else nested inside of that <div />


# Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()


# For example, if we were to use .find_all() instead of .find() 
# when pulling the summary, we would retrieve all of the summaries 
# on the page instead of just the first one.

# Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

return news_title, news_p



# ### Featured Images

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
# Tell BeautifulSoup to look inside the <img /> tag 
# for an image with a class of fancybox-image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

import pandas as pd

# Scrape the entire table with Pandas' .read_html() function.
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Convert our DataFrame back 
# into HTML-ready code using the .to_html() function
df.to_html


# Without this, the automated browser won't know to shut down—it will 
# continue to listen for instructions and use the computer's resources
browser.quit()


