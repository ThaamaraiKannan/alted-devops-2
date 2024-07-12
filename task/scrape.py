import requests

def website(webName):
    name = requests.get(webName)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(name.text)
    return

# website("https://timesofindia.indiatimes.com/")