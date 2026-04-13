def format_http_request(method, url, version, headers, body):
    valid_methods = ["GET", "POST", "PUT", "DELETE", "HEAD"]
    
    if method not in valid_methods:
        raise ValueError("Méthode HTTP invalide")

    if version == 1:
        http_version = "HTTP/1.1"
    elif version == 2:
        http_version = "HTTP/2.0"
    else:
        raise ValueError("Version HTTP invalide")

    request = f"{method} {url} {http_version}\n"

    for key, value in headers.items():
        request += f"{key}: {value}\n"

    request += "\n"
    request += body

    return request
