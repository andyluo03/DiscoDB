# Quickstart

## Prerequisites

DiscoDB was written using Python 3.8, it has not been tested on other Python versions.

## Installation

Install DiscoDB:

```bash
git clone https://github.com/andyluo03/DiscoDB
```

Install Dependencies:

```bash
cd DiscoDB
pip install -r requirements.txt
```

## Connecting to Discord

1. Go to Discord > Settings > Advanced and enable Developer Mode.

2. Create a Discord server with two text channels: users and logs.

3. Visit the [Discord Developer Portal](https://discord.com/developers/applications) and click the "New Application" button in the top right.

4. After clicking create, click "Bot" and then the "Add Bot" button.

5. Find "Token" and click the copy button. Save this somewhere safe for later use.

6. Under Privileged Gateway Intents, toggle Message Content Intents.

7. Finally, click OAuth2 on the left, choose the "bot" scope and "Administrator" bot permissions. Then, copy the generated URL and invite it the bot to your server.

## Configuring DiscoDB

Create ``config.json`` under DiscoDB/src.

Linux/MacOs:

```bash
cd src
touch config.json
```

Then, populate config.json with:

```json
{
    "HEADERS" : {
        "User-Agent" : "DiscordBot",
        "authorization" : "Bot <Token>",
        "Content-Type" : "application/json"
    },
    "BASE_URL" : "https://discord.com/api",
    "USERS_CHANNEL_ID" : "<channel id of users>",
    "LOG_CHANNEL_ID" : "<channel id of logs>"
}
```

The Token is the token copied in step 5 of "Connecting to Discord." You can obtain channel id's by right clicking a channel and clicking copy id.

Do not include the alligator brackets!

## Launching

Deploy (this will change to a bash script soon):

```bash
python3 src/app.py
```

## First Requests

Call ``http://127.0.0.1:5000/setup`` with body:

```json
{
    "user": "<username>",
    "pwd": "<password>"
}
```

You have now successfully setup DiscoDB, a NoSQL database that promises infinite storage at no cost!
