from twitchAPI.twitch import Twitch
import configparser
import json
import twitter

def main():
    twitchChannelInfo = None
    try:
        twitchChannelInfo = getTwitchInformation()
    except:
        print("Error Getting Twitch Information")
        return
    twitchChannelInfoObject = twitchChannelInfo.get('data')[0]
    streamGame = twitchChannelInfoObject['game_name']
    streamTitle = twitchChannelInfoObject['title']
    streamUser = twitchChannelInfoObject['broadcaster_name']
    tweetToSend = "I am live %s in %s come check it out twitch.tv/%s" % (streamTitle, streamGame, streamUser)
    try:
        sendTweet(tweetToSend)
    except Exception as ex:
        print("Error Sending Tweet")
        return

def getConfigInformationAsString(section,value):
    config = configparser.ConfigParser()
    try:
        config.read(".\\appConfig.ini")
        return config[section].get(value)
    except:
        print("Either Section %s or value %s does not exist in file appConfig.ini \r\n read the readme on how to make the config file" % (section, value))
        return ""

def getTwitchInformation():
    twitchAppId = getConfigInformationAsString("TwitchAPI","TwitchAppId")
    twitchAppSecret = getConfigInformationAsString("TwitchAPI","TwitchAppSecret")
    broadcasterId = getConfigInformationAsString("TwitchAPI", "TwitchBoradcastId")
    twitch = Twitch(twitchAppId, twitchAppSecret)
    twitch.authenticate_app([])
    return twitch.get_channel_information(broadcasterId)

def sendTweet(tweetToSend):
    consumerKey = getConfigInformationAsString("TwitterAPI","TwitterConsumerAPIKey")
    consumerSecret = getConfigInformationAsString("TwitterAPI", "TwitterConsumerSecretKey")
    accessTokenKey = getConfigInformationAsString("TwitterAPI", "TwitterAccessToken")
    accessTokenSecret = getConfigInformationAsString("TwitterAPI", "TwitterAccessTokenSecret")
    api = twitter.Api(consumer_key=consumerKey,consumer_secret=consumerSecret,access_token_key=accessTokenKey,access_token_secret=accessTokenSecret)
    status = api.PostUpdate(tweetToSend)


if __name__ == "__main__":
    main()