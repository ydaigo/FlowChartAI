from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
import gradio as gr
from PIL import Image
import subprocess

from core import gpt

CUSTOM_PATH = "/"

app = FastAPI()

load_dotenv()


@app.middleware("http")
async def some_fastapi_middleware(request: Request, call_next):
    response = await call_next(request)

    response_body = ""
    async for chunk in response.body_iterator:
        response_body += chunk.decode()

    some_javascript = """
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
    setInterval(function() {
            mermaid.contentLoaded()
    }, 100);
    mermaid.initialize({'theme':'base'});
    </script>
    """

    response_body = response_body.replace("</head>", some_javascript + "</head>")

    del response.headers["content-length"]

    return Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


def function(text):
    mermaid_text = gpt.create_flow_chart(text)
    html = f"""
<div class='mermaid'>
{mermaid_text}
</div>
"""
    return html


inputs = gr.Text(lines=5,label="フローチャートを作成したい文章を入力してください。",value="料理の手順を説明します。まず、器具と皿を準備します。調味料の分量を計り、材料を切ります。それらを使って調理をします。最後に盛り付けて完成です。")
outputs = gr.HTML()
io = gr.Interface(fn=function,
                  inputs=inputs,
                  outputs=outputs,
                  allow_flagging='never',
                  title="フローチャート作成AI",
                  description="ChatGPTを利用してフローチャートを作成する。"
                                                                                            )
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
