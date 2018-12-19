from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "ready"
machine = TocMachine(
    states=[
        'user',
        'ironclad',
        'silent',
        'defect',
        'state1',
        'state2',
        'state3',
        'monster1',
        'monster2',
        'elite',
        'monster3',
        'monster4',
        'finalboss',
        'theend'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger':'advance',
            'source':'user',
            'dest':'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger':'advance',
            'source':'user',
            'dest':'ironclad',
            'conditions': 'choose_ironclad'
        },
        {
            'trigger':'advance',
            'source':'user',
            'dest':'silent',
            'conditions': 'choose_silent'
        },
        {
            'trigger':'advance',
            'source':'user',
            'dest':'defect',
            'conditions': 'choose_defect'
        },
        {
            'trigger':'advance',
            'source':'user',
            'dest':'monster1',
            'conditions': 'is_going_to_monster1'
        },
        {
            'trigger':'advance',
            'source':'monster1',
            'dest':'monster2',
            'conditions': 'is_going_to_monster2'
        },
        {
            'trigger':'advance',
            'source':'monster2',
            'dest':'elite',
            'conditions': 'is_going_to_elite'
        },
        {
            'trigger':'advance',
            'source':'elite',
            'dest':'monster3',
            'conditions': 'is_going_to_monster3'
        },
        {
            'trigger':'advance',
            'source':'monster3',
            'dest':'monster4',
            'conditions': 'is_going_to_monster4'
        },
        {
            'trigger':'advance',
            'source':'monster4',
            'dest':'finalboss',
            'conditions': 'is_going_to_finalboss'
        },
        {
            'trigger':'advance',
            'source':'finalboss',
            'dest':'theend',
            'conditions': 'is_going_to_theend'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'ironclad',
                'silent',
                'defect',
                'theend'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=80, debug=True, reloader=True)
