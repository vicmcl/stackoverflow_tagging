from stackapi import StackAPI
from datetime import datetime
from pprint import pprint
import json

SITE = StackAPI('stackoverflow')

questions = SITE.fetch(
    'questions',
    fromdate=datetime(2022, 1, 1),
    todate=datetime.today(),
    min=50,
    tagged='python',
    sort='votes'
)

items = dict()

for question_data in questions["items"][-50:]:
    items[question_data["question_id"]] = dict()
    items[question_data["question_id"]]["sentence"] = question_data["title"]
    items[question_data["question_id"]]["tags"] = question_data["tags"]

with open("data/questions.json", "w") as f:
    json.dump(items, f)