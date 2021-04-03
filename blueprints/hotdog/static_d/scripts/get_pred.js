async function get_pred_fn() {

    console.log("Hotdog!")
    let uploadForm = document.getElementById('uploadForm')
    let file = document.getElementById('file_wtf')
    let formData = new FormData()

    formData.append("file", file.files[0])

    console.log(file.files)
    let response = await fetch('/hotdog', {
        method: "POST",
        body: formData
        // do not add content-type, form data automatically generaets this
    })

    let res = await response.json()

    console.log(res['message'])

    document.getElementById('prediction_result').style.visibility="visible"
    document.getElementById('output_header').innerHTML = res['message']


}