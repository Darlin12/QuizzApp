import json

import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}
question_data = requests.get('https://opentdb.com/api.php', params=parameters)
questions = question_data.json()['results']









