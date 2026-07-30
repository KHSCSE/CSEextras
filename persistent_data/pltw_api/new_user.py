import requests

base_url = 'https://cs-api.pltw.org/'
new_user_name = input("What username would you like to use?")


url_to_create_new = base_url + "/newuser/" + new_user_name # set the URL
response = requests.post(url_to_create_new) # make a 'POST' request
print(response.text) # view the response
print("\nImportant: write down your username and password")

# Notice how the URL is created and a POST request is made