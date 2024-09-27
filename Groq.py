from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0,model_name="llama-3.1-70b-versatile")
response = llm.invoke("write python code to reverse string without using inbuilt function")
print(response.content)

