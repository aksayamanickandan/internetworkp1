likeList = []
notLikeList = []


def getword(wordList):
    for ind, word in enumerate(wordList):
        if (wordList[ind - 1] != "don't" and word == "like" and wordList[ind + 2] == "and"):
            global likeList
            likeList.append(wordList[ind + 1])
            likeList.append(wordList[ind + 3])
        elif (wordList[ind - 1] != "don't" and word == "like"):
            likeList.append(wordList[ind + 1])

        elif (word == "don't" ):
            global notLikeList
            notLikeList.append(wordList[ind + 2])


stringWord = "I like pie and I like muffins. I don't like corona for breakfast. I like coffee for breakfast and I don't like milk. I like chicken for dinner. I don't like turkey for breakfast."  # this is our input

data = stringWord.split()  # split string into a list

getword(data)  # this function takes in the list and searches for key words

print((notLikeList))
print((likeList))
