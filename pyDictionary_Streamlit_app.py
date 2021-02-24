from PyDictionary import PyDictionary
import streamlit as st

dictionary = PyDictionary()

st.title('pyDictionary on Streamlit')

user_input = st.text_input(
    label = "Type a word and hit Enter",
    value = '',
    max_chars = None,
    key = None,
    type = "default")

# Translation of pyDictionary is buggy so commented out
# st.sidebar.write('### Spanish Translation:')
# st.sidebar.write(dictionary.translate(user_input, 'es'))

# Get array of all meanings of the word
meanings = dictionary.meaning(user_input)

# pos = part of speech
for pos in meanings.keys():
    st.markdown(f" **_{pos.lower()}_** ") # lowercase, bold, italic
    m = 1
    for meaning in meanings[pos]:
        st.markdown(f"{m}. {meaning}")
        m += 1
    st.write('') # empty line for white space
        
# This line creates 2 equal columns
left_column, right_column = st.beta_columns(2)

# Get array of all synonyms of the word
synonyms = dictionary.synonym(user_input)

# This 'if' condition ensures the Synonym heading doesn't appear when there's no user_input
if bool(user_input) == True:
    left_column.write('### Synonyms')
    
    # loop through the words
    s = 1
    for synonym in synonyms:
        # left_column.write(synonym)
        left_column.markdown(f"{s}. {synonym}")
        s += 1

# Get array of all antonyms of the word
antonyms = dictionary.antonym(user_input)
if bool(user_input) == True:
    right_column.write('### Antonyms')

    # loop through the words
    a = 1
    for antonym in antonyms:
        # right_column.write(antonym)
        right_column.markdown(f"{a}. {antonym}")
        a += 1

st.markdown('---') # This creates a thin divider
st.markdown('This streamlit app is developed by [Daniyal A. Syed](https://www.linkedin.com/in/daniyal-as/).')