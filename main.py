import sys
from geocoder import get_coordinates
from mapapi_PG import show_map


def main():
    toponym = " ".join(sys.argv[1:])
    if toponym:
        x, y = get_coordinates(toponym)
        show_map((x, y),ll_spn=f"ll={x},{y}&spn=0.003,0.003", map_type="map")
    else:
        print(":(")

    
if __name__ == '__main__':
    main()