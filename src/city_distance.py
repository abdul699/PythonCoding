from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    # value of latitude and longitude in radian is (latitide)*pi/180 . So calculated pi/180 and stored in p
    p = pi/180
    R = 6371 # Radius of earth
    # Used Haversine_formula to calculate distance, ref: https://en.wikipedia.org/wiki/Haversine_formula
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return R * 2 * asin(sqrt(a)) 



def main():
    # taking input parameter
    lat1_str, lon1_str = input("City 1: " ).split(', ')
    lat2_str, lon2_str = input("City 2: " ).split(', ')

    # seoarating latitude/longtitude and direction
    lat1, lat1_dir = lat1_str.split(' ')
    lon1, lon1_dir = lon1_str.split(' ')
    lat2, lat2_dir = lat2_str.split(' ')
    lon2, lon2_dir = lon2_str.split(' ')

    # converting latitude/longtitude to floats
    converted_latitude1 = float(lat1)
    converted_longitude1 = float(lon1)
    converted_latitude2 = float(lat2)
    converted_longitude2 = float(lon2)

    # checking if latitude dir is S then lies in down direction and if longitude dir is W then on left side keeping then as -ve
    if lat1_dir == "S":
        converted_latitude1 = -1.00*converted_latitude1
    if lat2_dir == "S":
        converted_latitude2 = -1.00*converted_latitude2
    if lon1_dir == "W":
        converted_longitude1 = -1.00*converted_longitude1
    if lon2_dir == "W":
        converted_longitude2 = -1.00*converted_longitude2

    print("City 1 and City 2 are " + str(distance(converted_latitude1, converted_longitude1, converted_latitude2, converted_longitude2)) + " km apart")

if __name__ == "__main__":     
    main()


