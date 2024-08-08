#!/usr/bin/python3

import webbrowser

favweb = { "soap2day": "https://soap2day.pe/",
          "ytstv": "https://ytstv.lol/",
          "youtube": "https://www.youtube.com/",
          "github" : "https://github.com"
          }

def firefox(website):
    if(website=="soap2day"):
        webbrowser.open(favweb["soap2day"])
    elif(website=="ytstv"):
        webbrowser.open(favweb["ytstv"])
    elif(website=="youtube"):
        webbrowser.open(favweb["youtube"])
    elif(website=="github"):
        webbrowser.open(favweb["github"])
