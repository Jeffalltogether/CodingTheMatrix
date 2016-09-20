def andSearch(inverseIndex, query):
	#define empty set for results
	docWithWord = set()
	tempList = []
	tempSet = set()
	
	#iterate thrugh search terme
	for i in range(len(query)):

		# if a match is found
		if query[i] in inverseIndex:
			tempList.append([query[i],inverseIndex[query[i]]])
			for keyList,valueList in tempList:
				if len(tempSet) == 0:
					tempSet = set(valueList)
				docWithWord = set(valueList) & set(tempSet)

		#if no match is found
		else: 
			docWithWord = set()
			break

	return docWithWord