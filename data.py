import requests
import html

quiz_api = requests.get("https://opentdb.com/api.php?amount=10&category=9&type=boolean")

quiz_data = quiz_api.json()
quiz_list = quiz_data['results']
for question in quiz_list:
    question['question'] = html.unescape(question['question'])

question_data = quiz_list

