import axios from "axios"

const API = https://rag-llm-yx9n.onrender.com

export async function askQuestion(question){

 const res = await axios.post(
    `${API}/chat`,
    {
      question
    }
 )

 return res.data.answer
}