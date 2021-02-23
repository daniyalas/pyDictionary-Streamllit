import numpy as np
import pandas as pd
import streamlit as st

from PyDictionary import PyDictionary
dictionary = PyDictionary()

user_input = st.text_input(
    label = "Type your word in the box below",
    value = '',
    max_chars = None,
    key = None,
    type = "default")

st.sidebar.write('Urdu Translation: ' + dictionary.translate(user_input, 'ur'))

'Meanings'
st.write(dictionary.meaning(user_input))

'Synonyms'
st.write(dictionary.synonym(user_input))

'Antonyms'
st.write(dictionary.antonym(user_input))