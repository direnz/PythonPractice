#! pytho#getWallpapers.py - downloads wallpapers from imgur

#loads the imgur home page

#searches for 3440x1440 wallpapers

#clicks on first result

#saves the images from the page (loop this?)

import requests, os, bs4

url = 'https://imgur.com/'  #starting url
os.makedirs('NewWallpapers', exist_ok = True) #store pictures in ./NewWallpapers

def getWallpapers():
    
    #TODO: get to the search bar and enter in 3440x1440 wallpapers

    #TODO: click on the first result

    #TODO: find the first picture/download it (while loop)
    #<img src="https://i.imgur.com/9kz3nYO.png" 
    
    #class = "Gallery-ContentWrapper"
    #<div class="Gallery-Content--mediaContainer"
    #TODO: save image to new folder


    #downloading the page
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #find the picture to download
    picElem = soup.select('#src img')
    
    picUrl = 'http' + picElem[0].get('src')
    #download the image
    print('Downloading the image %s...' %(picUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()


    #This might be an alternate way of referencing the img. 
    picElem = soup.select('.imageContainer img:nth-of-type(2)')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
