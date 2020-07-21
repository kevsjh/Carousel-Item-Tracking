import requests
import json
import os
from inputDoc import *


from twilio.rest import Client


# function to get the delta between two array
def differenceSet(x, y):
    return list(set(x)-set(y))


tempFileList = []
tempJsonList = []

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}


# jsondata used by sg.carousel
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


# Check if the result file exists, if it does, store its content into an array
# This array is use to check if the item queried already exist previously and saved to the output file
# Result stored in the output file are items the user is not interested anymore, hence no notification will be sent regarding this items
# carouselResult.txt is the sample output file

    if(os.path.isfile('carouselResult.txt')) == False:
        tempFileList = []
    else:

        with open('carouselResult.txt', 'r') as f:
            for line in f:
                # remove "\n"
                tempFileList.append(line.rstrip())

                if 'str' in line:
                    break


# Total Item to be returned
    for i in range(totalCount):

        # Tempororay Json object to store each queried item's parameter
        tempJsonObject = {
            'itemName': '',
            'itemPrice': 0,
            'seller': '',
            'imageUrl': '',
            'itemDescription': ''
        }

        tempStringList = list()


# first 3 item under belowFold is the itemname,itemprice and itemdescription.
# may change in the future if sg.carousel changes their json response

        for x in range(3):

            if(x == 0):
                tempJsonObject['itemName'] = jsonResponse['data']['results'][i]["listingCard"]['belowFold'][x]["stringContent"]
            if x == 1:
                tempPrice = float(jsonResponse['data']['results'][i]["listingCard"]
                                  ['belowFold'][x]["stringContent"].replace('S$', ''))
                tempJsonObject['itemPrice'] = tempPrice

            if(x == 2):
                tempJsonObject['itemDescription'] = jsonResponse['data']['results'][i]["listingCard"]['belowFold'][x]["stringContent"]

            else:
                tempStringList.append(
                    jsonResponse['data']['results'][i]["listingCard"]['belowFold'][x]["stringContent"])

        tempJsonObject['seller'] = jsonResponse['data']['results'][i]["listingCard"]['seller']['username']
        tempJsonObject['imageUrl'] = jsonResponse['data']['results'][i]["listingCard"]['photoUrls']

        tempJsonList.append(json.dumps(tempJsonObject))


except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)


# Get the differences between the queried items and the items stored in the output file
# Below code will only append the differences found here to the output file
listHolder = differenceSet(tempJsonList, tempFileList)

# print(tempJsonList)
# print("\n")
# print(tempFileList)
# print("\n")
# print(listHolder)
v = open('carouselResult.txt', 'a+')

bodyMessageArray = []
for i in listHolder:

    v.write(i+"\n")
    tempJson = json.loads(i)
    a = "Item Name:" + str(tempJson['itemName'])+"\n"+'Item Price:' + str(
        tempJson['itemPrice'])+"\n"+'Seller:' + str(tempJson['seller'])+"\n"+"\n"
    bodyMessageArray.append(a)


v.close()

bodyMessage = ""
for i in bodyMessageArray:
    bodyMessage = bodyMessage+i


print(bodyMessage)

# print(bodyMessage)

# Notification Method
# Modify the code below different ways of notification such as , Discord Bot, Slacks message, facebook message, sms and such with their API

# Whatsapp Twillio API
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

if bodyMessage == "":
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello, there! There are no new items on Carousell for ' + queryName +
        ' for the price from '+str(minPrice)+' to '+str(maxPrice)+' SGD',
        to=os.environ['PHONE_NUMBER']
    )



else:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello, there! Today\'s new items on Carousell for ' + queryName +
        ' for the price from ' +
        str(minPrice)+' to '+str(maxPrice) +
        ' SGD are shown below\n\n' + bodyMessage,
        to=os.environ['PHONE_NUMBER']
    )

print(message.sid)
