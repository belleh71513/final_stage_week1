const mainElement = document.querySelector("main");
const btn = document.querySelector("#btn")
const src = "/api/files";

async function getData(){
  const res = await fetch(src)
  const data = res.json()
  return data
}

async function upload(){
  const message = document.querySelector("#message")
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
    render(result);
  }
  catch (error) {
    console.error(error)
  }
}

btn.addEventListener("click", upload)

function render(result){
  const {message, image} = result

  let divElement = document.createElement("div")
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
  mainElement.append(divElement, bottomHrLine)
}

async function init(){
  const data = await getData()
  render(data)
}

