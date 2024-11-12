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
# Download the missing 'punkt_tab' data
nltk.download('punkt_tab') # This line was added to download the required resource

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
    stemmed = [ps.stem(word) for word in tokens]
    
    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    
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

# Input for raw text
raw_text = st.text_area("Enter Text", "")

if raw_text:
    # Process the text
    cleaned_data = clean_text(raw_text)
    
    # Display results
    st.subheader("Original Text")
    st.write(cleaned_data['original'])
    
    st.subheader("Tokens")
    st.write(cleaned_data['tokens'])
    st.subheader("Tokens after Stopword Removal")
    st.write(cleaned_data['tokens_no_stop'])    
    st.subheader("Stemmed Tokens")
    st.write(cleaned_data['stemmed'])
    
    st.subheader("Lemmatized Tokens")
    st.write(cleaned_data['lemmatized'])
