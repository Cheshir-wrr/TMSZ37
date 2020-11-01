from framework.types import RequestT
from framework.types import ResponseT
from handlers.not_found import read_static


def handle_image(_request: RequestT) -> ResponseT:
    payload = read_static("img.jpg")
    status = "200 OK"
    headers = {"Content-type": "img.jpg"}

    return ResponseT(status, headers, payload)
