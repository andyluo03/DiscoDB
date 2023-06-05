import secrets
import json

print("----------------------------------------------------------------")
print("Welcome to DiscoDB :)")
print("----------------------------------------------------------------")

# prompt user for Discord Bot Token
token = input("First, please enter your Discord Bot Token: ")

# get users channel id and log channel id
users_channel_id = input("\nNext, please enter the channel id for the users channel: ")
log_channel_id = input("\nFinally, please enter the channel id for the log channel: ")

print("\nThat's all we need! Now, we'll create a config.json file for you, which contains this information, along with a secret key that we'll generate for you for authentication purposes.")
print("\nGenerating secret key...")
secret_key = secrets.token_hex(32)
print("Secret key generated!")
print("\nHere is the secret key we generated for you: " + secret_key)
print("Make sure not to share this with anyone!")

print("\nCreating config.json file...")
config = {
    "HEADERS": {
        "User-Agent": "DiscordBot",
        "authorization": "Bot " + token,
        "Content-Type": "application/json"
    },
    "BASE_URL": "https://discord.com/api/",
    "USERS_CHANNEL_ID": users_channel_id,
    "LOG_CHANNEL_ID": log_channel_id,
    "SECRET_KEY": secret_key
}
# create file in src directory
with open("src/config.json", "w") as outfile:
    config_json = json.dumps(config, indent=4)
    outfile.write(config_json)
    
# for testing purposes
# with open("src/config-test.json", "w") as outfile:
#     config_json = json.dumps(config, indent=4)
#     outfile.write(config_json)
    
print("config.json file created!")

print("\nThat's all! There's just a few more steps to get DiscoDB up and running, and you can find them in the documentation at this link: https://andyluo03.github.io/DiscoDB/quickstart/")






