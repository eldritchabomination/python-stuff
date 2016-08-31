import urllib.request
<<<<<<< HEAD
url = input("put web url here")
with urllib.request.urlopen(url) as response:
    html = response.read()
    data = open("data.txt","w")
    print (html, file=data)
    data.close()
=======

url = input("Put web url here:")
print(url)

response = urllib.request.urlopen(url)
print(response.read())
>>>>>>> 2dc3c8b8db0ee4a35a3cc54e8aa80b0005a4ccbe
