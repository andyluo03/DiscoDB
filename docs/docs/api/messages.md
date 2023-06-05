# Messages

## ``POST`` /messages

Posts a new document to a channel

Headers:

```
Authorization: Bearer <token>
```

Body:

```json
{
    "channel_id": "<channel_id>",
    "content" : {
        //DATA
    }
}
```

Response:

```json
{
    "message": "Data uploaded successfully/<error message>",
    "status": "success/error"
}
```

## ``PUT`` /messages

Edit a message by id in a channel

Headers:

```
Authorization: Bearer <token>
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
{
    "message": "Data edited successfully/<error message>",
    "status": "success/error"
}
```

## `GET` /messages

Gets message content by id

Headers:

```
Authorization: Bearer <token>
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
    "content": {
        //DATA
    },
    "message": "Data retrieved successfully/<error message>",
    "status": "success/error"
}
```

## ``DELETE`` /messages

Delete a message by id in a channel

Headers:

```
Authorization: Bearer <token>
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
{
    "message": "Data deleted successfully/<error message>",
    "status": "success/error"
}
```
