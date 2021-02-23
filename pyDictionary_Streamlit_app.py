import numpy as np
import pandas as pd
import streamlit as st

from PyDictionary import PyDictionary
dictionary=PyDictionary()

word = ''
user_input = st.text_input(
    label = "Type your word in the box below",
    value = word,
    max_chars = None,
    key = None,
    type = "default")

# word = "indentation"
st.write(dictionary.meaning(user_input))