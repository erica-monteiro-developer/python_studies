import gradio as gr
import math

def fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos"
    return math.factorial(num)

iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    # Como não vamos realizar nenhum cálculo com o valor na interface, podemos deixar como texto no output
    outputs="text",
    title="Calculadora de Fatorial",
    description="Insira um número para obter o fatorial"
)

iface.launch()