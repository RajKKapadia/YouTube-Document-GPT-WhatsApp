from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from config import config

def create_conversation() -> ConversationalRetrievalChain:

    persist_directory = config.DB_DIR

    embeddings = OpenAIEmbeddings(
        openai_api_key=config.OPENAI_API_KEY
    )

    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=False
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(),
        chain_type='stuff',
        retriever=db.as_retriever(),
        memory=memory,
        get_chat_history=lambda h: h,
        verbose=True
    )

    return qa