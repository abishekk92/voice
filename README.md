voice
=====

__Installation__

Clone the repo:
```bash
    git clone git@github.com:abishekk92/voice.git 
```
Install the dependencies:
```bash
    pip install -r requirements.txt
```

- You will need Redis and MongoDB for the app to work properly. Please install them.

- For greater simplicity in making calls, Plivo Cloud has been used you can get a [free developer account](http://plivo.com/)

- Rename app.config.sample into app.config and use your auth_id and token

```bash
    python app.py
```
The app should be up and running, please feel free to open a issue if something is not working.
