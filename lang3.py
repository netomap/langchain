from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

import os
from vars import gemini_api, pg_pass, pg_port

os.environ["GOOGLE_API_KEY"] = gemini_api

db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{pg_pass}@localhost:{pg_port}/langchainteste"
)

model = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0)

agent = create_sql_agent(
    llm = model,
    db = db,
    agent_type = "openai-tools",
    verbose = True
)

# pergunta = "quantos funcionários tem por cada equipe?"
# pergunta = "quem são os funcionários menores de idade?"
pergunta = "qual a quantidade de carros comprados com a cor branca?"

resposta = agent.invoke({'input': pergunta})

print (resposta['output'])