# API Examples

This document shows example responses from the `/api/@name/status/@id/` endpoint.

## Example 1: Basic Text Tweet

**Request:**
```bash
GET /api/jack/status/20
```

**Response:**
```json
{
  "author": {
    "username": "jack",
    "fullname": "Jack Dorsey",
    "id": "12"
  },
  "text": "just setting up my twttr",
  "id": "20",
  "date": "Mar 21, 2006 · 9:50 PM UTC"
}
```

## Example 2: Tweet with Photos

**Request:**
```bash
GET /api/example_user/status/1234567890
```

**Response:**
```json
{
  "author": {
    "username": "example_user",
    "fullname": "Example User",
    "id": "987654321"
  },
  "text": "Check out these photos!",
  "id": "1234567890",
  "date": "Oct 16, 2023 · 4:00 PM UTC",
  "photos": [
    "https://pbs.twimg.com/media/example1.jpg",
    "https://pbs.twimg.com/media/example2.jpg"
  ]
}
```

## Example 3: Tweet with Video

**Request:**
```bash
GET /api/example_user/status/9876543210
```

**Response:**
```json
{
  "author": {
    "username": "example_user",
    "fullname": "Example User",
    "id": "987654321"
  },
  "text": "Watch this video!",
  "id": "9876543210",
  "date": "Oct 16, 2023 · 5:30 PM UTC",
  "video": {
    "thumb": "https://pbs.twimg.com/ext_tw_video_thumb/example/pu/img/thumb.jpg",
    "url": "https://video.twimg.com/ext_tw_video/example/pu/pl/video.m3u8",
    "duration": 15000,
    "views": "1.2M",
    "variants": [
      {
        "url": "https://video.twimg.com/ext_tw_video/example/pu/vid/480x270/video.mp4",
        "contentType": "video/mp4",
        "bitrate": 632000
      },
      {
        "url": "https://video.twimg.com/ext_tw_video/example/pu/vid/640x360/video.mp4",
        "contentType": "video/mp4",
        "bitrate": 832000
      },
      {
        "url": "https://video.twimg.com/ext_tw_video/example/pu/vid/1280x720/video.mp4",
        "contentType": "video/mp4",
        "bitrate": 2176000
      }
    ]
  }
}
```

## Example 4: Tweet with GIF

**Request:**
```bash
GET /api/example_user/status/1111111111
```

**Response:**
```json
{
  "author": {
    "username": "example_user",
    "fullname": "Example User",
    "id": "987654321"
  },
  "text": "Reaction GIF!",
  "id": "1111111111",
  "date": "Oct 16, 2023 · 6:00 PM UTC",
  "gif": {
    "url": "https://video.twimg.com/tweet_video/example.mp4",
    "thumb": "https://pbs.twimg.com/tweet_video_thumb/example.jpg"
  }
}
```

## Error Examples

### Invalid Tweet ID

**Request:**
```bash
GET /api/jack/status/invalid_id
```

**Response (404):**
```json
{
  "error": "Invalid tweet ID"
}
```

### Tweet Not Found

**Request:**
```bash
GET /api/jack/status/99999999999999
```

**Response (404):**
```json
{
  "error": "Tweet not found"
}
```

### Deleted or Unavailable Tweet

**Request:**
```bash
GET /api/jack/status/123456789
```

**Response (404):**
```json
{
  "error": "This Tweet is unavailable"
}
```
