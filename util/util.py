from bs4 import BeautifulSoup
import re, os


import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

from nltk.tokenize import word_tokenize
lemmatizer = nltk.stem.WordNetLemmatizer()

from sklearn.feature_extraction.text import TfidfVectorizer


def removeTags(text):
    """
    input: string that contains html tags
    output: string without html tags

    """
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()

    return text


# removeTags('<h1>this is a test</h1>')


def cleanText(text):
    """
    input: string with special characters, double spaces, single characters
    output: clean string
    """

    text = re.sub('\[[^]]*\]', ' ', text)  # removes special chars
    text = re.sub('[^a-zA-Z]', ' ', text)  # removes no lower or capital chars
    text = re.sub('\s+[a-zA-Z]\s+', ' ', text)  # removes single chars
    text = re.sub('\s+', ' ', text)  # removes double spaces
    text = text.strip().lower()  # makes all the text lower

    return text


# cleanText(' /$^_)(*&^%$#@!% THIS: is, a Test/ ')


def removeStopwords(text):
    """
    input: string that contains english stop words
    output: string without english stop words

    """

    text = " ".join([t for t in text.split() if t not in stop_words])
    return text


# removeStopwords("for me i don't care if you do is it true or not did he do it has he done it")
# removeStopwords("this is a test")


def removeString(full_text, filter_string):
    text = full_text.replace(filter_string, '')
    return text


# removeString('tajisawesome is', ' is')

def selectiveRemove(text ,l='abcdefghijklmnopqrstuvwxyz', n='1234567890',letters=True, numbers=True, s='' ):
    keep = ''
    final = text
    if letters is True:
        keep +=l
    if numbers is True:
        keep+=n
    keep+=s
    for i in text:
        if i not in keep:
            final = final.replace(str(i), "")
    return final

# selectiveRemove('<taj>',s='@.')

def textStemming(text):
    """ Stemming """

    word_tokens = word_tokenize(text)
    stemmed_text = " ".join([ps.stem(word) for word in word_tokens])
    return stemmed_text


# textStemming('im looking for some fun, why are you laughing at me, watching')


def textLemmatization(text):
    """ Lemmatization """

    word_tokens = word_tokenize(text)
    lemmatized_text = " ".join(lemmatizer.lemmatize(token) for token in word_tokens if token not in stop_words)
    return lemmatized_text

	
def list_directories(path):
    """list files and directories in a given path"""
    arr = os.listdir(path)
    return arr
	
	

# text = textStemming('im looking for some fun, why are you laughing at me, watching')
# textLemmatization(text)



# text ='<b>hi there fellow comrade</b>, i wish you a happy birthday mate, stop runining around and looking for that box please, i have it :D$$#@#$@#%@%#$%$@#$@#%    1232131231 '
# text = removeTags(text)
# text = cleanText(text)
# text = removeStopwords(text)
# text = textStemming(text)
# text = textLemmatization(text)
# print(text)

# tfidf_vec = TfidfVectorizer()
# review_tfidf_vec = tfidf_vec.fit_transform([text])
# review_tfidf_vec.toarray()
