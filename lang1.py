import os
from vars import gemini_api

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GOOGLE_API_KEY"] = gemini_api

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    temperature = 0,
    convert_system_message_to_human = True 
)

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um especialista em Machine Learning e Python."),
    ("user", "Me dê uma explicação técnica resumida sobre: {topico}")
])

parser = StrOutputParser()

chain = template | model | parser

resposta = chain.invoke(
    {"topico": "o que é langchain?"}
)

print (resposta)