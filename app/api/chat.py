# -*- coding: utf-8 -*-
"""
File: chat.py
Author: Hing
Date: 2025-03-17
Description: 聊天模型推理服务接口，包括用户输入处理、大模型调用与响应格式封装。
"""

from fastapi import Body, Request


def chat(qeury: str = Body(..., description="用户输入", examples=["你好"])):
    """
    处理用户输入并返回模型回复。

    Args:
        query (str): 用户输入的消息文本。

    Returns:
        str: 生成的模型回复。
    """
    pass