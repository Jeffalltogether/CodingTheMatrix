def makeInverseIndex(strlist):
	# load the file
	source = open(strlist)

	#convert to list of strings
	documents = list(source)

	#generate document numbers
	docNum = [num for num,string in enumerate(documents)]

	#generate word list for each document
	docWords = [string.split() for string in documents]

	#generate list of [[docNum,docWords]]
	numWords = zip(docNum, docWords)

	#generate set of unique words from all documents to search through
	words = {word for string in docWords for word in string}

	#search each word in the word list for match in the dictionary
	inverseIndex = {}
	
	for searchTerm in words:
		#make an empty set where we store matches
	    searchPosition = set()
	    for docNum,docWords in numWords:
	        for word in docWords:
	        	#match search term to word in document
	            if searchTerm == word: 
	                #update the set storing matches
	                searchPosition.add(docNum)
	    #update the inverse index, also conver the set to a list
	    inverseIndex.update({searchTerm:list(searchPosition)})

	return inverseIndex