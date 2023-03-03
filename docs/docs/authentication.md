# Authentication

DiscoDB uses JSON Web Tokens (JWTs) to authenticate requests. To obtain one, use the login endpoint. Then, authenticate your requests by adding the headers:

```json
token: <token>
user-id: <user-id>
```

## Best Practices

* Do not push your tokens to version control. Otherwise, your teammates will be mad at you!!!
* Use sessionStorage instead of localStorage on browsers to prevent XSS attacks
