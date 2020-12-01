async function delimit_text() {
    let text = document.getElementById('input_form').value

    let response = await fetch('/delimiter_remover', {
        method: "POST",
        body: JSON.stringify({value:text}),
        headers: {
            'content-type':'application/json'
        }
    })

    let res = await response.json()

    document.getElementById('output_form').value = res['message']
    document.getElementById('output_form_container').style.visibility="visible"

}

document.getElementById('input_btn').addEventListener('click',delimit_text)

