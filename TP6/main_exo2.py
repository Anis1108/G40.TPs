from exo2 import format_http_response

headers = {
    "Content-Type": "text/html"
}

response = format_http_response(
    1,
    200,
    headers,
    "<html><body><h1>TP6 Exo2</h1></body></html>"
)

print(response)
