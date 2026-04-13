from http_utils import format_http_request

headers = {
    "Host": "localhost:8000",
    "User-Agent": "Python"
}

req = format_http_request(
    "GET",
    "/index.html",
    1,
    headers,
    ""
)

print(req)
