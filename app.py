import eng_to_ipa as ipa

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/text-to-ipa', methods=['GET'])
def text_to_ipa():
    text = request.args.get('text')
    ipa_result = text_to_ipa_function(text)
    return jsonify({"ipa": ipa_result})


def text_to_ipa_function(text):
    return ipa.convert(text)


if __name__ == '__main__':
    app.run(debug=True)
