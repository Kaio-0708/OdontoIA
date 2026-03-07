# RAG Odontologia - Chat Inteligente de Odontologia com Documentos

Projeto desenvolvido para a disciplina Inteligência Artificial aplicada a Sistemas Físico-Cibernéticos do curso de Engenharia Elétrica na UFCG.
Sistema de **Perguntas e Respostas baseado em RAG (Retrieval-Augmented Generation)** especializado na área de **Odontologia**.

A aplicação permite que o usuário envie **documentos PDF ou TXT**, que são processados, convertidos em **embeddings vetoriais**, armazenados em um **banco vetorial ChromaDB**, e utilizados para responder perguntas utilizando um **LLM da Mistral AI**.

A interface foi construída com **Streamlit**, permitindo interação simples entre usuário e documento.

# Arquitetura do Sistema

O sistema segue a arquitetura clássica de **RAG (Retrieval-Augmented Generation)**:

Documento
↓
Conversão para texto
↓
Limpeza
↓
Chunking
↓
Embeddings
↓
Banco Vetorial (ChromaDB)
↓
Busca Semântica
↓
Construção do Prompt
↓
LLM (Mistral)
↓
Resposta

# Tecnologias Utilizadas

- Python
- Streamlit
- ChromaDB
- Mistral AI API
- Docling
- Regex (re)
- python-dotenv

# Funcionamento do Pipeline

O sistema utiliza o conceito de **Retrieval-Augmented Generation (RAG)**, que combina **busca semântica em banco vetorial com geração de texto por LLM**.

## 1. Upload do Documento

O usuário envia um arquivo:

- `.pdf`
- `.txt`

A interface do sistema é responsável por receber esse arquivo e iniciar o processamento.

# Conversão de Documento

Arquivos PDF são convertidos para texto utilizando a biblioteca **Docling**.

Arquivos TXT são carregados diretamente.

Arquivo responsável:
core/convert.py
Função principal:
analisarPdf(uploadedFile)

# Limpeza de Texto

Após a conversão, o texto passa por um processo de limpeza para remover inconsistências.

Principais operações:

- Padronização de quebras de linha
- Remoção de múltiplas linhas vazias
- Remoção de espaços extras
- Correção de palavras quebradas por hífen

Arquivo responsável:
core/cleaner.py
Função principal:
clearText(text)

# Chunking do Documento

Para permitir recuperação eficiente de contexto, o texto é dividido em **blocos menores (chunks)**.

Configuração utilizada:

| Parâmetro | Valor |
|----------|------|
| Tamanho do Chunk | 700 tokens |
| Overlap | 100 tokens |

O **overlap evita perda de informação entre blocos consecutivos**.

Arquivo responsável:
core/chunking.py
Função principal:
chunkText(text, size=700, overlap=100)

# Criação de Embeddings

Cada chunk de texto é convertido em um vetor numérico usando o modelo:
mistral-embed

Esses vetores representam semanticamente o conteúdo do texto.

Arquivo responsável:
core/embeddings.py
Função principal:
embedding(text)


# Banco Vetorial

Os embeddings são armazenados em um banco vetorial **ChromaDB**.

Arquivo responsável:
database/vetor_db.py
Funções principais:

### Inicializar banco

initDB()

### Adicionar chunks

addChunks(collection, chunks, embedding_function)

### Buscar contexto relevante

search(collection, query_text, embedding_function, k)

# Recuperação de Contexto

Quando o usuário faz uma pergunta:

1. A pergunta é convertida em embedding
2. O banco vetorial busca os **top-k trechos mais similares**
3. Esses trechos são utilizados como contexto para o LLM

# Construção do Prompt

Os segmentos recuperados são organizados em um prompt estruturado.

Arquivo responsável:
core/prompt.py
Função principal:
prompt(contextSegments, question)

O prompt impõe regras importantes ao modelo:

- responder **somente com base no contexto**
- não inventar informações
- não usar markdown
- não responder fora do tema odontológico

Caso a resposta não esteja no documento:
Não há informações suficientes no contexto fornecido.

# Geração da Resposta

A resposta é gerada utilizando o modelo:

mistral-medium-latest

Arquivo responsável:
core/llmService.py
Função principal:
chatResponse(prompt)

# Pipeline RAG

O fluxo final de resposta ocorre no arquivo:
core/rag.py
Função principal:
answerQuestion(collection, question, embedding_function, k=3)

Fluxo interno:

Pergunta
↓
Busca no banco vetorial
↓
Recuperação de segmentos
↓
Construção do prompt
↓
Envio para LLM
↓
Resposta

# Interface Streamlit

A interface da aplicação permite:

- Upload de documentos
- Processamento automático
- Perguntas sobre o documento
- Controle de **Top-K**
- Visualização dos trechos usados

Arquivo principal:
app.py

O usuário pode visualizar:

- resposta gerada
- trechos utilizados
- scores de similaridade

Exemplo de Fluxo de Uso

1. Usuário envia PDF de odontologia  
2. Documento é convertido para texto  
3. Texto é limpo  
4. Texto é dividido em chunks  
5. Chunks viram embeddings  
6. Embeddings são armazenados no ChromaDB  
7. Usuário faz pergunta  
8. Sistema recupera trechos relevantes  
9. LLM gera resposta baseada no contexto  

# Controle de Respostas

O sistema foi projetado para **evitar alucinação do modelo**.

Se a informação não estiver presente no documento, o modelo retorna:

Não há informações suficientes no contexto fornecido.

## Streamlit Cloud: 
https://odontoia-kxjsrwjqwcow2jhz63p3sr.streamlit.app/

## Autor

Kaio Vitor - [GitHub](https://github.com/Kaio-0708)

