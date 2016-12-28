# trashr
Twitter Trash reminder reply bot. Really weird corner-case bot that only
replies to a specific tweet with a randomly selected string from a list. It's
just an experiment to see how long it takes people to realize it's a bot talking
to a bot.

To use:
Edit either update the lines matching
```
CONSUMER_KEY = config.consumerkey
CONSUMER_SECRET = config.consumersecret
ACCESS_KEY = config.accesskey
ACCESS_SECRET = config.accesssecret
```

or edit config.py and set the following variables to match your Twitter API info.

Then launch using the command `nohup ./trashr.py &`

Outstanding items:
* Allow users to either specify credentials via CLI arguments or a config file
* Add a daemon mode so you don't have to launch via nohup
* Allow user to specify filter to use via CLI arguments
* Change responses to be read from a config file
* Reimport responses if the response file changes
