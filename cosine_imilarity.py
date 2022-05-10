from sklearn.feature_extraction.text import CountVectorizer
text=["London Paris London","Paris Paris London"]
cv=countVectorizer()
count_matrix = cv.fit_transform(text)
print count_matrix.toarray()
