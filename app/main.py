from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
# from api import chat
# 初始化 FastAPI 实例
app = FastAPI()


# # chat交互的API
# app.post("/chat/")(chat)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)