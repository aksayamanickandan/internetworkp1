likeList=[]
notLikeList=[]
def getword(wordList):
    global likeList
    global notLikeList
    for ind ,word in enumerate(wordList):
        if (word == "like"):
            likeList.append(wordList[ind+1])
    print(likeList)



stringWord = "we like apple. We don't like water"

data = stringWord.split()  # split string into a list

getword(likeList)
