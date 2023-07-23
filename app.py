from email import message
import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("Hello ㄱㄴㄷ팟! \n 생성형 인공지능 테스트 페이지")


with st.form("form"):
    user_input = st.text_input("Prompt")
    size=st.selectbox("Size",["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role":"system",
        "content":"magine the detail apperarence of the input. Response it shortly and around 200 words" 
    }]

    gpt_prompt.append({
        "role":"user",
        "content": user_input
    })

    with st.spinner("ㄱㄴㄷㄱㄴㄷ..."):
        gpt_response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)


    with st.spinner("ㄱㄴㄷㄱㄴㄷ..."):
       dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_response["data"][0]["url"])