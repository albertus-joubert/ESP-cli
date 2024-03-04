from EspApi import EspApi
import argparse
import json
import sys

def main():

    parser = argparse.ArgumentParser(
        prog="ESP-CLI",
        description="A CLI tool for ESP API.",
        epilog="yeah"
    )

    parser.add_argument(
        "--token", 
        type=str, 
        metavar="LICENSE KEY", 
        help="Provide your license key, or omit it if already stored in config."
    )

    parser.add_argument(
        "--status", 
        action="store_true",
        help="Query the current loadshedding status."
    )

    parser.add_argument(
        "--area", 
        type=str, 
        metavar="AREA_ID",
        help="Query the loadshedding schedule of specified area."
    )

    parser.add_argument(
        "--nearby_areas", 
        nargs=2, 
        type=float, 
        metavar="COORDINATE",
        help="Query nearby areas using latitude and longitude."
    )

    parser.add_argument(
        "--search_areas", 
        nargs="+", 
        type=str, 
        metavar="TEXT",
        help="Query areas by search text."
    )

    parser.add_argument(
        "--nearby_topics", 
        nargs=2, 
        type=float, 
        metavar="COORDINATE",
        help="Query nearby topics using latitude and longitude."
    )

    parser.add_argument(
        "--check_allowance", 
        action="store_true",
        help="Check your usage token allowance."
    )

    args = parser.parse_args()

    token = ""
    if args.token is not None:
        token = args.token
    else:
        try:
            with open("config/token.txt", "r") as f:
                token = f.readline().strip()
        except:
            print("You need to a specify a token to use,")
            print("either with the argument '--token TOKEN',")
            print("or by storing a default in config/token.txt")
            sys.exit(0)

    esp = EspApi(token)

    if args.check_allowance:
        print("Allowance remaining:")
        print(json.dumps(esp.check_allowance(), indent=4))
        sys.exit(0)

    if args.status:
        print("Loadshedding status:")
        print(json.dumps(esp.status(), indent=4))
        sys.exit(0)

    if args.search_areas is not None:
        text = ' '.join(args.search_areas)
        print(f"Areas matching \"{text}\":")
        print(json.dumps(esp.areas_search(text), indent=4))
        sys.exit(0)

    if args.nearby_areas is not None:
        lat, lon = args.nearby_areas
        print(f"Areas near ({lat}, {lon}):")
        print(json.dumps(esp.areas_nearby(lat, lon), indent=4))
        sys.exit(0)

    if args.nearby_topics is not None:
        lat, lon = args.nearby_topics
        print(f"Topics near ({lat}, {lon}):")
        print(json.dumps(esp.topics_nearby(lat, lon), indent=4))
        sys.exit(0)

    area_id = 0
    if args.area is None:
        try:
            with open("config/area-id.txt", "r") as f:
                area_id = f.readline().strip()
        except:
            print("You need to specify an area ID to query,")
            print("either with the argument '--area AREA_ID,")
            print("or by storing a default in config/area_id.txt")
            sys.exit(0)
    else:
        area_id = args.area

    print(f"Loadshedding info of {area_id}:")
    print(json.dumps(esp.area(area_id), indent=4))

if __name__ == '__main__':
    main()
