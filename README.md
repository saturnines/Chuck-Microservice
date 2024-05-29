
# Microservice for Chuck

This microservice allows you to get sessions by user id or id.

## Base URL for Testing (Change as needed as I used Flask.)
http://127.0.0.1:5000

## Endpoints for the microservice.

### 1. Retrieve a session with user ID

**Endpoint:** `/sessions`

**Request:**
- Method: `POST`
- Headers: 
  - `Content-Type: application/json`
- Body:
  ```json
  {
    "user_id": 123
  }
  ```

**Example Request by bash script:**
```bash
curl -X POST http://127.0.0.1:5000/sessions \
     -H "Content-Type: application/json" \
     -d '{"user_id": 123}'
```

**Example Response from microservice:**
```json
[
  {
    "id": 1,
    "session_data": "Sample data "
  },
  {
    "id": 2,
    "session_data": "Sample data "
  }
]
```

### 2. Retrieve a session by ID

**Endpoint:** `/session`

**Request:**
- Method: `POST`
- Headers: 
  - `Content-Type: application/json`
- Body:
  ```json
  {
    "session_id": 1
  }
  ```

**Example Request by bash script:**
```bash
curl -X POST http://127.0.0.1:5000/session \
     -H "Content-Type: application/json" \
     -d '{"session_id": 1}'
```

**Example Response from microservice:**
```json
{
  "id": 1,
  "user_id": 123,
  "session_data": "Sample test data"
}
```
