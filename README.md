# NLP Day 1: Text Preprocessing

## Introduction
Text preprocessing is a crucial step in any Natural Language Processing (NLP) project. It involves cleaning and preparing text data for analysis. The main steps include tokenization, stop-word removal, stemming, and lemmatization. In this project, we will go through these preprocessing steps.

### Project Contents
- **Jupyter Notebook (`day1_text_preprocessing.ipynb`)**: A notebook that demonstrates various text preprocessing techniques.
- **Streamlit App (`app.py`)**: An interactive app where you can input text and see the preprocessing in action.

## Concepts Covered
### 1. Tokenization
Tokenization is the process of splitting text into individual words or tokens. It helps in analyzing words separately.

- **Example**: 
  - Input: `"Natural Language Processing is fun!"`
  - Output: `['Natural', 'Language', 'Processing', 'is', 'fun', '!']`

### 2. Stop-word Removal
Stop words are common words like "is", "the", "in" that do not add much meaning to the text. Removing these words helps reduce noise in the data.

- **Example**:
  - Input: `['Natural', 'Language', 'Processing', 'is', 'fun', '!']`
  - Output: `['Natural', 'Language', 'Processing', 'fun', '!']`

### 3. Stemming
Stemming reduces words to their root form. It helps in grouping similar words together. For example, "running" and "runs" are both reduced to "run".

- **Example**:
  - Input: `['Processing', 'Processed', 'Processor']`
  - Output: `['process', 'process', 'process']`

### 4. Lemmatization
Lemmatization also reduces words to their base form but uses linguistic rules to find the proper "lemma" of a word. It considers the context of the word.

- **Example**:
  - Input: `['better', 'running']`
  - Output: `['good', 'run']`

## How to Run
### Jupyter Notebook
1. Open `day1_text_preprocessing.ipynb` in Jupyter Notebook or any other compatible editor.
2. Run the cells to see the output of each text preprocessing step.

## **Streamlit app link**:
  - **Link**: [NLP Day 1: Text Preprocessing - Streamlit App](https://nlp-day-1-textprepper.streamlit.app/)

