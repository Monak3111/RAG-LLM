import "./style.css"
import { askQuestion } from "./api.js"

document.querySelector("#app").innerHTML = `
<h1>AI BOT</h1>

<div id="chat"></div>

<input id="input" placeholder="Ask something..." />

<button id="send">
Send
</button>
`

const input = document.querySelector("#input")
const chat = document.querySelector("#chat")
const button = document.querySelector("#send")


button.onclick = async () => {

 const question = input.value

 chat.innerHTML += `
 <p><b>You:</b> ${question}</p>
 `

 input.value = ""

 const answer = await askQuestion(question)

 chat.innerHTML += `
 <p><b>Bot:</b> ${answer}</p>
 `
}