def get_w(city):
    import requests
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['weather'][0]['description']
    return ('The weater API predicts ' + format_add + ' in ' + city + ', with a temperature of ' + str(json_data['main']['temp']) + ' Kelvins or ' + str(json_data['main']['temp'] - 273) + ' degrees celsius')

