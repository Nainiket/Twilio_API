import urllib.request, json 
with urllib.request.urlopen("https://app.atera.com/Admin#/devices") as url:
    data = json.loads(url.read().decode())
    print(data)