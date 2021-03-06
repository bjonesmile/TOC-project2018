import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAWvYcUVRB0BABuQdgG4JpCevdcid6JaZBphPJ0Y29hmuCYZAtfveFuCE9H3r2GRxN6n38T6ONZBRHPzupGoCAtaJgQRwxuaovQszyZBmmrvsBgqy6A4RQR1WV7xvAZAcxEiw8fn0bDokoCqrUSaM0IZA9Xh2kZC2vvaIunXpLSswZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
