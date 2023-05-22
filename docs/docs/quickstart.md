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

7. Finally, click OAuth2 > URL Generator on the left, choose the "bot" scope and "Administrator" bot permissions. Then, copy the generated URL and invite it the bot to your server.

## Configuring DiscoDB

Run ``db_setup.py`` to create the database using the command below:

Linux/Mac:

```bash
python3 db_setup.py
```

Follow the instructions provided by the setup wizard. It will prompt you to enter the Discord Bot Token from step 5 of "Connecting to Discord." It will also ask for the channel ids for the users and logs channels, which you can obtain by right clicking each channel and clicking copy id.

After the setup is complete, confirm that a ``config.json`` file in the ``src`` directory has been created and populated with the correct information. This file contains the configuration for DiscoDB and should look something like this:

```json
{
    "HEADERS" : {
        "User-Agent" : "DiscordBot",
        "authorization" : "Bot <Token>",
        "Content-Type" : "application/json"
    },
    "BASE_URL" : "https://discord.com/api",
    "USERS_CHANNEL_ID" : "<channel id of users>",
    "LOG_CHANNEL_ID" : "<channel id of logs>",
    "SECRET_KEY" : "<secret key>"
}
```

## Launching

Deploy (this will change to a bash script soon):

```bash
cd src
python3 app.py
```

## First Requests

Call ``http://127.0.0.1:5000/setup`` with body:

```json
{
    "name": "<username>",
    "password": "<password>"
}
```
This will create the first user with the given username and password. If it succeeded, the users channel for your server should now contain a user.

You have now successfully setup DiscoDB, a NoSQL database that promises infinite storage at no cost!
