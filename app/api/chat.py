from fastapi import Body, Request


def chat(qeury: str = Body(..., description="用户输入", examples=["你好"])):
    pass