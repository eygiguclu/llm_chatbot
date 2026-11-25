from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Kalip(BaseModel):

    mesaj : str

@app.get("/")
def ana_sayfa():
    return {"mesaj": "Merhaba"}


@app.post("/chat")

def veri_al(veri: Kalip):
    adres = "http://localhost:11434/api/chat"

    istek =  {
    "model": "qwen3.5:4b",
   "messages": [
    
    {"role": "user", "content": veri.mesaj}
],
    "stream": False
}
    yanit = requests.post(adres, json=istek)
    sonuc = yanit.json()

    return {"cevap":sonuc["message"]["content"]}

