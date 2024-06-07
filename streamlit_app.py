import streamlit as st
from streamlit.components.v1 import html
st.set_page_config(page_title="Factorization-Game",layout="wide")

my_html = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Inter:wght@100..900&display=swap');

        body {
            width: 100%;
            height: 100%;
            margin: auto;
            position: relative;
            background: #f3f3f3;
            font-family: "DM Mono", sans-serif;
            color: #222;
        }

        main {
            position: fixed;
            width: 100%;
            height: 100%;
            max-height: 500px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        dialog {
            border-radius: 10px;
            border: #ddd;
            text-align: center;
            padding: 12px;
            width: 300px;
            font-family: "Inter", sans-serif;
        }

        dialog h2 {
            font-size: 32px;
            margin: 24px;
        }

        dialog .score-wrap {
            margin: 32px;
        }

        dialog p {
            margin: 0;
        }

        dialog .score {
            font-size: 70px;
            font-family: "DM Mono", sans-serif !important;
        }

        dialog .high-score {
            font-size: 32px;
        }

        dialog button {
            border: none;
            width: 100%;
            font-size: 22px;
            padding: 4px;
            border-radius: 5px;
        }

        header {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            height: 36px;
            top: 15px;
            align-items: center;
            justify-content: center;
            gap: 0px;
            width: 100%;
            max-width: 540px;
        }

        header .status {
            width: 50%;
            padding: 0 20px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            gap: 4px;
            border-radius: 400px;
        }

        header progress {
            width: 100%;
            accent-color: #222;
        }

        header .status-score {
            width: 56px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-size: 33px;
            font-weight: 500;
            border-radius: 400px;
            color: #ef7000;
        }

        header .time {
            width: 40px;
            text-align: center;
            font-size: 26px;
        }

        .output {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        h1 {
            text-align: center;
            font-weight: 500;
            font-size: 80px;
            margin: 0;
            animation: animationZoom 26s linear forwards;
        }

        @keyframes animationZoom {
            100% {
                transform: scale(2);
            }
        }

        .container {
            position: absolute;
            left: 50%;
            bottom: 0;
            transform: translateX(-50%);
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 5px;
            width: 100%;
        }

        .container button {
            background-color: white;
            border: #ddd solid 1px;
            width: 78px;
            padding: 13px;
            font-size: 34px;
            font-family: "DM Mono", sans-serif;
            border-radius: 10px;
            color: #222;
        }

        button {
            outline: none;
        }

        button:hover {
            filter: brightness(94%);
        }

        button:active {
            filter: brightness(90%);
        }

        @media (max-width: 600px) {
            main {
                max-height: calc(100%);
            }

            h1 {
                font-size: 54px;
            }

            button:hover {
                filter: brightness(100%);
            }

            button:active {
                filter: brightness(90%);
            }

            .output {
                top: 45%;
            }

            .container {
                width: calc(100% - 30px);
                gap: 2px;
                bottom: 50px;
            }

            .container button {
                width: 49%;
                padding: 8px;
            }
        }
    </style>
</head>

<body>
    <dialog>
        <div class="score-wrap">
            <p>score:</p>
            <p class="score">0</p>
        </div>
        <form method="dialog">
            <button onclick="location.reload()">Play Again</button>
        </form>
    </dialog>
    <main>
        <header>
            <div class="status">
                <p></p>
                <progress value="0" max="30"></progress>
            </div>
            <div class="status-score">
                0
            </div>
        </header>
        <div class="output">
            <h1></h1>
        </div>
        <div class="container">
        </div>
    </main>


    <script>
        let primes = [2, 3, 5, 7, 11, 13]
        let keybind = ["s", "d", "f", "j", "k", "l"]
        let prime_list = [2, 3, 5, 7]
        let prime_number = 1
        let difficulty = 3
        let score = 0

        function set_timer() {
            let countDownSeconds = 30
            document.querySelector("progress").value = countDownSeconds
            countdown = setInterval(function () {
                countDownSeconds--

                document.querySelector("progress").value = countDownSeconds

                if (countDownSeconds === 0) {
                    clearInterval(countdown)
                    gameover()
                }
            }, 1000);
        }

        function gameover() {
            document.querySelector("dialog").showModal()
            document.querySelector(".score").innerText = score
        }

        function getRandomInt(max) {
            return Math.floor(Math.random() * max)
        }

        function generate_product() {
            set_timer()
            for (let i = 0; i < difficulty ** 2 / 6; i++) {
                prime_number *= prime_list[Math.floor(Math.random() * (prime_list.length - 1) + 1)] * (Math.round(getRandomInt(difficulty) + 1))
            }
            document.querySelector("h1").remove()

            let element_button = document.createElement("h1")
            element_button.innerText = prime_number
            document.querySelector(".output").append(element_button)
        }

        function create_buttons() {
            document.querySelector(".container").innerHTML = ''
            prime_list.forEach((value, index) => {
                let element_button = document.createElement("button")
                element_button.innerText = value
                element_button.setAttribute("onclick", `devide(${value})`)
                element_button.value = value
                document.querySelector(".container").append(element_button)
            })
        }

        function devide(number) {
            if (prime_number % number == 0) {
                prime_number /= number
                score += number
                document.querySelector(".status-score").innerText = score

                document.querySelector("h1").innerText = prime_number

                if (prime_number === 1) {
                    difficulty += 0.25
                    if (Number.isInteger(difficulty)) {
                        document.querySelector("h1").innerText = "!"
                        if (primes[difficulty] != undefined) {
                            prime_list.push(primes[difficulty])
                            create_buttons()
                        }
                    } else {
                        document.querySelector("h1").innerText = "1"
                    }

                    clearInterval(countdown)

                    window.setTimeout(generate_product, 340);
                }
            } else {
                gameover()
            }
        }
        document.addEventListener('keyup', keyup_event)
        document.addEventListener('keydown', keydown_event)
        function keyup_event(e) {
            document.querySelector("[value='" + primes[keybind.indexOf(e.key)] + "']").style.filter = "brightness(100%)"
        }
        function keydown_event(e) {
            devide(primes[keybind.indexOf(e.key)])
            document.querySelector("[value='" + primes[keybind.indexOf(e.key)] + "']").style.filter = "brightness(90%)"
        }
        create_buttons()
        generate_product()
    </script>
</body>

</html>
"""

html(my_html ,height=520)
st.markdown("""
        <style>
         iframe {
            position:fixed !important;
            top: 0% !important;
            left: 0 !important;
            width: 100% !important;
            height:100% !important;
            z-index: 100000000;
         }
         button[data-testid="manage-app-button"],button.styles_terminalButton__JBj5T{
            display: none !important;
         }
        </style>
        """, unsafe_allow_html=True)
