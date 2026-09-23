import re


SUPPLIERS = [
    "CATL",
    "BYD",
    "Panasonic",
    "LG Energy Solution",
    "Samsung SDI",
    "Tesla",
    "SK On",
    "Albemarle",
    "SQM",
    "Ganfeng Lithium",
    "Vale",
    "BHP",
    "Rio Tinto",
    "Glencore",
    "Umicore",
    "Freeport-McMoRan",
    "Syrah Resources",
    "Novonix",
    "Epsilon Advanced Materials"
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
    "United States",
    "Canada",
    "Australia",
    "Indonesia",
    "Chile",
    "Brazil",
    "South Korea",
    "Japan",
    "Germany",
    "UK",
    "United Kingdom"
]


def extract_entities(text: str):

    text = str(text)

    supplier = "Unknown"
    material = "Unknown"
    region = "Unknown"

    # -----------------------------
    # Supplier extraction
    # -----------------------------

    for supplier_name in SUPPLIERS:

        if re.search(
            re.escape(supplier_name),
            text,
            re.IGNORECASE
        ):
            supplier = supplier_name
            break

    # -----------------------------
    # Material extraction
    # -----------------------------

    for material_name in MATERIALS:

        if re.search(
            re.escape(material_name),
            text,
            re.IGNORECASE
        ):
            material = material_name
            break

    # -----------------------------
    # Region extraction
    # -----------------------------

    for country in COUNTRIES:

        if re.search(
            re.escape(country),
            text,
            re.IGNORECASE
        ):
            region = country
            break

    # -----------------------------
    # Context-based fallback
    # -----------------------------

    if material == "Unknown":

        lower_text = text.lower()

        if "battery" in lower_text:
            material = "Battery"

        elif "ev" in lower_text:
            material = "Battery"

        elif "mineral" in lower_text:
            material = "Critical Minerals"

    if region == "Unknown":

        lower_text = text.lower()

        if "shanghai" in lower_text:
            region = "China"

        elif "china" in lower_text:
            region = "China"

        elif "europe" in lower_text:
            region = "Europe"

        elif "asia" in lower_text:
            region = "Asia"

        elif "us " in lower_text:
            region = "USA"

    return supplier, material, region
