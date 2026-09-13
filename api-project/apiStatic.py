#fastapi  静态文件
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn

app=FastAPI()

app.mount("/upimg", StaticFiles(directory="upimg"), name="upimg")

if __name__ == "__main__":
    uvicorn.run("apiStatic:app", host="127.0.0.1", port=8000)
