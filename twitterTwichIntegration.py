from twitchAPI.twitch import Twitch
import configparser
import json

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
    tweetToSend = "I am live plaing %s where I am %s over at twitch.tv/%s" % (streamGame, streamTitle, streamUser)
    print(tweetToSend)

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

if __name__ == "__main__":
    main()