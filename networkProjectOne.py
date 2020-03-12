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

		elif (word == "don't" and wordList[ind + 2] == "and"):
			global notLikeList
			notLikeList.append(wordList[ind + 2])
			notLikeList.append(wordList[ind + 4])
		elif (word == "don't" ):
			notLikeList.append(wordList[ind + 2])


stringWord = "I like pie and muffins. I don't like corona for breakfast. I like coffee for breakfast and I don't like milk. I like chicken for dinner. I don't like turkey for breakfast. I also like juice box."

data = stringWord.split()  # split string into a list

getword(data)  # this function takes in the list and searches for key words
#this is the last pushhhhh

biglist = notLikeList + likeList
data = {}

#assign values to all the key words obtained
for d in biglist:
	if d=='corona':
		data['corona']=2
	elif d=='milk.':
		data['milk.']=2.1
	elif d=='turkey':
		data['turkey']=2.8
	elif d=='pie':
		data['pie']=1
	elif d=='muffins.':
		data['muffins.']=1.2
	elif d=='coffee':
		data['coffee']=2.3
	elif d=='chicken':
		data['chicken']=3
	elif d=='juice':
		data['juice']=2.2
	else:
		continue


print((notLikeList))
print((likeList))


print((data))

