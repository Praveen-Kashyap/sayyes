import streamlit as st

st.set_page_config(
    page_title="A Very Important Question ❤️",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff0f5, #ffe4ec);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #d6336c;
    margin-top: 40px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #777;
    margin-bottom: 30px;
}

.question-box {
    background: rgba(255,255,255,0.85);
    border-radius: 25px;
    padding: 45px 25px;
    text-align: center;
    box-shadow: 0px 10px 30px rgba(214, 51, 108, 0.15);
}

.question {
    font-size: 30px;
    font-weight: 600;
    color: #333;
    margin-bottom: 35px;
}

/* Button arena */

#arena {
    position: relative;
    width: 100%;
    height: 180px;
    overflow: hidden;
    border-radius: 20px;
}

/* YES button */

#yesButton {
    position: absolute;
    left: 38%;
    top: 50%;
    transform: translate(-50%, -50%);

    background: #ff4d79;
    color: white;
    border: none;
    border-radius: 50px;

    padding: 15px 35px;
    font-size: 20px;
    font-weight: bold;

    cursor: pointer;

    box-shadow: 0px 5px 15px rgba(255,77,121,0.3);
}

/* NO button */

#noButton {
    position: absolute;

    left: 62%;
    top: 50%;

    transform: translate(-50%, -50%);

    background: white;
    color: #555;

    border: 2px solid #ddd;
    border-radius: 50px;

    padding: 15px 35px;

    font-size: 20px;
    font-weight: bold;

    cursor: pointer;

    transition: left 0.15s ease, top 0.15s ease;
}

#message {
    margin-top: 20px;
    color: #d6336c;
    font-size: 16px;
}

/* Success screen */

#success {
    display: none;
    text-align: center;
}

.big-heart {
    font-size: 80px;
    animation: heartbeat 1s infinite;
}

.success-title {
    font-size: 42px;
    color: #d6336c;
    font-weight: bold;
}

.success-text {
    font-size: 22px;
    color: #555;
}

@keyframes heartbeat {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.2);
    }

    100% {
        transform: scale(1);
    }

}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Website HTML + JavaScript
# -----------------------------

html_code = """

<div class="question-box" id="questionBox">

    <div class="main-title">
        💗 A Very Important Question 💗
    </div>

    <div class="subtitle">
        Please think carefully before answering...
    </div>

    <div class="question">
        Will you choose me? 🥺❤️
    </div>

    <div id="arena">

        <button id="yesButton">
            YES ❤️
        </button>

        <button id="noButton">
            NO 😭
        </button>

    </div>

    <div id="message">
        Go on... try clicking NO 😏
    </div>

</div>


<div id="success">

    <div class="big-heart">
        ❤️
    </div>

    <div class="success-title">
        I KNEW IT! 🥰
    </div>

    <div class="success-text">
        You just made me the happiest person ever. ❤️
    </div>

    <div style="font-size:40px; margin-top:25px;">
        💕 💗 💖 💘 💝
    </div>

    <div class="success-text" style="margin-top:25px;">
        Now you can't take it back. 😌
    </div>

</div>


<script>

const noButton = document.getElementById("noButton");
const yesButton = document.getElementById("yesButton");
const arena = document.getElementById("arena");

const message = document.getElementById("message");

const questionBox = document.getElementById("questionBox");
const success = document.getElementById("success");


const messages = [

    "Nice try 😏",

    "Nope! 😂",

    "You really thought you could click NO?",

    "The NO button is scared of you 😭",

    "Try YES instead ❤️",

    "Why are you chasing NO? 😂",

    "I'm faster than you 😌",

    "There is only one correct answer ❤️"

];


let attempts = 0;


function moveButton() {

    const arenaWidth = arena.clientWidth;
    const arenaHeight = arena.clientHeight;

    const buttonWidth = noButton.offsetWidth;
    const buttonHeight = noButton.offsetHeight;


    const maxX = arenaWidth - buttonWidth - 10;
    const maxY = arenaHeight - buttonHeight - 10;


    const randomX =
        Math.floor(Math.random() * maxX) + 5;

    const randomY =
        Math.floor(Math.random() * maxY) + 5;


    noButton.style.left = randomX + "px";
    noButton.style.top = randomY + "px";

    noButton.style.transform = "none";


    message.innerText =
        messages[attempts % messages.length];

    attempts++;

}


/*
    Desktop:
    Run away when mouse approaches.
*/

noButton.addEventListener(
    "mouseenter",
    moveButton
);


/*
    Mobile:
    Run away when she tries touching it.
*/

noButton.addEventListener(
    "touchstart",
    function(event) {

        event.preventDefault();

        moveButton();

    }
);


/*
    Also prevent actual clicking.
*/

noButton.addEventListener(
    "click",
    function(event) {

        event.preventDefault();

        moveButton();

    }
);


/*
    YES button
*/

yesButton.addEventListener(
    "click",
    function() {

        questionBox.style.display = "none";

        success.style.display = "block";

        createHearts();

    }
);


/*
    Floating hearts
*/

function createHearts() {

    for(let i = 0; i < 25; i++) {

        const heart =
            document.createElement("div");

        heart.innerHTML = "❤️";

        heart.style.position = "fixed";

        heart.style.left =
            Math.random() * 100 + "%";

        heart.style.top = "100%";

        heart.style.fontSize =
            (20 + Math.random() * 30) + "px";

        heart.style.pointerEvents = "none";

        heart.style.transition =
            "all 3s ease-out";

        document.body.appendChild(heart);


        setTimeout(function() {

            heart.style.top =
                Math.random() * 50 + "%";

            heart.style.opacity = "0";

            heart.style.transform =
                "translateY(-300px)";

        }, 100);


        setTimeout(function() {

            heart.remove();

        }, 3500);

    }

}

</script>

"""

st.components.v1.html(
    html_code,
    height=650,
    scrolling=False
)
