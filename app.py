import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Stop-word removal
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Stemming
    stemmed = [ps.stem(word) for word in tokens]
    
    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    
    return {
        'original': text,
        'tokens': tokens,
        'stemmed': stemmed,
        'lemmatized': lemmatized
    }

# Streamlit app layout
st.title("Text Preprocessing")
st.write("This app cleans the input text by performing tokenization, stopword removal, stemming, and lemmatization.")

# Input for raw text
raw_text = st.text_area("Enter Text", "NLTK is a powerful library for natural language processing.")

if raw_text:
    # Process the text
    cleaned_data = clean_text(raw_text)
    
    # Display results
    st.subheader("Original Text")
    st.write(cleaned_data['original'])
    
    st.subheader("Tokens")
    st.write(cleaned_data['tokens'])
    
    st.subheader("Stemmed Tokens")
    st.write(cleaned_data['stemmed'])
    
    st.subheader("Lemmatized Tokens")
    st.write(cleaned_data['lemmatized'])
