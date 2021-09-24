def get_news(i):
    import requests
    import json

    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=f9192911d38b4b14926f327bdb4f76c5')

    data = json.loads(r.content)
    return data['articles'][i]['title']

