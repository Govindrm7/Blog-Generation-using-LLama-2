import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers  
import os

# Function to get response from LLAMA 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    model_path = 'models/llama-2-7b-chat.ggmlv3.q8_0.bin'

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}. Please ensure it exists.")

    llm = CTransformers(
        model_file=model_path,
        model_type='llama',
        config={
            'max_new_tokens': 256,
            'temperature': 0.01
        }
    )

    template = """
        Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    response = llm(prompt.format(
        blog_style=blog_style,
        input_text=input_text,
        no_words=no_words
    ))
    return response


# Streamlit UI
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input('Number of words')
with col2:
    blog_style = st.selectbox('Blog Target Audience', ('Researchers', 'Data Scientists', 'General'), index=0)

submit = st.button("Generate the Blog")

if submit:
    if input_text and no_words:
        try:
            st.write(getLLamaresponse(input_text, no_words, blog_style))
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("Please enter both a topic and number of words.")
