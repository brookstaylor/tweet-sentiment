import tweepy
import csv
from textblob import TextBlob

consumerKey = 'AXPpBN95g4iGYH5dCbCTK4Ge0'
consumerSecret = '5Ql3WzXmSFgIMGbxxpRZyPX2XSMWqV3S70BX7urvqViNzSXtmx'

accessToken = '347582271-ym89UQElvR0BYx6cJOWx0HFj1uvznnQobz2W9CSm'
accessTokenSecret = 'nUk3J8iJWWZh1oHlMHR6XhR5NDX5Q3vU6pfssnxBcH68h'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

searchTerm = input("""What's on your mind? I can make a documennt
	to tell you what twitter has to think of it. Type in a topic 
	word and let's see what the world thinks about it: """)
publicTweets = api.search(searchTerm)

myFile = open('tweetSentiment.csv', 'w')

with myFile:
	myLabels = ['positive', 'negative']
	writer = csv.DictWriter(myFile, fieldnames=myLabels)
	writer.writeheader()

	for tweet in publicTweets:
		analysis = TextBlob(tweet.text)
		if analysis.sentiment.polarity >= 0:
			writer.writerow({'positive' : tweet.text})
		else:
			writer.writerow({'negative' : tweet.text})


