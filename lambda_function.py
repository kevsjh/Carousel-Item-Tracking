import requests
import json
import numpy
from inputDoc import *


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

jsonData = {
    "countryId": "1880251",
    "filters": [],
    "locale": "en",
    "prefill": {"prefill_price_start": minPrice, "prefill_price_end": maxPrice},
    "query": queryName,
    "count": totalCount

}


data = json.dumps(jsonData)

try:
    response = requests.post(
        'https://sg.carousell.com/api-service/filter/search/3.3/products/', headers=headers, data=data)
    jsonResponse = response.json()


    for i in range(totalCount):

        tempString = list()

        for x in range(3):
            if x == 1:
                tempPrice = float(jsonResponse['data']['results'][i]["listingCard"]
                                ['belowFold'][x]["stringContent"].replace('S$', ''))
                tempString.append(tempPrice)

            else:
                tempString.append(
                    jsonResponse['data']['results'][i]["listingCard"]['belowFold'][x]["stringContent"])

        tempString.append(jsonResponse['data']['results']
                        [i]["listingCard"]['seller']['username'])
        tempString.append(jsonResponse['data']['results']
                        [i]["listingCard"]["photoUrls"])

        print(tempString)

except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)
