from framework.types import RequestT
from framework.types import ResponseT
from handlers.not_found import read_static


def handle_index(_request: RequestT) -> ResponseT:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()

    result = base_html.format(xxx=index_html)
    result = result.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    return ResponseT(
        headers=headers,
        payload=result,
        status=status,
    )