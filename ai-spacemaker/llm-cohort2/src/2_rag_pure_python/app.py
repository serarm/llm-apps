# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)
import sys
import os
sys.path.append('../../lutil')
import openai  # importing openai for API usage
import chainlit as cl  # importing chainlit for our app
from chainlit.prompt import Prompt, PromptMessage  # importing prompt tools
from chainlit.playground.providers import ChatOpenAI  # importing ChatOpenAI tools
from dotenv import load_dotenv
from aimakerspace.text_utils import TextFileLoader, CharacterTextSplitter
from aimakerspace.vectordatabase import VectorDatabase
import asyncio
from raq_qa_reterieval_wandb import RetrievalAugmentedQAPipeline,raqa_prompt,user_prompt
from aimakerspace.openai_utils.chatmodel import ChatOpenAI
import wandb




load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
os.environ["WANDB_API_KEY"] = os.environ["WANDB_API_KEY"]



@cl.on_chat_start  # marks a function that will be executed at the start of a user session
async def start_chat():
    msg = cl.Message(
        content=f"Loading Dataset ...", disable_human_feedback=True
    )
    await msg.send()
    text_loader = TextFileLoader("../../data/KingLear.txt")
    documents = text_loader.load_documents()
    text_splitter = CharacterTextSplitter()
    split_documents = text_splitter.split_texts(documents)
    vector_db = VectorDatabase()
    vector_db = asyncio.run(vector_db.abuild_from_list(split_documents))
    chat_openai = ChatOpenAI()
    retrieval_augmented_qa_pipeline = RetrievalAugmentedQAPipeline(
    vector_db_retriever=vector_db,
    llm=chat_openai,
    wandb_project="RAQ ins pure python")
    msg.content = f"Dataset loading is done. You can now ask questions!"
    await msg.update()
    cl.user_session.set("chain", retrieval_augmented_qa_pipeline)

@cl.on_message  # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: str):
    # settings = cl.user_session.get("settings")
    chain = cl.user_session.get("chain")  

    output = chain.run_pipeline(message)
    print(output)
    msg = cl.Message(content=f"{output}")
    # msg.prompt = output
    await msg.send()
