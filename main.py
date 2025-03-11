import openai
from fastapi import FastAPI, Form, File, UploadFile


AIPROXY_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDE3NTlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.-RkHBM2JbPrhiL_zEt8UWQbkvmIoNe9u6mm2TWM-A4Q"

OPENAI_BASE_URL = "https://aiproxy.sanand.workers.dev/openai/v1"

client = openai.OpenAI(
    api_key=AIPROXY_TOKEN, 
    base_url=OPENAI_BASE_URL
)

app = FastAPI()

@app.post("/api/")
async def process_question(
    question: str = Form(...), file: UploadFile = File(None)
):
    """
    Processes a question using OpenAI's GPT model and returns the answer.
    Supports optional file uploads (not used in this version).
    """
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}
