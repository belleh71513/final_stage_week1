const mainElement = document.querySelector("main");
const btn = document.querySelector("#btn")
const src = "/api/files";

async function getData(){
  const res = await fetch(src)
  const data = await res.json()
  return data
}

async function upload(){
  const message = document.querySelector("#message").value
  const imageFile = document.querySelector("#image").files[0]

  const uploadBody = new FormData();
  uploadBody.append("message", message)
  uploadBody.append("image", imageFile)
  try {
    let uploadData = {
      method: "POST",
      body: uploadBody
    }
    const res = await fetch(src, uploadData)
    const result = await res.json()
    console.log(result)
    window.location.href = "/"
  }
  catch (error) {
    console.error(error)
  }
}

btn.addEventListener("click", upload)

function render(result){
  messageBoard = result.data


  for(let item of messageBoard){

    const {message, image} = item

    let divElement = document.createElement("div")
    divElement.classList.add("container")
    let hrLine = document.createElement("hr")
    let pElement = document.createElement("p")
    pElement.innerText = message

    let imgContainer = document.createElement("div")
    imgContainer.classList.add("img-container")
    let img = document.createElement("img")
    img.src = image

    let bottomHrLine = document.createElement("hr")

    imgContainer.appendChild(img)
    divElement.append(hrLine, pElement, imgContainer)
    let divZero = document.querySelectorAll(".container")[0]
    mainElement.append(divElement, bottomHrLine)
    mainElement.insertBefore(divElement, divZero)
  }
}



async function init(){
  const data = await getData()
  render(data)
}
init()
