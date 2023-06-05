# New User

## ``POST`` /new_user

Headers:

```
Authorization: Bearer <token>
```

Body:

```json
{
    "name": "<username>",
    "password": "<password>"
}
```

Response:

```json
{
    "message": "User created/<error message>",
    "status": "success/error"
}
```
