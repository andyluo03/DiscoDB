# Messages

## ``POST`` /messages

Posts a new document to a channel

Headers:

```json
token: <jwt-token> 
user-id: <user-id>
```

Body:

```json
{
    "channel_id": "<channel_id>"
    "content" : {
        //DATA
    }
}
```

Response:

```json
N/A
```

## ``PUT`` /messages

Edit a message by id in a channel

Headers:

```json
token: <jwt-token> 
user-id: <user-id>
```

Body:

```json
{
    "channel_id": "<channel_id>",
    "message_id": "<message_id>",
    "content" : {
        //DATA
    }
}
```

Response:

```json
N/A
```

## `GET` /messages

Gets message content by id

Headers:

```json
token: <jwt-token> 
user-id: <user-id>
```

Body:

```json
{
    "channel_id": "<channel_id>",
    "message_id": "<message_id>"
}
```

``Response:``

```json
{
    //JSON
}
```

## ``DELETE`` /messages

Delete a message by id in a channel

Headers:

```json
token: <jwt-token> 
user-id: <user-id>
```

Body:

```json
{
    "channel_id": "<channel_id>",
    "message_id": "<message_id>"
}
```

Response:

```json
N/A
```
