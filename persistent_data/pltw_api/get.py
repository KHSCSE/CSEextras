import requests

base_url = 'https://cs-api.pltw.org/'
user_name = input("Type your username:")



# get the data
url_to_get = base_url + user_name # set the url
response = requests.get(url_to_get) # make a 'get' request
print(response.text) # view the response



# TODO use print() and type() to view the type of data of 'response' 


# TODO use print() and type() to view the type of data of 'response.txt' 

