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
                        "text": "User Key: " + str(request.json['userRequest']['user']['properties']['plusfriendUserKey'])
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "QuickReply1",
                    "action": "message",
                    "messageText": "QuickReply1 ResponseMSG"
                },
                {
                    "label": "QuickReply1",
                    "action": "message",
                    "messageText": "QuickReply1 ResponseMSG"
                },
                {
                    "label": "QuickReply1",
                    "action": "message",
                    "messageText": "QuickReply1 ResponseMSG"
                }
            ]
        }
    }
                    # "basicCard": {
                    #     "title": "카드의 제목",
                    #     "description": "상세 설명",
                    #     "thumbnail": {
                    #         "imageUrl":
                    #         "https://t1.daumcdn.net/friends/www/talk/kakaofriends_talk_2018.png",
                    #         "link": {
                    #             "mobile": "https://naver.com",
                    #             "android": "https://google.com"
                    #         }
                    #     },
                    #     "buttons": [
                    #         {
                    #             "label": "Go to Azure",
                    #             "action": "webLink",
                    #             "webLinkUrl": "https://portal.azure.com"
                    #         },
                    #         {
                    #             "label": "Share",
                    #             "action": "share"
                    #         }
                    #     ]
                    # }
    #              }
    #         ]
    #     }
    # }
    return jsonify(data)
def main():
    return "Hi! If u wanna get response about Skill server, Go to /skill"
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
