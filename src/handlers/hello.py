from framework.types import RequestT
from framework.types import ResponseT


def hello(request: RequestT) -> ResponseT:

    name = request.query.get("name") or "anon"
    msg = f"Hello, {name}!"

    payload = msg.encode()
    status = "200 ok"
    headers_strings = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers_strings, payload)
