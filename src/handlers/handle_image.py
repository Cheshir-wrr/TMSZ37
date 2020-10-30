from static.read_static import read_static


def handle_image(_environ):
    payload = read_static("img.jpg")
    status = "200 OK"
    headers = {"Content-type": "img.jpg"}

    return status, headers, payload
