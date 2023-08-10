import requests
try:
    my_file = requests.get("asdfasdfasdfasd:asdfasfd;asdfasdfsdf:asdf")
except requests.exceptions.InvalidSchema:
    print("oh no")