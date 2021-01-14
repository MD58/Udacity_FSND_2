## README

Kindly check the readme files for installation / set up details:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

## Api Reference

### Getting Started
- After running the backend server locally, you should be able to access all endpoints using the base url ```http://127.0.0.1:5000/api/```
- This version does not required authentication or API Keys.

### Error Handling
Error are returned as JSON objects in the following format:
```json
{
  "success" : False,
  "error" : 400,
  "message" : "bad request"
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Unprocessable


### Endpoints
#### GET /categories
