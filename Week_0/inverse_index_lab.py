# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Task 1) Movie Review
## Task 1
def movie_review(name):
    Rev = ["See it!", "A gem!", "Ideological claptrap!"]
    return print("Suggestions: %s" % Rev[randint(0,2)])



## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
        #open document and generate a list of stories
    #f = open(strlist)
    mylines = strlist
    
    # convert list of stories into list of list of words
    mywords=[]
    for i in range(len(mylines)):
        mywords.append(mylines[i].split())

    # organize list of words into a new list with the format [docuemnt#: [words]]
    docwords = []
    for count, elem in enumerate(mywords):
        docwords.append([count, elem])

    # extract all the unique words from the text file
    allwords = {item for sublist in mywords for item in sublist}

    # search each word in the document
    invIndex = {}
    for word in allwords:
        wordset = set()
        # match the word with the text of each story
        for storynumber,storytext in docwords:
            for i in storytext:
                # if there is a match, append the story # from where it matched to a set
                if i == word:
                    wordset.add(storynumber)
        # create a dictionary of the document words and the story number from where they are located
        invIndex.update({word:wordset})
    
    # return the newly generated list
    return invIndex



## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    pass



## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    pass

