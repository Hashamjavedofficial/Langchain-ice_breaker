import os
from pinecone import Pinecone

from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


load_dotenv()

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

if __name__ == "__main__":
    print("Hello vectors")

    loader = TextLoader("medium-blog1.txt")
    document = loader.load()
    print("Document loaded", document)

    print("splitting text")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    text = text_splitter.split_documents(document)
    print(f"created {len(text)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    print("Ingesting into Pinecone")
    PineconeVectorStore.from_documents(
        text,
        embeddings,
        index_name="medium-blogs-embeddings-index",
    )
