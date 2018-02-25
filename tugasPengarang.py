# Nama      : I Made Narendra Putra
# NIM       : 155150201111328

import urllib.request, json
def getFromAPI(query):
    url = "https://www.googleapis.com/books/v1/volumes?q=inauthor:" + query
    with urllib.request.urlopen(url) as addr:
        data = json.loads(addr.read().decode())
        return data

query = input("Masukkan nama pengarang: ")
output = getFromAPI(query.replace(" ","%20"))

print("Judul Buku : ")
for i in output["items"]: 
     print("- "+ i["volumeInfo"]["title"])
