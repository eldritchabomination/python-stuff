import urllib.request

# read a url
url = input("Put web url here:")
print(url)

# get a response
response = urllib.request.urlopen(url)
html = response.read()


# parse the response
