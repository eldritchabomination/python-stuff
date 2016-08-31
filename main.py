import urllib.request

url = input("Put web url here:")
print(url)

response = urllib.request.urlopen(url)
print(response.read())
