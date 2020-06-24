from Guide import Guide
from DB import DB
from Query import Query

print('Bot: wellcome to Guide me')
print('Lets start and build your own computer.')


gameDB = DB("query_list.csv")
gameGuide = Guide("steps_level1.txt", port=65432,gameDB=gameDB)

def firstElment(elment):
    return elment[0]

def getSimilarQuery(clientHelpReq):
    countList = []
    for query in gameDB.queries:
        wordCount = 0
        for word in clientHelpReq.split():
            if word in query.question:
                wordCount=+1
        countList.append((wordCount, query))
    countList.sort(key=firstElment, reverse=True)
    return countList[0][1]


while gameGuide.showNextStep():
    helpMe = gameGuide.showDoneOrHelp()
    #while helpMe:
    if helpMe:
        clientHelpReq = gameGuide.showGetHelp()

        query = getSimilarQuery(clientHelpReq)

        rightQ = gameGuide.isQuestionCorrect(query)
        if rightQ:
            rightA = gameGuide.isAnsCorrect(query)
            if not rightA:
                print('waiting for expert to answer....')
                gameGuide.goToExpert(clientHelpReq, query)
        else:
            print('waiting for expert to answer....')
            gameGuide.goToExpert(clientHelpReq)

gameGuide.sock.close()