# Carousel-Item-Tracking
To track desired item in Singapore Carousel with a min and max price

#
File use case

lambda_function.py is the main source code. No changes needed to be done on this file

inputDoc.py is used as the input file. Only change the content of this file item name, min price, max price to be tracked etc...


# 
To run the system locally, only lambda_function.py and inputDoc.py is needed.
You may need to perform pip install requests to install python requests module on the local machine if it doesn't exists 


#
To run on serverless system on the cloud, for example AWS Lambda
Download all the files and zip it. Upload the file to aws lambda as it is.
