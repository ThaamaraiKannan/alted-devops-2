import requests

def website(webName, url):
    name = requests.get(webName)
    with open(url, "w", encoding="utf-8") as f:
        f.write(name.text)
    return

# website("https://timesofindia.indiatimes.com/")