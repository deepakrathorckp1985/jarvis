from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

llm = Ollama(model="llama3")

prompt = ChatPromptTemplate.from_template("Write me an poem about {topic} for 5 year old child")

add_routes(
    app,
    prompt|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
