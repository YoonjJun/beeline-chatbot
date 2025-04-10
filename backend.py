from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class ChatInput(BaseModel):
    message: str


@app.post("/chat")
def chat(input: ChatInput):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input.message}]
    )
    return {"response": chat_completion.choices[0].message.content}
