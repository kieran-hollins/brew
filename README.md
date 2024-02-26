# brew
This project is intended to be used for a university DevOps project. This will demonstrate continous integration with a cloud platform.

## What is the App?
This app is for guiding users through finding their ideal coffee and allowing them to store results about new beans that they try.

## Debugging locally
Use venv to manage python and dependancy version control.
Use the following comands:
```python
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install Flask
$ python3 -m pip install click
$ python3 -m pip install python-dotenv

# You can then use this command to run a debug environment locally
$ python3 -m flask --app brew run --port 8080 --debug
```
