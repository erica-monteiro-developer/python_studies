# módulo fornece manipulação de arquivos em memória (em vez de arquivos no disco). Ex.: salvar imagens ou pdfs em RAM
import io 
# Este módulo é usado para codificar dados binários em texto e vice-versa. Ex.: enviar imagens via HTML, incluir arquivos em JSON...
import base64
# PIL (Pillow -> versão atualizada da Python Imaging Library) -> serve para manipular imagens 
# Image -> classe principal responsável por representar as imagens
from PIL import Image
import numpy as np
import gradio as gr

def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
    estilo = (
        f"background-color: {cor_fundo};"
        f"color: {cor_texto};"
        f"padding: 20px;"
        f"text-align: center;"
    )

    # Converte a imagem para base64 se estiver presente
    imagem_html = ""
    if imagem is not None:
        buffered = io.BytesIO()
        Image.fromarray(imagem).save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        imagem_html = (
            f"<img src='data:image/png;base64,{img_str}' "
            "style='max-width: 100%; height: auto;'>"
        )

    slide_html = f"""
        <div style="{estilo}">
            <h1>{titulo}</h1>
            <p>{texto}</p>
            {imagem_html}
        </div>
    """
    return slide_html

iface = gr.Interface(
    fn=criar_slide,
    inputs=[
        gr.Textbox(label="Título do Slide", placeholder="Digite o título.."),
        gr.Textbox(label="Texto do Slide", placeholder="Digite o texto.."),
        gr.Image(type="numpy", label="Imagem do slide"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto", value="#000000"),
    ],
    outputs=gr.HTML(label="Slide customizado"),
    title="Criador de Slides",
    description="Crie um slide personalizado"
)

iface.launch()