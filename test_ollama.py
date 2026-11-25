import requests
adres = "http://localhost:11434/api/chat"

veri = {
    "model": "qwen3.5:4b",
   "messages": [
    
    {"role": "user", "content": "Benim adım neydi?"}
],
    "stream": False

}

cevap = requests.post(adres, json=veri)
sonuc = cevap.json()
print(sonuc["message"]["content"])