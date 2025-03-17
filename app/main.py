from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
from util.upload_docs import upload_pdfs
from chat.knowledge_chat import chat
# 初始化 FastAPI 实例
app = FastAPI()


# 批量上传PDF文件的API
# app.post("/upload_pdfs/")(upload_pdfs)
# chat交互的API
app.post("/chat/")(chat)


if __name__ == '__main__':
    uvicorn.run(app='ragapi:app', host="127.0.0.1", port=8000, reload=True)