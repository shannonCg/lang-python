import urllib.request
import urllib.parse

def read_text():
    with open("./movie_quotes.txt") as f:
        content = f.read()
        check_profanity(content.replace("\n",""))

def check_profanity(text_to_check):
    data = {"q": text_to_check}
    url = 'http://www.wdylike.appspot.com/?' + urllib.parse.urlencode(data)

    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
        if 'true' in content:
            print("Profanity Alert!")
        elif 'false' in content:
            print("This document has no curse words!")
        else:
            print("Could not scan the document propertly.")


read_text()