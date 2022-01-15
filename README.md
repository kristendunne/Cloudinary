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
1. Got upload widget to work (default)
    - Replaced cloud name and created preset
    - Verified this uploaded to dashboard in Cloudinary
    - Hosted using simple http server

2. Displayed image on page
    - Used secure_URL to display image
    - Played with transformations (scale, crop, quality) to image
    - Used public_ID from response to use whichever image was uploaded 

3. Created flask app with 2 endpoints - in memory rather than using DB
    - Read public_id list
    - Add new public_id

4. Connected front-end and back-end app together
    - Added persistence - each time we update list, additional items are added and prior remain
   - New items are added to back-end (where front-end is pulling from and displaying in console,
  then as images on page)
