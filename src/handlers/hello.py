from framework.types import RequestT
from framework.types import ResponseT
from static.read_static import read_static


def hello(request: RequestT) -> ResponseT:

    name = (request.form_data.get("name") or [None])[0]
    address = (request.form_data.get("address") or [None])[0]

    base_html = read_static("_base.html").decode()
    hello_html = read_static("hello.html").decode()

    document = hello_html.format(
        address_header=address or "Nowhere",
        address_value=address or "",
        name_header=name or "Anon",
        name_value=name or "",
    )
    document = base_html.format(xxx=document)

    # msg = f"Hello, {name}!"

    payload = document.encode()
    status = "200 ok"
    headers = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers, payload)
