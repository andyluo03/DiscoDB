# Login

## ``PUT`` /login

Headers:

```json
N/A
```

Body:

```json
{
    "user": "<username>",
    "pwd": "<password>"
}
```

Response:

```json
{
    "token" : "<jwt_token>",
    "user_id" : "<user_id>"
}
```
