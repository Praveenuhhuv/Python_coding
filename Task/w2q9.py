monuments = {
    "Delhi": "Red Fort",
    "Agra": "Taj Mahal",
    "Jaipur": "Jal Mahal"
}

city = input("Enter a city (Delhi, Agra, Jaipur): ").strip()

if city in monuments:
    print(monuments[city])
else:
    print("Monument information is not available for this city.")