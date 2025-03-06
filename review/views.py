from django.shortcuts import render
from selenium import webdriver
import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = "dsw0zwafj", 
    api_key = "874289292168252", 
    api_secret = "WHr1OeCFxrVOTiqgx0vDZ-Zwo4w", # Click 'View API Keys' above to copy your API secret
    secure=True
)
# Create your views here.

def take_screenshot(url):
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--diable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    # print(browser)
    browser.get(url)

    total_height=browser.execute_script("return document.body.parentNode.scrollHeight")

    browser.set_window_size(1200, total_height)

    screenshot= browser.get_screenshot_as_png()

    browser.quit()
    
    santized_url =url.replace('http://','').replace('https','').replace('/','_').replace(':','_')

    upload_response = cloudinary.uploader.upload(
        screenshot,
        folder="screenshots",
        public_id= f"{santized_url}.png",
        resource_type='image'
    )

    print(upload_response)
    return upload_response

def index(request):
    take_screenshot("https://felix221123.github.io/my-portfolio-website/")
    return render(request, 'index.html')