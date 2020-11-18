import urllib.request
import json
import urllib
from xml.etree import ElementTree as ET
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import clipboard

def Shortener(link , key):

    
    url = link
    url = url.replace("&", "%26")

    keyword = key
    if keyword == "":
        keyword = url.split("/")[-1]

    requestURL = "https://shortener.tarundev.com/yourls-api.php" \
                + "?signature=92d16c5db3" \
                + "&action=shorturl" \
                + "&keyword=" + keyword \
                + "&format=json" \
                + "&url=" + url

    root = urllib.request.urlopen(requestURL).read()

    jsonn = json.loads(root)
    print('\n')

    try:
        status = jsonn['status']
        message = jsonn['message']
        short = jsonn['shorturl']
        title = jsonn['title']
    except:
        print(root)

    out = "STATUS:\t\t" + status + "\n" \
        + "MESSAGE:\t" + message + "\n" \
        + "TITLE:\t\t" + title + "\n" \
        + "SHORTURL:\t" + short + "\n"
    print(out)

    clipboard.copy(short)


    return out