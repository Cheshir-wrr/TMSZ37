from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_image(_request: RequestT) -> ResponseT:
    payload = read_static("img.jpg")
    status = build_status(200)
    headers = {"Content-type": "img/jpg"}

    return ResponseT(status, headers, payload)
