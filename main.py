import os
import requests
from fastapi import FastAPI, Request
from datetime import datetime


app = FastAPI()

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_amazing_alert(header):
             print(111)
             BOT_TOKEN = "8861282098:AAEAUNblYeQwnxr-uYH-Odaubwvk_ITFf9Q"
             user_telegram_id = "8812384862"

             today = datetime.now()
             formatted_date = today.strftime("%B %d, %Y")

             header_html = (
             "📅 <b>TODAY'S DAILY MATCHES</b>\n"
             f"<code>🤖 Generated: {formatted_date}</code>\n"
             "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
             )

             message_html = (
             f"<b></b>\n"
             "━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    
             f"<b>Job Title:</b>\n \n\n"
    
             f"<b>Experience Level:</b> \n\n"
    
             f"<b>Salary Range:</b> \n\n"
    
             f"<b>Job Type:</b>\n \n\n"
    
             f"<b>Company Name:</b>\n \n\n"
    
             f"<b>Job Location:</b>\n \n\n"
    
             "<b>Job Description:</b>\n"
             f"\n\n"
    
             "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
             f"🔗 <a href='https://yourwebsite.com'><b>View Full Details</b></a>"
         )





             if header:
                   message_html = header_html
             url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
             payload = {
                 "chat_id": "8812384862",
                 "text": message_html,
                 "parse_mode": "HTML"
             }

             response = requests.post(url, json=payload)
             print(response.json()) # Verifies success or shows API errors
             return "good"




@app.get("/")
async def telegram_webhook(request: Request):
        return {"status": "error", "message": "good"}
                
@app.get("/send/{pas}")
async def generalbot(pas): 
    print(" Request arived ..")
    return send_amazing_alert(False)
    
