async function delimit_text() {

    let text = document.getElementById('inputTextArea').value
    let delimiter = document.getElementById('delimiterInput').value
    console.log(delimiter)

    let response = await fetch('/delimiter_remover', {
        method: "POST",
        body: JSON.stringify({text:text,
                                   delimiter:delimiter}),
        headers: {
            'content-type':'application/json'
        }
    })

    let res = await response.json()

    document.getElementById('outputTextArea').value = res['message']
    document.getElementById('output_form_container').style.visibility="visible"
}


