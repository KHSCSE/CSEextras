import requests

base_url = 'https://cs-api.pltw.org/'
user_name = input("Type your username:")

# post
message = input("Type a message to post:")
url_to_post = base_url + user_name + '?text=' + message # set the URL
response = requests.post(url_to_post) # make a POST request
print(response.text) # view the response


# TODO run this program several times, make a few new posts
