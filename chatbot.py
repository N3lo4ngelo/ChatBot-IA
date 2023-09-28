from flask import Flask, request, jsonify
import random
from nltk.tokenize import word_tokenize
import nltk
from voice import text_to_voice as ttv
perguntas_respostas = {
    1:"Olá! Como posso ajudar você?",
    2:"Estou bem, obrigado por perguntar.",
    3:"Meu nome é ChatBot.",
    4:"Posso responder a perguntas simples.",
    5:"Eu sou um chatbot, uso algoritmos de processamento de linguagem natural para entender suas perguntas e fornecer respostas adequadas.",
    6:"Você pode interagir com um chatbot digitando mensagens de texto em uma janela de chat ou falando com ele usando comandos de voz.",
    7:"Essa pergunta é um dos grandes mistérios da existência.",
    8:"O que é um terapeuta? 1.024 gigapeutas",
    9:"Tchau! Tenha um bom dia!"
}

cumprimento = ["olá", "oi", "hello", "hi", "see you soon"]
perguntas =  ["como você está?", "tudo bem?", "bem", "tudo bem", "como vai", "how are you?"]
perguntas_nome = ["nome", "qual é o seu nome?", "seu nome?", "me fale sobre você"]
perguntas_pergunta = ["perguntas simples", "consegue me responder?", "responder"]
perguntas_info = ["quem é você?", "o quê você faz?", "como você funciona?"]
perguntas_interacao = ["ajuda", "como posso interagir?", "preciso de ajuda", "interagir"]
perguntas_filosoficas = ["viver", "qual o sentido da vida?", "por quê viver", "existir", "existência"]
perguntas_piadas = ["piada", "engraçado", "risada"]


app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    print("Olá! Sou o CavaloMan. Digite 'Tchau' para finalizar nossa conversa")
    
    data = request.json
    user_question = data['question']
    resposta = responder_pergunta(user_question)
    
    return jsonify({'response': resposta})


def responder_pergunta(pergunta):
    tokens = word_tokenize(pergunta.lower())
    tokens = tokens if tokens.count(" ") < 1 else (tokens[0] + " " + tokens[1])
    print("TOKEN: ", tokens)
    
    p = [cumprimento, perguntas, perguntas_nome, perguntas_pergunta, perguntas_info, perguntas_interacao, perguntas_filosoficas, perguntas_piadas]

    for index, words in enumerate(p):
      if pergunta in words: 
        key_pergunta = index+1
        resposta = perguntas_respostas.get(key_pergunta)
        ttv(resposta, "log.mp3")
        return resposta
    return "Não entendi sua pergunta"
            

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
