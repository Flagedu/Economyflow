import base64

us_pass = b"menareefat-api:a54sOce7OXdFKqghQFo3"
b64Val = base64.b64encode(us_pass)

print(b64Val.decode("utf-8"))

