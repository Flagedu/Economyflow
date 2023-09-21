x = {
	"error": [
		{
			"code": "AHDD01",
			"description": "Blocked Country"
		}
	]
}

y = x.get("error", None)

print(y[0].get("description"))