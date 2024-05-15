#Importing libraries 
import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
import pickle

csv_file = "Apple_reviews.csv"

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

def preprocess_sentence(sentence):
    # Parse the sentence using spaCy
    doc = nlp(sentence)
    
    # Lemmatization, removing stop words, punctuation, and non-alphanumeric tokens
    words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    
    # Join the words back into a sentence
    preprocessed_sentence = ' '.join(words)
    
    return preprocessed_sentence

def process_csv_file(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Drop rows with missing values in the "Reviews" column
    df = df.dropna(subset=["Reviews"])
    
    # Combine all reviews into a single string
    all_reviews = " ".join(df["Reviews"])
    
    # Split the combined reviews into individual sentences
    sentences = sent_tokenize(all_reviews)
    
    # Preprocess each sentence
    preprocessed_sentences = [preprocess_sentence(sentence) for sentence in sentences]
    
    return preprocessed_sentences

preprocessed_sentences = process_csv_file(csv_file)

# Define your own list of additional stopwords
additional_stopwords = ['phone', 'apple', 'iphone']

# Get the default English stopwords from NLTK
default_stopwords = set(stopwords.words('english'))

# Combine default English stopwords with additional stopwords
stopwords = list(default_stopwords) + additional_stopwords

# Vectorize the sentences using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000, min_df=5, max_df=0.95,stop_words = stopwords)
tfidf_matrix = vectorizer.fit_transform(preprocessed_sentences)

# Apply NMF
num_topics = 10  # Number of topics
nmf_model = NMF(n_components=num_topics, random_state=42)
nmf_model.fit(tfidf_matrix)


#pickle.dump(nmf_model, open("Apple_model.pkl", "wb"))
# Save the NMF model and the vectorizer
with open("Apple_model.pkl", "wb") as model_file:
    pickle.dump(nmf_model, model_file)

with open("Apple_vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

# Save the TF-IDF matrix to a file using pickle
with open("Apple_tfidf_matrix.pkl", "wb") as f:
    pickle.dump(tfidf_matrix, f)

# Save the preprocessed sentences to a file using pickle
with open("Apple_preprocessed_sentences.pkl", "wb") as f:
    pickle.dump(preprocessed_sentences, f)