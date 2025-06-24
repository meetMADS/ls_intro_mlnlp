import math
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = [
    'the sun is a star',
    'the moon is a satellite',
    'the sun and moon are celestial bodies'
]

token_doc = []
for sentence in corpus:
    words = sentence.lower().split()
    token_doc.append(words)

vocabulary = []
for doc in token_doc:
    for word in doc:
        if word not in vocabulary:
            vocabulary.append(word)

tf_list = []
for doc in token_doc:
    tf = {}
    total_len = len(doc)
    for word in vocabulary:
        count = doc.count(word)
        tf[word] = count / total_len
    tf_list.append(tf)

df = {}
for word in vocabulary:
    count = 0
    for doc in token_doc:
        if word in doc:
            count += 1
    df[word] = count

#idf calculation
N = len(corpus)
idf = {}
for word in vocabulary:
    idf[word] = math.log(N / df[word])

#TF-IDF = TF*IDF
manual_count = []
for tf in tf_list:
    tfidf = {}
    for word in vocabulary:
        tfidf[word] = tf[word] * idf[word]
    manual_count.append(tfidf)
print("\n")
print("Manual")
for i, tfidf in enumerate(manual_count):
    print(f"Document {i+1}")
    for word in vocabulary:
        print(f"{word}: {tfidf[word]}")
print("\n")
print("CountVectorizer")
vectorizer = CountVectorizer()
X_count = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names_out()
matrix = X_count.toarray()
for i in range(len(corpus)):
    print(f"Document {i+1}")
    for j in range(len(words)):
        print(f"{words[j]}: {matrix[i][j]}")
print("\n")
print("TfidfVectorizer")
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(corpus)
words = tfidf_vectorizer.get_feature_names_out()
matrix = X_tfidf.toarray()
for i in range(len(corpus)):
    print(f"Document {i+1}")
    for j in range(len(words)):
        print(f"{words[j]}: {matrix[i][j]}")
