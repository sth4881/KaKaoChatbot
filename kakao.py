from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/skill", methods=["GET", "POST"]) # @app.route란? 어느 경로를 통해 들어갈 수 있는 지 나타내는 decorate 함수
def skill():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    }
    return jsonify(data)
def main():
    return "Hi! If u wanna get response about Skill server, Go to /skill"
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
