<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-1.9.1.js"></script>
    <script src="main.js" defer></script>
    <link rel="stylesheet" href="styles.css">
    <title>ChatBot</title>
</head>
<body>
    <h1>ChatBot</h1>
    <div id="chat">
        <div id="chat-area"></div>
        <div id="resp">
            <p id="resposta"></p>
            <button id="botaoResposta" onclick="tocar()"><img src="play.png"></button>
        </div>
        <input type="text" id="pergunta" placeholder="Digite sua pergunta: ">
        <button id="perguntar">Enviar</button>
    </div>
</body>
</html>