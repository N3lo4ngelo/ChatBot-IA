const botaoResposta = document.getElementById("botaoResposta");
$(document).ready(function () {
    $("#perguntar").click(function () {
        
        var pergunta = $("#pergunta").val();
        console.log(pergunta);
        $.ajax({
            url: 'conectChat.php',
            method: 'post',
            dataType: 'json',
            data: {
                pergunta:pergunta
            },

            success: function (data) {
                console.log(data);
                if(data.status != "error") {
                    var response = document.getElementById('resposta');
                    botaoResposta.style.visibility = "visible";
                    response.textContent = data;
                } else{
                    $("resposta").val("Erro");
                }
            },

            error: function (xhr, status, error) {
                console.log(xhr.responseText);
            }
        })  

    })

});

function tocar(){
    const audio = new Audio("log.mp3");
    audio.play()
}