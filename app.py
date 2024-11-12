
import streamlit as st
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

spacy.load('en_core_web_sm')

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize tools
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")

# Streamlit UI
st.title("Text Preprocessing Demo")
user_input = st.text_area("Enter your text:", "Natural Language Processing is an exciting field. It's full of challenges!")

if st.button("Process Text"):
    tokens = word_tokenize(user_input)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    stemmed_tokens = [ps.stem(word) for word in filtered_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    st.subheader("Tokenized Text")
    st.write(tokens)

    st.subheader("Filtered Text (No Stopwords)")
    st.write(filtered_tokens)

    st.subheader("Stemmed Text")
    st.write(stemmed_tokens)

    st.subheader("Lemmatized Text")
    st.write(lemmatized_tokens)

    st.subheader("Named Entities (NER)")
    doc = nlp(user_input)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    st.write(entities)
