# OpenPOI-TR 🇹🇷

**OpenPOI-TR** is a Python tool that collects **Points of Interest (POI)** for specific brands across Turkey using the **OpenStreetMap Overpass API**. It allows you to fetch locations such as gas stations, markets, banks, ATMs, telecom dealers, PTT offices, and cargo services, then export them to a structured **JSON file**.

*🇹🇷 Türkçe açıklama [aşağıda](#türkçe-açıklama) bulunmaktadır.*

---

## 🚀 Features

- ✅ **Complete Turkey Coverage** - Works across the entire country with adjustable bounding box
- 🏷️ **Brand-based Queries** - Target specific brands within multiple categories  
- 🏦 **Smart Banking Data** - Separate handling for bank branches and ATMs
- 📄 **Clean JSON Output** - Standardized fields for easy integration
- 🗂️ **Multiple Categories** - Comprehensive POI coverage:
  - ⛽ **Petrol Stations** (Shell, BP, Total, etc.)
  - 🛒 **Supermarkets** (Migros, CarrefourSA, A101, etc.)
  - 🏦 **Banks & ATMs** (Ziraat, İş Bankası, Garanti, etc.)
  - 📡 **Telecom Dealers** (Turkcell, Vodafone, Türk Telekom)
  - 📮 **PTT Offices**
  - 📦 **Cargo Services** (Aras, MNG, Yurtiçi, etc.)

## 🛠 Technologies Used

- **Python 3.6+**
- **requests** - HTTP requests to Overpass API
- **json** - Data serialization and handling
- **OpenStreetMap Overpass API** - Primary data source

## 📋 Prerequisites

- Python 3.6 or higher
- Internet connection for API requests
- Basic knowledge of Python (for customization)

## 📌 Installation & Usage

### Option 1: Clone Repository

```bash
# Clone the repository
git clone https://github.com/bootkitt/OpenPOI-TR.git
cd OpenPOI-TR

# Install dependencies
pip install -r requirements.txt

# Run the script
python openpoi_tr.py
```

### Option 2: Download Script Only

```bash
# Download the main script
wget https://raw.githubusercontent.com/bootkitt/OpenPOI-TR/main/openpoi_tr.py

# Install required packages
pip install requests

# Run the script
python openpoi_tr.py
```

## ⚙️ Configuration

You can modify the bounding box coordinates in the script to focus on specific regions:

```python
# Default: All Turkey
TURKEY_BBOX = "35.8,25.6,42.1,44.8"

# Example: Istanbul only  
ISTANBUL_BBOX = "40.8,28.5,41.3,29.3"
```

## 📂 Output Format

The script generates a JSON file with the following structure:

```json
[
  {
    "bayi_adi": "Shell",
    "enlem": 41.015137,
    "boylam": 28.979530,
    "tur": "petrol"
  },
  {
    "bayi_adi": "Ziraat Bankası",
    "enlem": 41.022345,
    "boylam": 28.945678,
    "tur": "banka"
  },
  {
    "bayi_adi": "Migros",
    "enlem": 41.018742,
    "boylam": 28.964521,
    "tur": "market"
  }
]
```

### Field Descriptions

| Field | Description | Type |
|-------|-------------|------|
| `bayi_adi` | Brand/Business name | String |
| `enlem` | Latitude coordinate | Float |
| `boylam` | Longitude coordinate | Float |
| `tur` | Category type | String |

## 🎯 Use Cases

- **Business Intelligence** - Market analysis and competitor mapping
- **Location Planning** - Site selection for new branches/stores
- **Navigation Apps** - POI data integration
- **Research Projects** - Academic studies on retail distribution
- **Mobile Apps** - Location-based services

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contribution
- Add new brand categories
- Improve error handling
- Add data validation
- Create visualization tools
- Add export formats (CSV, Excel)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool uses OpenStreetMap data through the Overpass API. Please respect the [OSM Usage Policy](https://operations.osmfoundation.org/policies/api/) and avoid excessive API requests.

## 🔗 References

- [OpenStreetMap](https://www.openstreetmap.org/) - Open-source map data
- [Overpass API](https://overpass-api.de/) - Query interface for OSM data
- [Overpass QL Documentation](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL)

## ⭐ Support

If you find this project useful, please **give it a star on GitHub**! ⭐

For questions or issues, please [open an issue](https://github.com/bootkitt/OpenPOI-TR/issues) on GitHub.

---

## Türkçe Açıklama

**OpenPOI-TR**, Türkiye genelinde belirli markalara ait **işletme ve hizmet noktalarını (POI – Point of Interest)** **OpenStreetMap Overpass API** üzerinden toplayan bir Python aracıdır. Petrol istasyonları, marketler, bankalar, ATM'ler, telekom bayileri, PTT ve kargo noktalarını sorgulayarak **JSON formatında çıktı** üretir.

### 🚀 Özellikler

- ✅ **Tüm Türkiye Kapsamı** - Ayarlanabilir sınır kutusuyla ülke genelinde çalışır
- 🏷️ **Marka Bazlı Sorgular** - Çoklu kategorilerde belirli markaları hedefler
- 🏦 **Akıllı Bankacılık Verisi** - Banka şubeleri ve ATM'ler ayrı ayrı işlenir
- 📄 **Temiz JSON Çıktısı** - Kolay entegrasyon için standart alanlar
- 🗂️ **Çoklu Kategoriler** - Kapsamlı POI coverage:
  - ⛽ **Petrol İstasyonları** (Shell, BP, Total, vb.)
  - 🛒 **Süpermarketler** (Migros, CarrefourSA, A101, vb.)
  - 🏦 **Bankalar & ATM'ler** (Ziraat, İş Bankası, Garanti, vb.)
  - 📡 **Telekom Bayileri** (Turkcell, Vodafone, Türk Telekom)
  - 📮 **PTT Ofisleri**
  - 📦 **Kargo Servisleri** (Aras, MNG, Yurtiçi, vb.)

### 🛠 Kullanılan Teknolojiler

- **Python 3.6+**
- **requests** - Overpass API'sine HTTP istekleri
- **json** - Veri serileştirme ve işleme
- **OpenStreetMap Overpass API** - Birincil veri kaynağı

### 📌 Kurulum ve Kullanım

```bash
# Repoyu klonlayın
git clone https://github.com/bootkitt/OpenPOI-TR.git
cd OpenPOI-TR

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Betiği çalıştırın
python openpoi_tr.py
```

### 📂 Örnek JSON Çıktısı

```json
[
  {
    "bayi_adi": "Shell",
    "enlem": 41.015137,
    "boylam": 28.979530,
    "tur": "petrol"
  },
  {
    "bayi_adi": "Ziraat Bankası",
    "enlem": 41.022345,
    "boylam": 28.945678,
    "tur": "banka"
  }
]
```

### 🤝 Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Sorun açabilir, özellik önerebilir veya pull request gönderebilirsiniz.

### ⭐ Destek

Bu projeyi faydalı bulduysanız, lütfen **GitHub'da bir yıldız verin**! ⭐

Sorularınız için GitHub'da [issue açın](https://github.com/bootkitt/OpenPOI-TR/issues).

---

<div align="center">
Made with ❤️ for the Turkish OpenStreetMap community
</div>