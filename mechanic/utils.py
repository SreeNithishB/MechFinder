

def get_googlemaps_direction_url(o_lat, o_lng, d_lat, d_lng):
    def convert_dd_to_dms_for_lat(decdegrees):
        degrees = int(decdegrees)
        temp = 60 * (decdegrees - degrees)
        minutes = int(temp)
        seconds = 60 * (temp - minutes)
        return str(degrees) + '°' + str(minutes) + "'" + str(seconds) + '"N'

    def convert_dd_to_dms_for_lng(decdegrees):
        degrees = int(decdegrees)
        temp = 60 * (decdegrees - degrees)
        minutes = int(temp)
        seconds = 60 * (temp - minutes)
        return str(degrees) + '°' + str(minutes) + "'" + str(seconds) + '"E'

    origin = str(convert_dd_to_dms_for_lat(o_lat)) + "+" + str(convert_dd_to_dms_for_lng(o_lng))
    destination = str(convert_dd_to_dms_for_lat(d_lat)) + "+" + str(convert_dd_to_dms_for_lng(d_lng))
    url = 'https://www.google.com/maps/dir/' + str(origin) + "/" + str(destination) + "/"

    return url
