# DiscoDB
Have you ever had random pieces of JSON lying around and thought, *where could I possibly store objects so precious?* Companies like MongoDB don't understand that JSON is more than just JavaScript Object Notation; rather, it has the power to hold the memories most dear to us. They charge you, the people, ridiculous prices simply to find these beautiful memories a home. Well, in today's economy, we think that is unaccepatable. That's why we created DiscoDB, a novel NoSQL document database with unlimited - that's right, *unlimited* - storage. It's completely free!

## Getting Started
1) Create a Discord server. 
2) In this server, create the following two required channels: `users` and `logs`. You can also create channels for collections of data within your database, as well as chat channels (or really anything you can imagine). Here is an example of a channel organization to start out with: 
<img width="224" alt="image" src="https://user-images.githubusercontent.com/66141551/221403694-be571483-db44-4148-af09-919d0ad75eaf.png">

3) Before being able to use `DiscoDB`, you need to create the `config.json` file at the location `~/src/config.json` with data pertaining to your specific discord server. Here's a template: 

```json
{
    "HEADERS" : {
        "User-Agent" : "DiscordBot",
        "authorization" : "Bot <TOKEN>", // remove angled brackets when substituting (<>)
        "Content-Type" : "application/json"
    },
    "BASE_URL" : "https://discord.com/api",
    "USERS_CHANNEL_ID" : "<ENTER_USERS_CHANNEL_ID>",
    "LOG_CHANNEL_ID" : "<ENTER_LOG_CHANNEL_ID>"
}
```

- To get your bot token read [this](https://discord.com/developers/docs/getting-started#creating-an-app) **MAKE SURE NOT TO PUSH YOUR BOT TOKEN TO REMOTE** ... or else everyone on your team will get mad at you :(
- To get the channel IDs of the `users`and `logs` channels, first make sure you're in developer mode on discord (`User Settings > Advanced > Developer Mode`). Right click one of the channels and then click `Copy ID`; you can then paste the ID in it's corresponding place in the JSON file.

4) Send a POST Request to the `/setup` API endpoint with a request body:
```
{
  "user" = "<insert_username>", // remove angled brackets when substituting
  "pwd" = "<insert_password>"
}
```
This will create the first authorized user for your database, with the credentials (username and password) that you specified. If the user was created successfully, they should show up in your `users` channel in the form of stringified JSON. After logging in as this user (using a different API endpoint `/login`), you will be able to manipulate the data in your database using other endpoints. More in-depth explanations of these endpoints are below. 

# Endpoints

## baseurl/setup

### POST

Creates the first authorized user for the database, which should appear in the `users` channel in JSON format. The credentials for this user is the username and password in the request body.

`Headers:`
```
N/A
```

`Body:`
```
{
    "user" = "<username>",
    "pwd" = "<password>"
}
```

`Response:`
```
N/A
```

## baseurl/login

### PUT

Logs in a specific user if 
1) the credentials passed through the request body are correct for that user
2) the user exists in the `users` channel

`Headers:`
```
N/A
```

`Body:`
```
{
    "user" = "<username>",
    "pwd" = "<password>"
}
```

`Response:`
```
{
    "token" : "<jwt_token_for_user>",
    "user_id" : "<user_id>" // this is equivalent to the discord message id for the user in the users channel
}
```

## baseurl/new_user [requires auth header]

### POST

Creates a new user using credentials passed through the request body. This will only be successful if the current user (described by `user-id` in `headers`) is already successfully logged and if their session is successfully validated by the JWT token (also in `headers`). If successful, the created user will appear in the `users` channel.

`Headers:`
```
token : <jwt_token> // was in the response when the current user was logged in
user-id : <user-id>
```

`Body:`
```
{
    "new_user" = "<new_username>",
    "new_pwd" = "<new_password>"
}
```

`Response:`
```
N/A
```

## baseurl/message [requires auth header]

## baseurl/query [requires_auth header]


