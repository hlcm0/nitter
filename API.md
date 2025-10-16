# API Endpoint Documentation

## Status Endpoint

### GET /api/@name/status/@id/

Returns JSON data for a specific tweet.

#### Parameters
- `@name`: Twitter username (e.g., "jack", "mobile_test")
- `@id`: Tweet ID (numeric, max 19 characters)

#### Response Format

```json
{
  "author": {
    "username": "string",
    "fullname": "string", 
    "id": "string"
  },
  "text": "string",
  "id": "string",
  "date": "string",
  "photos": ["string"],  // Optional: array of photo URLs
  "video": {             // Optional: video object
    "thumb": "string",
    "url": "string",
    "duration": number,
    "views": "string",
    "variants": [        // Array of video quality variants
      {
        "url": "string",
        "contentType": "string",
        "bitrate": number
      }
    ]
  },
  "gif": {               // Optional: GIF object
    "url": "string",
    "thumb": "string"
  }
}
```

#### Examples

**Basic tweet:**
```bash
curl http://localhost:8080/api/jack/status/20
```

**Tweet with media:**
```bash
curl http://localhost:8080/api/mobile_test/status/572593440719912960
```

#### Error Responses

**Invalid tweet ID (400):**
```json
{
  "error": "Invalid tweet ID"
}
```

**Tweet not found (404):**
```json
{
  "error": "Tweet not found"
}
```

Or if the tweet has been deleted:
```json
{
  "error": "This Tweet is unavailable"
}
```
