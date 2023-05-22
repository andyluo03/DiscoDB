# Query

## ``GET`` /query

Headers:

```
Authorization: Bearer <token>
```

Body:

```json
{
    "channel_id" : "<channel_id>" ,
    "attributes" : {
        //Attributes is any JSON
    }
}
```

Response:

```json
{
    "message_ids" : [
        //Messages IDs of All Matches
    ]
}
```
