import tweepy, json, urllib
from urllib2 import Request, urlopen
from credentials import *

# class to extract tweet

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print('Tweet text: ' + status.text) # prints the user tweet

        # extract the tweet excluding hashtag

        search_text_components = str(status.text).strip().split(" ")
        search_text = '+'.join(search_text_components[1:])
        print 'search text components:', search_text_components, search_text
        url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=" + search_text # Pass the user input to Giphy API
        request = Request(url)
        random_image = json.loads(urlopen(request).read())
        print random_image
        url = random_image['data']['image_url'] #parse json output
        testfile = urllib.URLopener()
        testfile.retrieve(url, "/Users/divyasingh/Documents/CC/Bot/twitter-bot/gif1.gif") # download the gif file
        api.update_with_media('gif1.gif') # tweet the gif file on twitter

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth) # use tweepy to communicate with twitter
    stream = tweepy.Stream(auth, MyStreamListener())
    stream.filter(track = ['#gifbot']) # track tweets having this filter

print "All done!"
