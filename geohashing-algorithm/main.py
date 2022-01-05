import hashlib


def geohash(dow, date):
    coordinates: list = []
    date_dow: object = date.strftime("%Y-%m-%d") + "-" + str(dow)
    md5_hex_output: str = hashlib.md5(date_dow.encode('utf-8')).hexdigest()
    latitude_part: str = "0." + md5_hex_output[:16]
    longitude_part: str = "0." + md5_hex_output[16:]
    latitude_decimal: float = float.fromhex(latitude_part)
    longitude_decimal: float = float.fromhex(longitude_part)
    longitude = float("{:.6}".format(longitude_decimal))
    latitude = float("{:.6}".format(latitude_decimal))
    
    coordinates.extend([latitude, longitude])
    
    return coordinates

