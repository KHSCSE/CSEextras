import requests

print("\nBefore this program will run correctly, there is one TODO below.\n")

base_url = 'https://cs-api.pltw.org/'
user_name = input("Type your username:")

# vote
message_num = input("Which message would you like to vote for?")
url_to_vote = base_url + user_name + 'TODO' + message_num # set the URL
response = requests.post(url_to_vote) # make a post request
print(response.text) # view the response


print("\nNow that it is working, run this program several times and vote for a few posts")
