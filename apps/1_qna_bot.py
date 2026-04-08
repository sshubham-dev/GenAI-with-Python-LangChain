from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with Langchain and Google Gemini !")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask anything ?")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai", "content":res.content})




# que = "Who is PM of India?"
# result = llm.invoke(que)
# print(result.content)

# while True:
# query = input("Ask anything ?")
    # if query.lower() in ["quit","exit","bye"]:
    #     print("GoodBye")
    #     break

    # result = llm.invoke(query)
    # print(result.content)