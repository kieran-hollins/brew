# brew
This project is intended to be used for a university DevOps project. This will demonstrate continous integration with a cloud platform. 

## What is the App?
This app lets people show off their favourite coffees and get pretentious without judgement (because I didn't have time to add comments!)

## Debugging locally
Use venv to manage python and dependancy version control.
Use the following comands:
```python
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt

# You can then use this command to run a debug environment locally
$ python3 -m flask --app brew run --port 8080 --debug
```
