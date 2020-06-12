from httpx import HTTPError


def get_http_err_content(e: HTTPError):
    try:
        return e.response.content.decode()
    except AttributeError:
        return ""


class ApiClientError(Exception):
    """ Base error of the ApiClient """


class ApiCallError(ApiClientError):
    """ Retrocomptiblity """


class ApiClientRequestError(ApiClientError):
    """ Error during a request with the ApiClient """