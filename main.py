import urllib.request
url = input("put web url here")
with urllib.request.urlopen(url) as response:
    html = response.read()
    data = open("data.txt","w")
    print (html, file=data)
    data.close()

# read a url
url = input("Put web url here:")
print(url)

# get a response
response = urllib.request.urlopen(url)
html = response.read()


# parse the response
print(response.read())
