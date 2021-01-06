import pandas as pd
from splinter import Browser 
from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape_all():
    browser = Browser('chrome', **executable_path, headless=False)
    title, paragraph = mars_news(browser)

    mars_data = {
        'title': title,
        'paragraph': paragraph,
        'image': featured_image(browser),
        'facts': mars_facts(),
        'hemispheres': hemisphere(browser)
    }
    return mars_data

# ### NASA Mars News
# * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
def mars_news(browser):
    browser.visit('https://mars.nasa.gov/news/')
    title = browser.find_by_css('div.content_title a').text
    paragraph = browser.find_by_css('div.article_teaser_body').text
    print(title, paragraph)
    return title, paragraph

# ### JPL Mars Space Images - Featured Image
# * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# * Make sure to find the image url to the full size `.jpg` image.
# * Make sure to save a complete url string for this image.
def featured_image(browser):
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.find_by_id('full_image').click()
    browser.links.find_by_partial_text('more info').click()
    featured_image_url = browser.find_by_css('figure.lede a')['href']
    return featured_image_url
    
# ### Mars Facts
# * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# * Use Pandas to convert the data to a HTML table string.
def mars_facts():
    mars_fact_html = pd.read_html('https://space-facts.com/mars/')[0].rename(columns={0:'labels',1:'measurements'}).to_html(classes='table table-stripped')
    return mars_fact_html

# ### Mars Hemispheres
# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# # * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
def hemisphere(browser):
    img_list = []
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    img_urls = browser.find_by_css('a.product-item h3')

    for link in range(len(img_urls)):
        hems_imgs = {}
        browser.find_by_css('a.product-item h3')[link].click()
        img_url = browser.links.find_by_text("Sample")['href']
        img_title = browser.find_by_css('h2.title').text
        img_list.append({'title': img_title, 'img_url': img_url})
        browser.back()
        
    browser.quit()
    return img_list

# Mars Hemispheres
# def hemisphere():
#     base_url = 'https://astrogeology.usgs.gov'
#     url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(url)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='item')
#     urls = []
#     titles = []
#     for item in items:
#         urls.append(base_url + item.find('a')['href'])
#         titles.append(item.find('h3').text.strip())
#     img_urls = []
#     for oneurl in urls:
#         browser.visit(oneurl)
#         html = browser.html
#         soup = BeautifulSoup(html, 'html.parser')
#         oneurl = base_url+soup.find('img',class_='wide-image')['src']
#         img_urls.append(oneurl)
#     hemisphere_image_urls = []
#     for i in range(len(titles)):
#         hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})
#     return hemisphere_image_urls





