def format_http_response(version, status_code, headers, body):
    # Version HTTP
    if version == 1:
        http_version = "HTTP/1.1"
    elif version == 2:
        http_version = "HTTP/2.0"
    else:
        raise ValueError("Version HTTP invalide")

    # Codes HTTP
    status_messages = {
        200: "OK",
        404: "Not Found",
        400: "Bad Request"
    }

    if status_code not in status_messages:
        raise ValueError("Code HTTP invalide")

    status_text = status_messages[status_code]

    # Construction réponse
    response = f"{http_version} {status_code} {status_text}\n"

    for key, value in headers.items():
        response += f"{key}: {value}\n"

    response += "\n"
    response += body

    return response
