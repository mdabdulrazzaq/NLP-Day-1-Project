import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize tools
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Stop-word removal
    tokens_no_stop = [word for word in tokens if word.lower() not in stop_words]
    
    # Stemming
    stemmed = [ps.stem(word) for word in tokens_no_stop]
    
    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens_no_stop]
    
    return {
        'original': text,
        'tokens': tokens,
        'tokens_no_stop': tokens_no_stop,
        'stemmed': stemmed,
        'lemmatized': lemmatized
    }

# Streamlit app layout
st.title("Text Preprocessing")

st.write("""
    This app demonstrates the following text preprocessing techniques:
    - **Tokenization**: Splitting text into individual words.
    - **Stopword Removal**: Removing common words like 'the', 'is', etc.
    - **Stemming**: Reducing words to their root form.
    - **Lemmatization**: Converting words to their base form considering context.
""")

# Default text
default_text = "NLTK is a powerful library for natural language processing."

# Input for raw text
raw_text = st.text_area("Enter Text (or use the default)", default_text)

if raw_text:
    # Process the text
    cleaned_data = clean_text(raw_text)
    
    # Display Results
    st.subheader("Original Text")
    st.write(cleaned_data['original'])
    
    st.subheader("Tokens (Word Splitting)")
    st.write(f"Tokenized text: {cleaned_data['tokens']}")
    
    st.subheader("Tokens after Stopword Removal")
    st.write(f"Text after removing common stopwords: {cleaned_data['tokens_no_stop']}")
    
    st.subheader("Stemmed Tokens")
    st.write(f"Stemming result: {cleaned_data['stemmed']}")
    
    st.subheader("Lemmatized Tokens")
    st.write(f"Lemmatization result: {cleaned_data['lemmatized']}")
    
# Optionally, include a button for the user to reset the input
if st.button("Reset"):
    st.text_area("Enter Text (or use the default)", "")
