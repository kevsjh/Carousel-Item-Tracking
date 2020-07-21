# Carousel-Item-Tracking
A web scraping python script performed on sg.carousell for items that user are keened on with a min and max price range
Able to send notification such as whatsapp messenge to notify user on new items listed on the website. Giving the user the chance to grab an item before others do


#
Files

main.py-main source code. 
    Perform web scraping on sg.carousell based on items that user are interested in.
    The script will check if there are any new items by comparing it to the items stored in the output file. Any new items will be written to the output file as well at the end of the script.
    Twilio whatsapp API can be also found here. 
    Can modify the API to send simple notification to user such as via Discord,Slack,Facebook Msg, whatsapp by using third party API such as twilio


inputDoc.py-input file. 
    Only change the content of this file item name, min price, max price to be tracked etc...

carouselResult.txt-output file. 
   This file will be used as the base comparision with the newly queried item
    Items stored in this output file are items *deemed* as not interested by the user. Hence any old items stored will not be stored here again and no notification will be sent to user regarding old items.

#
The package included here are
    requests package - to make curl request
    twilio.rest package - to integrate whatsapp message and send notification to user


# 
To run the python script on system locally, only main.py and inputDoc.py is needed.
You may need to perform pip install requests to install python requests module on the local machine if it doesn't exists 


#
To run on serverless system on the cloud, AWS lambda for example
Some packages mentioned are required to be uploaded as deployment file
