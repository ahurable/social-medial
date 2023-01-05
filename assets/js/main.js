
async function like(id) {
    
    const response = await fetch(`like/${id}`, {method:"get"})
    const txtResponse = await response.text()
    const jsnResponse = JSON.parse(txtResponse)
    var likesCount = document.getElementById("likeCount").innerHTML
    var likes = parseInt(likesCount)
    if(jsnResponse.sit == 0) {
        document.getElementById("likeBtn").style.color = "white"
        document.getElementById("likeCount").innerHTML = likes - 1
    } else if (jsnResponse.sit == 1) {
        document.getElementById("likeBtn").style.color = "#ff004c"
        document.getElementById("likeCount").innerHTML = likes + 1
    }
}