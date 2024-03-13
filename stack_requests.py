from stackapi import StackAPI
from datetime import datetime
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

items = questions["items"][-50:]

with open("questions.json", "w") as f:
    json.dump(items, f)