#OpenPOI-TR Python tool for extracting brand-based Points of Interest (POI) across Turkiye using OpenStreetMap Overpass API.
#Developed by bootkitt

import requests
import json

# Overpass API endpoint
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# İstanbul sınırları (yaklaşık bounding box: [minlon, minlat, maxlon, maxlat])
ISTANBUL_BBOX = (28.55, 40.80, 29.50, 41.25)

# Kategorilere göre markalar
categories = {
    "petrol": [
        "Shell", "Total", "Türk Petrolleri",
        "Petrol Ofisi", "Opet", "Lukoil", "Kadoil",
        "Sunpet", "Aytemiz", "Moil", "GO -"
    ],
    "market": ["ŞOK", "A101", "BİM", "Migros"],
    "banka": ["Akbank", "Ziraat", "Vakıfbank", "Garanti", "Yapı Kredi", "Halkbank"],
    "telekom": ["Türk Telekom", "Vodafone", "Turkcell", "Millenicom", "Dsmart", "Digiturk", "Turknet"],
    "ptt": ["PTT"],
    "kargo": ["Yurtiçi Kargo", "Aras Kargo", "MNG Kargo", "DHL"]
}

def build_query(bbox, categories):
    minlon, minlat, maxlon, maxlat = bbox
    query = "[out:json][timeout:60];\n("

    for cat, brands in categories.items():
        if cat == "banka":
            # Banka şubeleri
            for brand in brands:
                query += f'  node["amenity"="bank"]["name"="{brand}"]({minlat},{minlon},{maxlat},{maxlon});\n'
            # ATM'ler
            for brand in brands:
                query += f'  node["amenity"="atm"]["operator"="{brand}"]({minlat},{minlon},{maxlat},{maxlon});\n'
        else:
            for brand in brands:
                query += f'  node["brand"="{brand}"]({minlat},{minlon},{maxlat},{maxlon});\n'
                query += f'  node["name"="{brand}"]({minlat},{minlon},{maxlat},{maxlon});\n'

    query += ");\nout body;\n>;out skel qt;"
    return query

def fetch_data():
    query = build_query(ISTANBUL_BBOX, categories)
    response = requests.post(OVERPASS_URL, data={"data": query})
    response.raise_for_status()
    data = response.json()
    return data

def parse_data(data):
    results = []
    for element in data.get("elements", []):
        if element["type"] == "node":
            tags = element.get("tags", {})
            name = tags.get("name") or tags.get("brand") or tags.get("operator")
            if not name:
                continue

            # Tür belirleme
            tur = "diğer"
            for cat, brands in categories.items():
                if any(b.lower() in name.lower() for b in brands):
                    if cat == "banka":
                        if tags.get("amenity") == "atm":
                            tur = "banka_atm"
                        else:
                            tur = "banka"
                    else:
                        tur = cat
                    break

            results.append({
                "bayi_adi": name,
                "enlem": element["lat"],
                "boylam": element["lon"],
                "tur": tur
            })
    return results

def save_to_json(results, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Toplam {len(results)} kayıt kaydedildi -> {filename}")

if __name__ == "__main__":
    data = fetch_data()
    parsed = parse_data(data)
    save_to_json(parsed)
