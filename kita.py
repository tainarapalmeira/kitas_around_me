import requests
import csv


def get_kitas(address, api_key):
    # Increase the radius parameter to cover a larger area (e.g., 10000 meters)
    radius = 10000
    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={address}&radius={radius}&type=child_care&keyword=kita&key={api_key}"
    # lat = "52.6024712"
    # lon = "13.3212267"
    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=child_care&location=-{lat}%{lon}&radius=1500&type=restaurant&key={api_key}"

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=cruise&location=-33.8670522%2C151.1957362&radius=1500&type=child_care&key={api_key}"
    print(url)

    # Print the URL
    print("API URL:", url)

    response = requests.get(url)
    data = response.json()

    # Print the response
    print("API Response:", data)

    return data["results"]


def export_to_csv(kitas, filename):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [
            "Name",
            "Address",
            "Telephone",
            "Distance",
        ]  # Add 'Telephone' field
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for kita in kitas:
            # Check if 'formatted_phone_number' exists in the kita details
            telephone = kita.get("formatted_phone_number", "N/A")
            writer.writerow(
                {
                    "Name": kita["name"],
                    "Address": kita["vicinity"],
                    "Telephone": telephone,
                    "Distance": kita.get("distance", "N/A"),
                }
            )


if __name__ == "__main__":
    address = "Avenue Charles de Gaulle 10 B, 13469"
    api_key = "AIzaSyCsNjtUsi1lFf398p94NKLQfFpuhDWNszE"

    kitas = get_kitas(address, api_key)

    export_to_csv(kitas, "kitas_near_address.csv")
