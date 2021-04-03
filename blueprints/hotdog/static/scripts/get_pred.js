async function get_pred_fn() {
    let uploadForm = document.getElementById('uploadForm')
    let file = document.getElementById('file_wtf')

    let inputFile = file.files[0]

    let previewContainer = document.getElementById('image_preview')
    let previewImage = document.getElementById('image_preview_image')
    let previewDefaultText = document.getElementById('image_preview_default_text')

    let formData = new FormData()
    formData.append("file", inputFile)

    let response = await fetch('/hotdog', {
        method: "POST",
        body: formData
        // do not add content-type, form data automatically generaets this
    })

    let res = await response.json()

    // Generate Preview Image
    let reader = new FileReader()

    previewDefaultText.style.display = "none"
    previewImage.style.display ="block"

    reader.addEventListener("load", function () {
        previewImage.setAttribute('src', this.result)
    })

    reader.readAsDataURL(inputFile)


    document.getElementById('prediction_result').style.visibility="visible"
    document.getElementById('output_header').innerHTML = res['message']


}