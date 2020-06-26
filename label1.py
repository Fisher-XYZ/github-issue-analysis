

    
from sklearn.feature_extraction.text import TfidfVectorizer

handle=open('labeltask.csv')

next(handle)
allcom=list()
for line in handle:
    words= line.split(',')
    commentbody=words[5]
    allcom.append(commentbody)


tfidf2 = TfidfVectorizer()
re = tfidf2.fit_transform(allcom)
print(re)



    


