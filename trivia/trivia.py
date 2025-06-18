import requests
from translate import Translator
import json
import os
import time

translator = Translator(to_lang="tr")

while True:
	os.system("cls")
	print("""=======
TRİVİA
=======
""")
	trivia_url = "https://opentdb.com/api.php?amount=1&category=17&difficulty=easy&type=boolean"
	triviaRead = requests.get(trivia_url)
	jsonDATA = json.loads(triviaRead.text)
	
	print(translator.translate(jsonDATA["results"][0]["question"]))
	dy = input("D/Y: ")
	
	if dy.lower() == "d": dy = "True"
	else: dy = "False"

	if dy == jsonDATA["results"][0]["correct_answer"]: print("\ndoğru!")
	else: print("\nyanlış!")

	time.sleep(2)