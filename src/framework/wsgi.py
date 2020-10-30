from handlers.handle_image import handle_image
from handlers.handle_index import handle_index
from handlers.not_found import generate_404
from handlers.Styles import handle_style


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handlers = {
        "/xxx/": handle_style,
        "/img.jpg/": handle_image,
        "/": handle_index,
    }

    handler = handlers.get(url, generate_404)

    status, headers, payload = handler(environ)

    start_response(status, list(headers.items()))

    yield payload
