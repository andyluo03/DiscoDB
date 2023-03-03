# Query

## ``get`` /query

Headers:

```json
token: <jwt-token> 
user-id: <user-id>
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
