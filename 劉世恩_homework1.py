import requests
url = "https://www.google.com/search?q=genshin+impact&rlz=1C5CHFA_enTW987TW987&oq=genshin+impact&aqs=chrome.0.69i59j46i512j35i39j0i512l7.2151j0j7&sourceid=chrome&ie=UTF-8"
data = requests.get(url)
print(data)

print(data.text)