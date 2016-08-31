import urllib.request
url = input("put web url here")
with urllib.request.urlopen(url) as response:
    html = response.read()
    data = open("data.txt","w")
    print (html, file=data)
    data.close()
