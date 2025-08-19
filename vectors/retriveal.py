import os
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain import hub

load_dotenv()


def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


if __name__ == "__main__":
    print("Retriveing vectors")

    embeddings = OpenAIEmbeddings()

    llm = ChatOpenAI()

    query = "what is Pinecone in machine learning?"
    chain = PromptTemplate.from_template(template=query) | llm

    result = chain.invoke(input={})

    print(result.content)

    vector_store = PineconeVectorStore(
        index_name=os.environ.get("INDEX_NAME"), embedding=embeddings
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

    retrieval_chain = create_retrieval_chain(
        retriever=vector_store.as_retriever(), combine_docs_chain=combine_docs_chain
    )

    result = retrieval_chain.invoke(input={"input": query})

    print("result", result)

    template = """
    Answer any use questions based solely on the context below, If you don't know the answer say 'I don't know' or 'I am not sure. Don't try to make up the answer

<context>
{context}
</context>

Question: {question}

Helpful Answer:

"""

    custom_rag_prompt = PromptTemplate.from_template(template=template)

    vector_docs = vector_store.as_retriever()

    rag_chain = (
        {
            "context": vector_docs | format_docs,
            "question": RunnablePassthrough(),
        }
        | custom_rag_prompt
        | llm
    )

    res = rag_chain.invoke(input={"input": query})

    print(res)
