import json
import sys

import tweepy


class StdOutListener(tweepy.StreamListener):
    total_tweets = []

    def on_data(self, data):
        tweet = json.loads(data)

        StdOutListener.total_tweets.append(tweet)
        if len(StdOutListener.total_tweets) > 9:
            with open('sample.json', 'w') as output_fd:
                json.dump(StdOutListener.total_tweets, output_fd)

            sys.exit(0)
        #  if tweet.get('coordinates', None) is not None:
        #      print('\n\nFound a geotagged tweet!')
        #      print(tweet)
        #      print('Coordinates: ({})'.format(tweet['coordinates']))

        return True

    def on_exception(self, exception=None):

        print(exception)


def main():
    with open('.env', 'r') as env:
        content = env.readlines()
        env_vars = {
            key: value for key,
            value in [tuple(line.strip().split('=')) for line in content]
        }

    #  CONSUMER_KEY'
    #  CONSUMER_SECRET'
    #  OAUTH_TOKEN'
    #  OATH_SECRET'

    auth = tweepy.OAuthHandler(
        env_vars['CONSUMER_KEY'], env_vars['CONSUMER_SECRET']
    )
    auth.set_access_token(env_vars['OAUTH_TOKEN'], env_vars['OAUTH_SECRET'])

    api = tweepy.Stream(auth=auth, listener=StdOutListener())

    api.filter(track=['brexit'])


if __name__ == '__main__':
    main()
