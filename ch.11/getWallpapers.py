#! python 3

#getWallpapers.py - downloads wallpapers from imgur

#saves the images from the page (loop this?)

import requests, os, bs4

url = 'https://imgur.com/t/3440x1440/sflfmCZ'  #starting url
os.makedirs('NewWallpapers', exist_ok = True) #store pictures in ./NewWallpapers

def getWallpapers():

    #TODO: find the first picture/download it (while loop)
    #<img src="https://i.imgur.com/9kz3nYO.png" 
    
    #class = "Gallery-ContentWrapper"
    #<div class="Gallery-Content--mediaContainer"
    #TODO: save image to new folder


    #downloading the page
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)     

    #find the first picture to download (not sure if this is right yet)
    picElem = soup.select('#src img')
    
    picUrl = 'http' + picElem[0].get('src')
    #download the image
    print('Downloading the image %s...' %(picUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
