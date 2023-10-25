# beginners code snip
# kluckner@htw-berlin.de
# purpose: read / present initial data from file

import json
  
f = open('tweets_ws23_v1.json')
data = json.load(f)

print("Number of Tweets:" , len(data))

# show tweet
tweetID = 0

print("Tweet", data[tweetID]["text"])
print("Component:", data[tweetID]["labels"]["topic"][0]['topic'])
print("Sentiment:", data[tweetID]["labels"]["sentiment"][0]['sentiment'])

f.close()