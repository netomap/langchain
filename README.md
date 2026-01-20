# Langchain

## [lang1.py](lang1.py)

- Neste script, é o primeiro projeto. Apenas criando uma requisição usando LLMs do Gemini. 

- No script tem-se uma pergunta: ```o que é langchain?```

- E a resposta é bem interessante:

Como especialista em Machine Learning e Python, posso te dar uma explicação técnica resumida sobre o LangChain.

**Em essência, LangChain é um framework de desenvolvimento em Python (e JavaScript) projetado para simplificar a criação de aplicações que utilizam Modelos de Linguagem Grandes (LLMs) como o GPT-3, GPT-4, Llama, etc.**

Pense no LangChain como um **"orquestrador"** que permite conectar LLMs a outras fontes de dados e ferramentas, transformando modelos de linguagem brutos em aplicações complexas e úteis.

**Componentes Chave e Conceitos Técnicos:**

1.  **LLMs (Large Language Models):** LangChain não é um LLM em si, mas sim uma interface para interagir com eles. Ele abstrai as complexidades de chamar diferentes APIs de LLMs (OpenAI, Hugging Face, Anthropic, etc.), permitindo que você troque de modelo facilmente.

2.  **Prompts:** A forma como você "fala" com um LLM é crucial. LangChain oferece ferramentas para gerenciar, formatar e otimizar prompts. Isso inclui:
    *   **Prompt Templates:** Estruturas reutilizáveis para criar prompts dinâmicos, onde você pode inserir variáveis.
    *   **Output Parsers:** Ferramentas para estruturar a saída do LLM em formatos específicos (JSON, listas, etc.), facilitando o processamento posterior.

3.  **Chains:** Este é o coração do LangChain. Uma "chain" é uma sequência de chamadas a LLMs ou a outras ferramentas. Você pode encadear várias operações para construir fluxos de trabalho complexos. Exemplos:
    *   **LLMChain:** A chain mais básica, que combina um prompt template com um LLM.
    *   **Sequential Chains:** Permitem executar várias chains em sequência, onde a saída de uma chain se torna a entrada da próxima.
    *   **Router Chains:** Permitem direcionar a execução para diferentes chains com base na entrada.

4.  **Agents:** Agentes são sistemas mais avançados que utilizam um LLM para decidir qual ação tomar. Eles têm acesso a um conjunto de "ferramentas" (tools) e usam o LLM para raciocinar sobre qual ferramenta usar e como usá-la para atingir um objetivo.
    *   **Tools:** Funções ou APIs que o agente pode usar (ex: busca na web, acesso a bancos de dados, execução de código Python).
    *   **Agent Executor:** O componente que gerencia o ciclo de raciocínio do agente: receber entrada, usar o LLM para escolher uma ação, executar a ação, receber o resultado e repetir até que o objetivo seja alcançado.

5.  **Memory:** Para que as aplicações de LLM sejam contextuais e lembrem de interações passadas, o LangChain oferece mecanismos de memória. Isso permite que o LLM "lembre" de conversas anteriores, mantendo o contexto.
    *   **ConversationBufferMemory:** Armazena todas as mensagens da conversa.
    *   **ConversationSummaryMemory:** Resume a conversa para economizar tokens.

6.  **Indexes:** Para que os LLMs possam interagir com seus próprios dados, o LangChain fornece ferramentas para indexar e recuperar informações.
    *   **Document Loaders:** Carregam dados de diversas fontes (arquivos, URLs, bancos de dados).
    *   **Text Splitters:** Dividem documentos grandes em pedaços menores para serem processados pelo LLM.
    *   **Vector Stores:** Armazenam representações vetoriais (embeddings) dos seus dados, permitindo buscas semânticas eficientes.
    *   **Retrievers:** Componentes que buscam informações relevantes em um índice para serem usadas pelo LLM.

**Por que usar LangChain?**

*   **Abstração:** Simplifica a interação com diversos LLMs e ferramentas.
*   **Modularidade:** Permite construir aplicações complexas combinando componentes reutilizáveis.
*   **Flexibilidade:** Facilita a experimentação com diferentes LLMs, prompts e estratégias.
*   **Produtividade:** Acelera o desenvolvimento de aplicações de IA generativa.

Em resumo, LangChain é um framework poderoso que democratiza o desenvolvimento de aplicações com LLMs, fornecendo uma estrutura robusta para conectar, orquestrar e gerenciar a interação entre modelos de linguagem, dados e ferramentas externas. Ele permite que desenvolvedores passem de "apenas usar um LLM" para "construir sistemas inteligentes que utilizam LLMs".



## [Lang2.py](lang2.py)

- No script lang2.py, temos uma análise de como retirar entidades de texto. Podemos enviar um texto, naturalmente não estruturado, e solicitamos que a LLM (no caso estamos usando Gemini) retire as entidades. 

- Uma forma prática de fazer isso é usando a biblioteca pydantic, onde criamos uma classe que herda BaseModel que descreve a entidade que você quer retirar dos textos:  
```
# Aqui definimos a estrutura dos das entidades que queremos receber como resposta
class Resposta_Estruturada(BaseModel):
    operacao: str = Field(description="Operação de venda ou compra da transação", examples=["Venda", "Compra"])
    produto: str = Field(description="Descrição do produto da transação")
    quantidade: int = Field(description="Quantidade do item negociado na transação")
    valor_total: float = Field(description="Valor, em reais, do total da transação")
```

- Depois informamos ao modelo que queremos uma resposta baseada na estrutura que passamos. Importante notar que a descrição de cada item precisa estar bem descrita, para o modelo tirar suas conclusões.  
```
model_structured = model.with_structured_output(Resposta_Estruturada)
```

- Criamos nossa cadeia simples: ```chain = template | model_structure```

- Os resultados são bem interessantes, para frases bem simples e aleatórias:

- 1ª frase:
```
O estoque que tinha 18 tablets acabou hoje. vendemos tudo por 50 reais cada
{'operacao': 'venda', 'produto': 'tablet', 'quantidade': 18, 'valor_total': 900.0}
```
- 2ª frase:
```
Ana comprou 4 abacates para a festa de hoje. reclamou que deu 34 reais.. tá muito caro
{'operacao': 'compra', 'produto': 'abacates', 'quantidade': 4, 'valor_total': 34.0}
```
- 3ª frase: Interessante notar que mesmo informando que só existem operações de compra e venda, ele pegou "financiamento". Está errado mas é facilmente corrigido.
```
ele financiou o carro dele por 75k.
{'operacao': 'financiamento', 'produto': 'carro', 'quantidade': 1, 'valor_total': 75000.0}
```
- 4ª frase: uma frase totalmente indefinida, o modelo não conseguiu captar o produto e retornou um "unknown".
```
Sei lá por quanto ele vendeu isso.. já faz um tempo né
{'operacao': 'venda', 'produto': 'unknown', 'quantidade': 0, 'valor_total': 0.0}
```

## [Lang3.py](lang3.py)

- Muito interessante essa abordagem. Para criar um agente que consulta uma base de dados, você tem o trabalho de somente apresentar a base de dados para o modelo e fazer a pergunta. Depois o modelo vai explorando todas as tabelas, colunas e conteúdos para criar a query ideal, executá-la e trazer as informações quando possível. 
- Interessante perceber que aqui, neste documento lang3.py, vamos apenas fazer consultas. Não vamos fazer update, create ou delete. Para estes casos, vamos trabalhar usando tools, pois assim vamos criar funções bem robustas para que o modelo não faça nenhuma consulta do tipo "delete from table" e deletar tudo, certo? 
- Assim, vamos criar funções robustas que evitem quaisquer erros grosseiros que possam vir das sugestões do model.

- Mas por enquanto, vamos focar apenas nas consultas de "descoberta" dos dados. Primeiro devemos informar qual é o banco de dados:
```
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{pg_pass}@localhost:{pg_port}/langchainteste"
)
```

- Criamos o modelo: ``` model = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0) ```

- E criamos o agente: 
```
agent = create_sql_agent(
    llm = model,
    db = db,
    agent_type = "openai-tools",
    verbose = True
)
```

- Os resultados são muito bons. Se não quiser ver os raciocínios, basta fazer: ```verbose = False```. 
- Antes disso, foi criado uma tabela numa base de dados no postgres. A tabela foi chamada de usuários e tinha algumas colunas como nome, email e idade. 
- A primeira pergunta foi: "quantos funcionários tem por cada equipe?".  
![figura1](assets/figura1.png)

- Segunda pergunta: "liste funcionários menores de idade"
![figura2](assets/figura2.png)
- Olha que legal, dependendo da entonação da chamada, tipo pergunta ou uma ordem, o tipo de resposta vem diferente. Quando perguntamos vem um dicionário com "input" e "output" de chaves. Quanto ordenamos (liste, enumere...) vem um dicionário com as chaves "type" e "text". **tem que ter um tratamento das respostas bem rigoroso**

- Terceira pergunta: "quem são os funcionários menores de idade?" A mesma solicitação anterior, agora no tom de pergunta.
![figura3](assets/figura3.png)

- Quarta pergunta: "qual a quantidade de carros comprados com a cor branca?" Uma pergunta sem sentido nenhum para a base de dados. E o modelo tem uma resposta curta e grossa.
![figura4](assets/figura4.png)