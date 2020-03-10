likeList=[]
notLikeList=[]
def getword(wordList):

    for ind ,word in enumerate(wordList):
        if (word == "like"):
            global likeList
            likeList.append(wordList[ind+1])
        elif(word=="don't" ):
            global notLikeList
            notLikeList=wordList[ind+2]





stringWord = "we like apple. We don't like water"

data = stringWord.split()  # split string into a list

getword(data)

print(likeList)
print(notLikeList)
