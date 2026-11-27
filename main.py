from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.staticfiles import StaticFiles

app = FastAPI()

gecmis = []

class Kalip(BaseModel):

    mesaj : str

''' @app.get("/")
def ana_sayfa():
   return {"mesaj": "Merhaba"} '''


@app.post("/chat")

def veri_al(veri: Kalip):
    gecmis.append({"role": "user", "content": veri.mesaj})
    adres = "http://localhost:11434/api/chat"

    istek =  {
    "model": "qwen3.5:4b",
   "messages": 
       gecmis ,
    "stream": False
}
    yanit = requests.post(adres, json=istek)
    sonuc = yanit.json()
    gecmis.append({"role": "assistant", "content":sonuc["message"]["content"]})

    return {"cevap":sonuc["message"]["content"]}

app.mount("/", StaticFiles(directory="static", html=True), name="static")

