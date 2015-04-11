import json
import requests

import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.

    data = requests.get(url).text
    data = json.loads(data)

    top_artists = data['topartists']
    artists = top_artists['artist']

    top_artist = artists['rank'==1]
    top_artist_name = top_artist['name']
    return top_artist_name # return the top artist in Spain
'''Official Answer:

    data = requests.get(url).text
    data = json.loads(data)	

    print data['topartists']['artist'][0]['name']

if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain

	url = # fill this in 
    print api_get_request(url) 

