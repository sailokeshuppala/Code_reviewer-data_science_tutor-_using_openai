from openai import OpenAI
import streamlit as st

# Set title and page layout
st.set_page_config(page_title="Data Science Tutor", page_icon=":computer:", layout="wide")

# Title and subtitle
st.title("Data Science Tutor")
st.markdown("Welcome! This AI assistant helps you solve doubts in Data Science.")

# Load OpenAI API key from file
with open("keys/.new_api.txt") as f:
    key = f.read()

# Initialize OpenAI client
client = OpenAI(api_key=key)



if "memory" not in st.session_state:
    st.session_state["memory"]= []
st.chat_message("ai").write("Hi, How may i help you today")

for msg in st.session_state["memory"]:
    st.chat_message("user").write(msg)
prompt = st.chat_input()


if prompt:
    
        st.session_state["memory"].append({"role":"user","content" : prompt})
        st.chat_message("user").write(prompt)
        history = st.session_state["memory"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a helpful AI assistant.
                         
                         You will be given a Data Science topic as a input. First, you should explain the topic and solve the doubts if asked any and if any thing asked other than data science polietly say i don't know.
                                        """},
                {"role": "user", "content": prompt}
            ]
        )
    
    
        
        st.session_state["memory"].append({"role":"ai", "content": response.choices[0].message.content})
        st.chat_message("ai").write(response.choices[0].message.content)
        

