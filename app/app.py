import chainlit as cl


@cl.on_chat_start
async def start():
    await cl.Message(content="Andddddddddd we are live!!").send()