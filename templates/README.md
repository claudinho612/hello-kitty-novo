[Uploading inde<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verificação de Calouro</title>
    <style>
        body {
            background-color: pink;
            color: black;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            overflow: hidden; /* Impede que a imagem saia da tela */
        }
        h1 {
            font-size: 48px; /* Aumenta o tamanho da fonte do título */
        }
        input, button {
            font-size: 24px;
            padding: 10px;
            margin-top: 5px;
        }
        img {
            width: 250px; /* Aumentando a largura da imagem 3 */
            height: 250px; /* Aumentando a altura da imagem 3 */
            position: absolute; /* Para mover a imagem */
            top: 300px; /* Ajuste a posição inicial da imagem */
            transition: left 0.5s, top 0.5s; /* Adiciona transição suave ao mover a imagem */
        }
        .imagem1 {
            width: 200px; /* Diminuindo a largura da imagem 1 */
            height: 200px; /* Diminuindo a altura da imagem 1 */
        }
        /* Estilo para o texto de créditos no canto inferior direito */
        #creditos {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: black; /* Cor preta */
            font-size: 30px; /* Aumentando o tamanho da fonte */
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Você é calouro? (S, N ou talvez)</h1>

    <!-- Exibindo a imagem inicial (Imagem 3) -->
    <img id="helloKitty" src="{{ url_for('static', filename='hello_kitty_3.png') }}" alt="Hello Kitty">

    <form method="POST">
        <input type="text" name="resposta" placeholder="Digite 'S', 'N' ou 'talvez'" required>
        <button type="submit">Verificar</button>
    </form>

    <h2 id="resultado"></h2>

    <!-- Texto de créditos -->
    <div id="creditos">
        CRÉDITOS PARA O PROGAMADOR CLÁUDIO DA 612 <br> @claudio._fl
    </div>

    <script>
        // Função que faz a imagem "pular" aleatoriamente
        function fazerImagemPular(imagemSrc) {
            var imagem = document.getElementById('helloKitty');
            imagem.src = imagemSrc; // Define a imagem que deve pular
            var larguraTela = window.innerWidth - imagem.width; // largura da tela menos a largura da imagem
            var alturaTela = window.innerHeight - imagem.height; // altura da tela menos a altura da imagem

            // Função para mover a imagem aleatoriamente
            function pular() {
                // Gera uma posição aleatória para a imagem dentro da tela
                var posX = Math.random() * larguraTela;
                var posY = Math.random() * alturaTela;

                // Move a imagem para a nova posição
                imagem.style.left = posX + 'px';
                imagem.style.top = posY + 'px';
            }

            // Chama a função de pulo a cada 500ms para simular o movimento
            setInterval(pular, 500);
        }

        // Verificar a resposta do usuário
        document.querySelector('form').onsubmit = function(event) {
            event.preventDefault(); // Impede o envio do formulário

            var resposta = document.querySelector('input[name="resposta"]').value.toLowerCase();

            if (resposta === 'n') {
                // Se a resposta for "N", faz a imagem pular e alternar entre a imagem 2 e a imagem 3
                fazerImagemPular("{{ url_for('static', filename='hello_kitty_3.png') }}");
                document.querySelector('#resultado').textContent = "Ataaaa você é normal, agora a Hello Kitty está feliz e saltitante!!!"; // Feedback visual
            } else if (resposta === 'eu sou voce') {
                document.querySelector('#resultado').textContent = "OLÁ MEU CRIADOR";
            } else if (resposta === 'hello kitty') {
                document.querySelector('#resultado').textContent = "oiiiii";
            } else if (resposta === 's') {
                // Se a resposta for "S", mostra a imagem 1
                var imagem = document.getElementById('helloKitty');
                imagem.src = "{{ url_for('static', filename='hello_kitty_1.png') }}";
                imagem.className = "imagem1"; // Adiciona a classe para a imagem 1
                document.querySelector('#resultado').textContent = "HAHAHAHAHAHHA, SEU BIXO!!!"; // Feedback visual para resposta 'S'
            } else if (resposta === 'talvez') {
                // Se a resposta for "talvez", mostra a imagem 4 e a mensagem
                var imagem = document.getElementById('helloKitty');
                imagem.src = "{{ url_for('static', filename='hello_kitty_4.png') }}"; // Altera para a imagem 4
                imagem.className = ""; // Remove a classe para a imagem 3
                document.querySelector('#resultado').textContent = "pau no seu cu"; // Mensagem para resposta 'talvez'
            } else if (resposta === 'não te interessa') {
                // Se a resposta for "não te interessa", faz a imagem 4 pular
                fazerImagemPular("{{ url_for('static', filename='hello_kitty_4.png') }}"); // Chama a função para fazer a imagem 4 pular
                document.querySelector('#resultado').textContent = "VAI TOMAR NO CU SEU FILHO DA PUTA, NÃO QUER RESPONDER? VAI SE FUDERRRRRR"; // Mensagem para resposta 'não te interessa'
            } else {
                document.querySelector('#resultado').textContent = "Resposta inválida!"; // Mensagem para resposta inválida
            }
        };
    </script>
</body>
</html>
x.html…]()
