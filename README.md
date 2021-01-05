![Muse](./assets/gh_header.png)
### Music recommendations based on lyrics.
---

Muse is a platform created to serve intelligent music recommendations to it's users based on a target songs lyrics. 

Muse uses a pretrained NLP encoder to perform STS (Semantic Textual Similarity) between the target music and Spotify recommendations to return a refined list of suggestions that exactly match the type of music you just heard.

The recommendations you get are purely based off of the music you chose, unlike other services which look at the activity of bulk users and other metrics based on music genre to craft recommendations for you.

# How things work ?
The project is mainly divided into 3 different parts -
- Django Backend Server serving API endpoints for the frontend
- Scrapyd Server running spiders
- Flask API serves the NLP model as JSON API

## Django 
The Django model is pretty straightforward, it is currently used to serve the API for the whole project. 

The current available API endpoints are -

```
/api/v1/sp_recommedations - POST
{
    "song": "cheapskate",
    "artist": "oliver tree"
}
```
Responds with Spotify recommendations for a particular song.

The recommendations fetched are saved in the Django Model named `SongQueryObject` which will be used later in many instances to fetch the status of the User Query.


```
/api/v1/start_fetch - POST
{
    "query_id": "1"
}
```
The  `query_id` parameter corresponds to the `PK` from the model `SongQueryObject`, this essentially stores the list of songs fetched from the SPotify API earlier and schedules a Scrapy Spider Job to scrape the lyrics of the songs.

Responds with the status of Scrapy spider job that was scheduled for the User's query.


```
/api/v1/show_lyrics - POST
{
    "query_id": "1"
}
```
The  `query_id` parameter corresponds to the `PK` from the model `SongQueryObject`

Responds with the lyrics for the `query_id`, i.e. the lyrics for every song fetched from the Spotify API


```
/api/v1/get_embeddings - POST
{
    "type": "full",
    "songs": [
        {"1": "ok boomer is the song lyric"}
    ],
    "model": "use"
}
```
```
/api/v1/get_embeddings - POST
{
    "type": "partial",
    "songs": [
        "1", "2", "3"
    ],
    "model": "use"
}
```
`type`  - The type of query either `full` (with song IDs and lyrics) or `partial` (with only song IDs)

`songs` - Array of Song IDs **OR** Song IDs with lyrics 

`model` - The model used to compute similarity, only available - `use`

