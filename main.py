import os
import requests
from fastapi import FastAPI, Request

app = FastAPI()

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        update = await request.json()
        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text", "")
            
            if text == "/start":
                requests.post(f"{BASE_URL}/sendMessage", json={
                    "chat_id": chat_id,
                    "text": "Hello! I am running seamlessly on Kuberns."
                })
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
