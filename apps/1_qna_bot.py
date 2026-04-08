from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# que = "Who is PM of India?"
# result = llm.invoke(que)
# print(result.content)

while True:
    query = input("User: ")
    if query.lower() in ["quit","exit","bye"]:
        print("GoodBye")
        break

    result = llm.invoke(query)
    print(result.content)