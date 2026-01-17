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


