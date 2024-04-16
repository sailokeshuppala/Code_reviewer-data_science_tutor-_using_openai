from openai import OpenAI
import streamlit as st


f = open("keys/.new_api.txt")
key = f.read()

client = OpenAI(api_key = key)

prompt = st.text_area("Python Code", height=400)

if st.button("Generate"):
    response = client.chat.completions.create(
                      model="gpt-3.5-turbo",
                      messages=[
                        {"role": "system", "content": """you are helpful AI assistant.
                         
                         you will be given a python code first you should find the bugs and then correct the python code and give me.
                                        """},
                        {"role": "user", "content": prompt}
                      ]
                )
    
    if response.choices:
        st.write(response.choices[0].message.content)
    else:
        st.write("No response received.")
