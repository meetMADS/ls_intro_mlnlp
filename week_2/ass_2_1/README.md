##Findings

**Manual**
**Document 1**
the: 0.0, sun: 0.0811, is: 0.0811, a: 0.0811, star: 0.2197
moon, satellite, and, are, celestial, bodies: 0.0

**Document 2**
the: 0.0, moon: 0.0811, is: 0.0811, a: 0.0811, satellite: 0.2197
sun, star, and, are, celestial, bodies: 0.0

**Document 3**
sun, moon: 0.0579; and, are, celestial, bodies: 0.1569
the, is, a, star, satellite: 0.0

**CountVectorizer**
**Document 1**
and: 0
are: 0
bodies: 0
celestial: 0
is: 1
moon: 0
satellite: 0
star: 1
sun: 1
the: 1
**Document 2**
and: 0
are: 0
bodies: 0
celestial: 0
is: 1
moon: 1
satellite: 1
star: 0
sun: 0
the: 1
**Document 3**
and: 1
are: 1
bodies: 1
celestial: 1
is: 0
moon: 1
satellite: 0
star: 0
sun: 1
the: 1


**TfidfVectorizer**
**Document 1**
and: 0.0
are: 0.0
bodies: 0.0
celestial: 0.0
is: 0.4804583972923858
moon: 0.0
satellite: 0.0
star: 0.6317450542765208
sun: 0.4804583972923858
the: 0.3731188059313277
**Document 2**
and: 0.0
are: 0.0
bodies: 0.0
celestial: 0.0
is: 0.4804583972923858
moon: 0.4804583972923858
satellite: 0.6317450542765208
star: 0.0
sun: 0.0
the: 0.3731188059313277
**Document 3**
and: 0.42618350336974425
are: 0.42618350336974425
bodies: 0.42618350336974425
celestial: 0.42618350336974425
is: 0.0
moon: 0.3241235393856436
satellite: 0.0
star: 0.0
sun: 0.3241235393856436
the: 0.2517108425440014

*Findings*
Manual TF-IDF:
Some words like star and satellite got higher scores because they appeared in only one document. Common words like the got a score of 0 because they were present in all documents.

CountVectorizer:
Just counted how many times each word appeared. That's why the gets a score.

TfidfVectorizer:
Gave higher scores to words that were important and unique, like star and satellite. Common words like the and is got lower scores.