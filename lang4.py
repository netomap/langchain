from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from vars import gemini_api
import os

os.environ["GOOGLE_API_KEY"] = gemini_api

model = ChatGoogleGenerativeAI(
    model = "gemini-flash-latest",
    temperature = 0
)

@tool
def enviar_email(destinatario: str, conteudo: str)->None:
    """
    Função que envia um prepara um texto para enviar por email. precisa dos argumentos destinatário e o conteúdo. 
    Você pode reescrever o conteúdo mais informal, entre amigos. 
    Use essa ferramenta quando o usuário pedir para enviar, avisar, informar mensagens por email.
    """
    print (f'Email enviado para {destinatario} com conteudo: \n{conteudo}')
    print (50*'*')

@tool
def registrar_conteudo(nome_arquivo: str, conteudo: str)->None:
    """
    Função que registra um documento com extensão .txt com o conteúdo forneceido nessa função.
    É para salvar no formato yyyy-mm-dd-MM-HH-ss.txt exatamente como o conteúdo foi passado.
    Use essa ferramenta quando o usuário pedir para salvar, registrar, logar, anotar. 
    """
    print (f'Documento registrado com conteúdo: {conteudo}')

model = model.bind_tools([enviar_email, registrar_conteudo])

for chamada in [
    "explique porque o céu é azul em um parágrafo.",
    "é necessário enviar um email para o manuel@gmail.com informando que a reunião vai ser cancelada. o projeto atrasou.", 
    "salva aí essa informação: o custo da proposta passou muito do esperado. Vamos declinar e procurar outros fornecedores...",
    "Registra que precisamos revisar o projeto até amanhã e depois envie um email para o joao@gmail.com. informando esse assunto."
]:
    print (chamada)
    resposta = model.invoke(chamada)
    
    print (f'{resposta.tool_calls=}')
    
    print (50*'*')