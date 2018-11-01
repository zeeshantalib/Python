#----- Download Image From any website - urllib.request.urlretrieve(url,"Zee.jpg")

import random
import urllib.request

def download_image(url):
    name=random.randrange(1,1000)
    fullname=str(name)+".jpg"
    urllib.request.urlretrieve(url,fullname)
download_image("http://4.bp.blogspot.com/-FyLDEusIQS0/WtghV-3aQwI/AAAAAAAAEG4/IdyXoGKI86MyYXJk3ntwZuUBZNcV8w5owCK4BGAYYCw/s320/zeeshantalib.jpg")
