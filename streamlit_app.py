import streamlit as st
import random
import asyncio
import streamlit as st
from streamlit.components.v1 import html
import time

st.set_page_config(layout="wide")

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
            height: 500px;
            margin: auto;
            position: relative;
            background: #f3f3f3;
            font-family: "DM Mono", sans-serif;
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

        header .status {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            height: 64px;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }

        header progress {
            width: 300px;
            accent-color: #000000;
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
            animation: animationZoom 30s linear forwards;
        }

        @keyframes animationZoom {
            100% {
                transform: scale(1.8);
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
            padding: 20px;
            font-size: 32px;
            font-family: "DM Mono", sans-serif;
            border-radius: 10px;
        }

        button {
            outline: none;
        }

        button:hover {
            filter: brightness(94%);
        }
    </style>
</head>

<body>
    <dialog>
        <div class="score-wrap">
            <p>score:</p>
            <p class="score">40</p>
        </div>
        <form method="dialog">
            <button onclick="location.reload()">Play Again</button>
        </form>
    </dialog>
    <header>
        <div class="status">
            <progress value="0" max="30"></progress>
        </div>
    </header>
    <div class="output">
        <h1></h1>
    </div>
    <div class="container">
    </div>

    <script>
        let primes = [2, 3, 5, 7, 11, 13]
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
                document.querySelector(".container").append(element_button)
            })
        }

        function devide(number) {
            if (prime_number % number == 0) {
                prime_number /= number
                score += number
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
        create_buttons()
        generate_product()
    </script>
</body>

</html>
"""

html(my_html ,height=520)

difficulty = 2
prime_lists = [2,3,5,7,11,13,17]

@st.experimental_dialog("Game Over!")
def gameover():
    if st.button("リプレイ"):
        st.rerun()

def generate_product(multiply_number):
    return random.randint(1,difficulty)*multiply_number

def devide(n):
    if st.session_state.number % n != 0:
        gameover()
    else:
        st.session_state.number /= n
        if st.session_state.number == 1:
            st.session_state.number = 1
            st.rerun()

if 'number' not in st.session_state:
    st.session_state.number = 1

    for prime in prime_lists:
        st.session_state.number *= generate_product(prime)


if st.button("2"):
    devide(2)

if st.button("3"):
    devide(3)

if st.button("5"):
    devide(5)

if st.button("7"):
    devide(7)

if st.button("11"):
    devide(11)

if st.button("13"):
    devide(13)

if st.button("17"):
    devide(17)


st.title(round(st.session_state.number))
