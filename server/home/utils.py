from django.contrib.gis.geoip2 import GeoIP2


def get_country_code_from_ip(ip):
    try:
        g = GeoIP2()
        obj = g.city(ip)
        country_code = obj["country_code"]
    except:
        country_code = "BD"

    return country_code


