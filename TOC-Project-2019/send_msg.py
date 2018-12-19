import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EAAWvYcUVRB0BAFM5BkJgIaMHj7bimEcvbTFzGQsHk75QElVfRKjeykpTx4MIuyHKZArweLapbsXlRCOLrhxtMSDIn5XobDIzHcLRAMgguDKl8TSVIEPedU6wqkps8KW2sbfkOZBmwO7MiaPPY1EZCixwHBlOkOwtZBGt3InJzAZDZD")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
