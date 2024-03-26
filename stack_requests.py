from stackapi import StackAPI
from datetime import datetime
import json
from pprint import pprint

SITE = StackAPI('stackoverflow')

SITE.page_size = 100
SITE.max_pages = 10

response = SITE.fetch(
    'questions',
    fromdate=datetime(2010, 1, 1),
    todate=datetime.today(),
    min=50,
    tagged='python',
    sort='votes',
)

questions = dict()

for question_data in response['items']:
    questions[question_data["question_id"]] = dict()
    questions[question_data["question_id"]]["sentence"] = question_data["title"]
    questions[question_data["question_id"]]["tags"] = question_data["tags"]

with open("data/api_response.json", "w") as f:
    json.dump(questions, f)
    