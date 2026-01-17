from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

import os
from vars import gemini_api

os.environ["GOOGLE_API_KEY"] = gemini_api

# Aqui definimos a estrutura dos das entidades que queremos receber como resposta
class Resposta_Estruturada(BaseModel):
    operacao: str = Field(description="Operação de venda ou compra da transação", examples=["Venda", "Compra"])
    produto: str = Field(description="Descrição do produto da transação")
    quantidade: int = Field(description="Quantidade do item negociado na transação")
    valor_total: float = Field(description="Valor, em reais, do total da transação")

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    temperature = 0
)

model_structured = model.with_structured_output(Resposta_Estruturada)

template = ChatPromptTemplate.from_messages([
    ("system", "Você apenas é um fiscal de transações. Vai receber um texto e extrair as entidades exigidas."),
    ("user", "{mensagem}")
])

chain = template | model_structured

for mensagem in [
    "O estoque que tinha 18 tablets acabou hoje. vendemos tudo por 50 reais cada",
    "Ana comprou 4 abacates para a festa de hoje. reclamou que deu 34 reais.. tá muito caro",
    "ele financiou o carro dele por 75k.",
    "Sei lá por quanto ele vendeu isso.. já faz um tempo né"
    ]:
    resultado = chain.invoke(
        {"mensagem": mensagem}
    )
    print (mensagem)
    print (resultado.model_dump())
    print (20*"*")