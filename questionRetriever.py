import requests
import json
import random
import html
import time

class retriever:
    token = ""

    def __init__(self):
        response = json.loads((requests.get("https://opentdb.com/api_token.php?command=request")).content.decode())
        self.token = response["token"]
        #print(f"Token: {self.token}")
    
    def getScienceAndNat(self, num = 1):
        response = json.loads((requests.get(f"https://opentdb.com/api.php?amount={num}&category=17&token={self.token}")).content.decode())
        return self.parseResponseToQuestions(response)
    
    def getScienceComputers(self, num = 1):
        response = json.loads((requests.get(f"https://opentdb.com/api.php?amount={num}&category=18&token={self.token}")).content.decode())
        return self.parseResponseToQuestions(response)
    
    def getMath(self, num = 1):
        response = json.loads((requests.get(f"https://opentdb.com/api.php?amount={num}&category=19&token={self.token}")).content.decode())
        return self.parseResponseToQuestions(response)
    
    def getSingleRandom(self):
        response = json.loads((requests.get(f"https://opentdb.com/api.php?amount=1&category={random.randrange(17, 20)}&token={self.token}")).content.decode())
        return self.parseResponseToQuestions(response)

    def parseResponseToQuestions(self, response):
        if response["response_code"] == 5:
            return [["Woaw woaw woaw slow down! Enter 'c' to continue.", "c"]]
        qns = []
        for x in response["results"]:
            qns.append([html.unescape(x["question"]).strip(), html.unescape(x["correct_answer"]).strip()])
        return qns

def testQuizMode(sleepTime = 5):
    a = retriever()
    print("-----Rapid (databased) Flamethrower-----\nType 'q' to quit anytime!\n")
    while True:
        qData = a.getSingleRandom()
        print(f"Question: {qData[0][0]}")
        inp = input(f"Enter answer (note: answer will only be evaluated after {sleepTime}s to prevent overload): ")
        if inp == "q":
            break
        if inp.lower() == qData[0][1].lower():
            print("Correct!!")
        else:
            print(f"Wrong :(. Answer is {qData[0][1]}")
        print()
        time.sleep(sleepTime)

testQuizMode(0)
