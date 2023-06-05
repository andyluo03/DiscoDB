# Setup

## ``POST`` /setup

Creates the first authorized user for the database, which should appear in the `users` channel in JSON format. The credentials for this user is the username and password in the request body.

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
    "message": "User created/<error message>",
    "status": "success/error"
}
```
