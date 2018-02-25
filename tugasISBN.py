# Nama		: I Made Narendra Putra
# NIM		: 155150201111328

import urllib.request, json
def getFromAPI(query):
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + query
    with urllib.request.urlopen(url) as addr:
        data = json.loads(addr.read().decode())
        return data

query = input("Masukkan nomor ISBN: ")
output = getFromAPI(query)

for i in output["items"]:
    print("Judul          : " + i["volumeInfo"]["title"])
    print("Pengarang      : ")
    for j in output["items"][0]["volumeInfo"]["authors"] : 
    	print("- "+ j)
    
    print("Penerbit       : " + i["volumeInfo"]["publisher"])
    print("Tanggal Terbit : " + i["volumeInfo"]["publishedDate"])