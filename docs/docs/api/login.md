# Login

## ``PUT`` /login

Headers:

```json
N/A
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
    "Authorization": "Bearer <token>",
    "message": "User logged in/<error message>",
    "status": "success/error"
}
```
