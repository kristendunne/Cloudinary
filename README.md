# Cloudinary

## Pre-requisites:
- install Python 3.10.1 - https://www.python.org/downloads/
- `pip install Flask`
- `pip install flask-cors`

## Run front-end:
```
py -m http.server
```

## Run back-end:
```
flask run
```

## Summary of steps completed:
1. Successful use of Cloudinary's Upload Widget
    - Replaced cloud name and created a preset
    - Verified successful upload to Cloudinary's Media Library
    - Hosted using a simple http server

2. Displayed image on page
    - Used asset's secure_url to display image
    - Played with image transformations (scale, crop, quality)
    - Used public_id from asset's response to display uploaded image 

3. Created a Flask app with 2 endpoints - stored in memory rather than using a DB
    - Read public_id list
    - Add a new public_id

4. Connected front-end and back-end applications together
    - Added persistence
    - Front-end makes http requests to back-end
