import re


SUPPLIERS = [
    "CATL",
    "BYD",
    "Panasonic",
    "LG Energy Solution",
    "Samsung SDI",
    "Tesla",
    "SK On"
]

MATERIALS = [
    "Lithium",
    "Nickel",
    "Cobalt",
    "Graphite",
    "Copper",
    "Manganese"
]

COUNTRIES = [
    "China",
    "India",
    "USA",
    "Canada",
    "Australia",
    "Indonesia",
    "Chile",
    "Brazil",
    "South Korea",
    "Japan"
]


def extract_entities(text: str):
    supplier = "Unknown"
    material = "Unknown"
    region = "Global"

    for s in SUPPLIERS:
        if re.search(s, text, re.IGNORECASE):
            supplier = s
            break

    for m in MATERIALS:
        if re.search(m, text, re.IGNORECASE):
            material = m
            break

    for c in COUNTRIES:
        if re.search(c, text, re.IGNORECASE):
            region = c
            break

    return supplier, material, region