# like-app

## objective

this tg bot api is used to like and dislike photos

## bot requirements

- [x] add a new photo
- [x] send a photo to channel
- [x] count likes and dislikes
- [x] send the most popular photo to channel
- [x] send the least popular photo to channel

## database requirements

- [x] store photos with likes and dislikes
- [x] get the most popular photo
- [x] get the least popular photo
- [x] one user can like or dislike a photo only once

### database structure

```json
{
    "images": {
        "1": {
            "photo_id": "photo_id",
            "likes": [
                "user_id",
                "user_id",
                "user_id"
            ],
            "dislikes": [
                "user_id",
                "user_id",
                "user_id"
            ]
        }
    }
}
```

### database methods

- [x] add a new photo
- [x] get a photo
- [x] get the most popular photo
- [x] get the least popular photo
- [x] like a photo
- [x] dislike a photo

