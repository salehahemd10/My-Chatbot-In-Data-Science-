from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# جهز pipeline لتوليد النصوص باستخدام موديل محلي
chat_pipe = pipeline("text-generation", model="distilgpt2")

class UserInput(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(user_input: UserInput):
    try:
        result = chat_pipe(user_input.user_input, max_length=50, num_return_sequences=1)
        text = result[0]["generated_text"]
        return {"response": text}
    except Exception as e:
        return {"response": f"Error during generation: {e}"}
