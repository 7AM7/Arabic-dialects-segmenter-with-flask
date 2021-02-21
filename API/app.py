import os
from flask import Flask,request,json
from model.predict import decode
from model.utils import getData, load_model

app = Flask(__name__)
# LOAD MODEL
model = load_model()

@app.route('/DialectalARSeg', methods=['GET', 'POST'])
def DialectalARSeg():
    try:
        text = request.args.get('text')
        result = decode(model, text)
        result_dict = {"result": result}
        return  app.response_class(
            response=json.dumps(result_dict, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    except Exception:
        return app.response_class(
            response="Not Found",
            status=400,
        )


if __name__ == '__main__':
    app.run(debug=False)
