from typing import Any
from typing import Dict
from urllib.parse import parse_qs


def get_form_data(body: bytes) -> Dict[str, Any]:
    qs = body.decode()
    form_data = parse_qs(qs or "")
    return form_data


def get_body(environ: dict) -> bytes:
    fp = environ["wsgi.input"]
    cl = int(environ.get("CONTENT_LENGTH") or 0)

    if not cl:
        return b""

    content = fp.read(cl)

    return content
