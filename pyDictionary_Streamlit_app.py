import numpy as np
import pandas as pd
import streamlit as st

from PyDictionary import PyDictionary
dictionary = PyDictionary()

st.title('pyDictionary on Streamlit')

user_input = st.text_input(
    label = "Type a word and hit Enter",
    value = '',
    max_chars = None,
    key = None,
    type = "default")

# Translation is very buggy for some reason
# st.sidebar.write('### Urdu Translation:')
# st.sidebar.write(dictionary.translate(user_input, 'es'))

meanings = dictionary.meaning(user_input)

# pos = part of speech
for pos in meanings.keys():
    st.markdown(f"*{pos.lower()}*")
    m = 1
    for meaning in meanings[pos]:
        st.write(m, '. ' , meaning)
        m += 1
    st.write('')
        

left_column, right_column = st.beta_columns(2)

synonyms = dictionary.synonym(user_input)
if bool(user_input) == True:
    left_column.write('### Synonyms')
    
    # loop through the words
    s = 1
    for synonym in synonyms:
        # left_column.write(synonym)
        left_column.markdown(f"{s}. {synonym}")
        s += 1

antonyms = dictionary.antonym(user_input)
if bool(user_input) == True:
    right_column.write('### Antonyms')

    # loop through the words
    a = 1
    for antonym in antonyms:
        right_column.markdown(f"{a}. {antonym}")
        a += 1
