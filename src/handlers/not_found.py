import random


def generate_404(environ) -> tuple:
    """
    Give me a WSGI environ and I will return bytes
    :param environ:
    :return:
    """
    url = environ["PATH_INFO"]
    pin = random.randint(1, 1000)
    msg = f"Hello world! Your path: {url} not found. Pin: {pin}"

    payload = msg.encode()
    status = "404 Not Found"
    headers = {
        "Content-type": "text/plain",
    }
    return status, headers, payload
