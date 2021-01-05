### THIS PROJECT IS A WORK IN PROGRESS!
Please have a look at the project [status of the project](#Status). I would love to have some helping hands contributing to the project.


![Muse](./assets/gh_header.png)
### Music recommendations based on lyrics.
---

Muse is a platform created to serve intelligent music recommendations to it's users based on a target songs lyrics. 

Muse uses a pretrained NLP encoder to perform STS (Semantic Textual Similarity) between the target music and Spotify recommendations to return a refined list of suggestions that exactly match the type of music you just heard.

The recommendations you get are purely based off of the music you chose, unlike other services which look at the activity of bulk users and other metrics based on music genre to craft recommendations for you.

# How things work ?
The project is mainly divided into 3 different parts -
- Django Backend Server serving API endpoints for the frontend
- Scrapy Server running spiders
- Flask API serves the NLP model as JSON API
- NLP Model

## Django 
`musebackendserver/muse`

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

Responds with the cross product of the embeddings for the lyrics sent as input

## Scrapy
`musebackendserver/muse/spiders`

Muse does not use publically available APIs to fetch lyrics of a song because they are way to expensive, a workaround for the same is fetching the lyrics from public domains like Genius and Musixmatch. 

To achieve this the scrapy spiders are hosted using `scrapyd` which are interacted with using JSON endpoints inside the Django project. 

Running spiders instead of using an API is a very takes exponentially more time hence we need to keep checking the status of our spiders, hence that the endpoints provided by `scrapyd` can be polled repeatedly to check the status of the spider.

More information on `scrapyd` [here](https://scrapyd.readthedocs.io/).

## Flask API
`modelserver/`

The flask API holds our NLP model in machine memory so that inference can be performed without extended delay, the API offers endpoint to perform inference on the JSON input data.

## NLP Model

The model used by Muse is [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/4) trained and inferred using Tensorflow 2.0

The model accepts short paragraphs of english text and outputs a 512 dimensional vector, this is the word embedding of each song. The correlation matrix of these embeddings is what gives us the ranks of the recommended songs based on the similarity.

---
# Running locally

## Backend
### Installation
```
# Clone repo
git clone 
cd muse/musebackendserver

# Create and activate virtual environment if not already
mkdir ~/venvs
python -m venvs ~/venvs/<ENV_NAME>
source ~/venvs/<ENV_NAME>/bin/activate

# Install requirements
pip install -r requirements.txt
```
### Running the django, scrapyd, flask servers
```
# Django
cd muse/musebackendserver
python manage.py runserver

# Scrapyd
scrapyd

# Flask
cd muse/modelserver
python api.py
```

## Frontend
### Installation
```
cd muse/muse-frontend
npm install
```

### Running the React app 
```
cd muse/muse-frontend
npm start
```

# Status

## Finish the project
- [x] Django API for storing and fetching data
- [x] Scrapy Spider to scrape lyrics automatically
- [x] Integrating NLP model to the project
- [ ] React Frontend App
- [ ] Adding minimalistic styles to the webpage
- [ ] Writing backend tests

## Future additions
- [ ] Add support for more NLP models to give users a choice to see results from a different perspective
- [ ] Include search parameters provided by Spotify to provide better result filtering
- [ ] Implement load balancing to manage huge number of requests efficiently
