import configparser
config = configparser.ConfigParser()
config['TWITTER'] = {'APP_KEY':input("PLease enter your app key:"),
                     'APP_SECRET':input("Please enter your app secret key:"),
                     'USER_OATH_TOKEN':input("Please enter your user OAth tonen:"),
                     ' USER_OATH_TOKEN_SECRET': input("please enter your user OAth token secret:")
                     }
with open('twitter_info.ini', 'w') as configfile:
    config.write(configfile)
                      
