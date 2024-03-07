import csv
import googlemaps

KITAS = []


def check_business_status(business_status):
    return business_status == "OPERATIONAL"


def set_kita_data(kita_data):
    kita = {"name": None, "address": None, "phone": None, "website": None}
    # Set kita data
    kita["name"] = kita_data["result"]["name"]
    kita["address"] = kita_data["result"]["formatted_address"]
    if "formatted_phone_number" in kita_data["result"]:
        kita["phone"] = kita_data["result"]["formatted_phone_number"]
    if "website" in kita_data["result"]:
        kita["website"] = kita_data["result"]["website"]
    KITAS.append(kita)


def get_kitas(address, radius, api_key):
    try:
        # Instanciates a Google API client
        gmaps = googlemaps.Client(key=api_key)

        # Get geocode of an address
        geocode_result = gmaps.geocode(address)
        set_geocode = geocode_result[0]["geometry"]["location"]

        # Get places data
        places_result = gmaps.places_nearby(
            location=(set_geocode), radius=radius, keyword="kita"
        )

        for item in places_result["results"]:
            business_status = item["business_status"]
            # Check if tha place still functioning
            if check_business_status(business_status):
                # Get information about the kita
                kita_place_id = item["place_id"]
                kita_data = gmaps.place(kita_place_id)
                set_kita_data(kita_data)
            else:
                print("This kita is not functioning anymore")
    except Exception as e:
        print(f"An error occurred: {e}")
    return KITAS


def export_to_csv(filename):
    try:
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "name",
                "address",
                "phone",
                "website",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for kita in KITAS:
                writer.writerow(
                    {
                        "name": kita["name"],
                        "address": kita["address"],
                        "phone": kita["phone"],
                        "website": kita["website"],
                    }
                )
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")


if __name__ == "__main__":
    address = input("Address:")
    if not address:
        print("An address was not provided. The default value for the address is 'Dubliner Str. 59, 13349 Berlin'.")
        address = "Avenue Charles de Gaulle 10 B, 13469"
    radius = input("Radius in meters: ")
    if not radius:
        print("Radius was not provided. The default value for the radius is 1000m.")
        radius = 1000
    api_key = input("API KEY(required): ")

    kitas = get_kitas(address, radius, api_key)

    export_to_csv("kitas_near_address.csv")
