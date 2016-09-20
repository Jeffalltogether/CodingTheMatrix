def orSearch(inverseIndex, query):
    #define empty set for results
    docWithWord = set()
    
    #iterate thrugh search terme
    for searchTerm in query:
        #update results set with values of inverseIndex for key equal to search term
        if searchTerm in inverseIndex:
            docWithWord.update(inverseIndex[searchTerm]) 

    return docWithWord