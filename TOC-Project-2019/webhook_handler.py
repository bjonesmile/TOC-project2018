import json

from bottle import route, run, request


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('REQUEST BODY: ')
    print(json.dumps(body, indent=2))

run(host="localhost", port=80, debug=True)
