from flask import render_template, request, jsonify, make_response, url_for, redirect, Blueprint
from blueprints.hotdog.static.forms.hotdog_form import FileUploadForm
from blueprints.hotdog.model.pretrained_resnet import Hotdog_Model_Resnet
from PIL import Image
from torch.nn.functional import softmax
from torch import topk

hotdog_app = Blueprint("hotdog_app", __name__,
                       template_folder="templates",
                       static_folder="static",
                       static_url_path='/blueprints/hotdog/static')

# Model created as a global variable to cache it
model = Hotdog_Model_Resnet()
model.model.eval()

@hotdog_app.route('/hotdog',methods=['GET','POST'])
def hotdog():

    form = FileUploadForm()
    if request.method == 'POST':
        uploaded_file = request.files['file']
        img = Image.open(uploaded_file).convert('RGB')
        input_img = model.transform(img)
        input_batch = input_img.unsqueeze(0)

        output = model.model(input_batch)
        scores = softmax(output[0], 0)

        top_prob, top_catid = topk(scores, 1)

        pred_class = 'Hotdog' if top_catid[0].item() == model.HOTDOG_CLASS else "Not Hotdog"

        return make_response(jsonify({'message': pred_class}), 200)
    else:
        return render_template('/hotdog_app.html', form=form)

@hotdog_app.errorhandler(413)
def too_large(e):
    return make_response(jsonify({'message': "File too large, please make it smaller first"}), 413)