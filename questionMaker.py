from meta_ai_api import MetaAI

class bio:
    #Main
    BIO = "biology"
    #Specifics
    ANAT = "anatomy"
    PHYSIO = "physiology"
    EVO = "evolution"

class phy:
    #Main
    PHY = "physics"
    #Specifics
    PARTICLE = "particle physics"
    DYNAMICS = "kinematics and dynamics"

class chem:
    #Main
    CHEM = "chemistry"
    #Specifics
    OCHEM = "organic chemistry"
    PCHEM = "physical chemistry" 
    OBSCURE_REACT = "obscure chemical reactions"

class math:
    #Main
    MATH = "mathematics"
    #Specifics
    TOPO = "topology"
    GRAPH = "graph theory"

class cs:
    #Main
    CS = "computer science"
    #Specifics
    DATA_ALGO = "data structures and algorithms"
    AI_ML = "artificial intelligence and machine learning"

class general:
    SCIENTIST = "scientists and their discoveries"
    
def generatePrompt(subject):
    return f"Generate a single question, without any headers (only the question) on {subject} trivia, where the player has to fill in the blank.\
    Add in the answer after inserting 2 new lines and prepend the answer with @\
    Please also give more varied questions"

def getQuestionAndAnswer(subject):
    ai = MetaAI()
    response = (ai.prompt(message = generatePrompt(subject)))
    response = response["message"]
    return response[0 : response.find("@")].strip(), response[response.find("@") + 1 : len(response)].strip()

print("-----Rapid Flamethrower-----\n\n")

while True:
    question, answer = getQuestionAndAnswer(cs.CS) #Change this to get different types of questions
    print(f"Question: {question}")
    inp = input("Enter answer (or q to quit): ")
    if inp == "q":
        break
    if inp.lower() == answer.lower():
        print("Correct!!")
    else:
        print(f"Wrong :(. Answer is {answer}")
    print()
