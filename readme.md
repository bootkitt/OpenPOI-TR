# OpenPOI-TR  

**OpenPOI-TR** is a Python tool that collects **Points of Interest (POI)** for specific brands across Turkey using the **OpenStreetMap Overpass API**.  
It allows you to fetch locations such as gas stations, markets, banks, ATMs, telecom dealers, PTT, and cargo offices, then export them to a structured **JSON file**.  
*(Türkçe açıklama aşağıdadır ⬇️)*

## 🚀 Features  
- Works across the entire Turkey (adjustable bounding box).  
- Brand-based query system for multiple categories.  
- Separate handling of bank branches and ATMs.  
- Clean JSON output with standardized fields.  
- Categories included:  
  - ⛽ Petrol  
  - 🛒 Market  
  - 🏦 Bank & ATM  
  - 📡 Telecom  
  - 📮 PTT  
  - 📦 Cargo  

## 🛠 Technologies Used  
- **Python 3**  
- **requests** – for HTTP requests  
- **json** – for data handling  
- **OpenStreetMap Overpass API** – as the data source  

## ⭐ Support & Contribution  
If you find this project useful, please **give it a star on GitHub**!  
Contributions are always welcome – feel free to open issues, suggest features, or submit pull requests.  

## 📌 Installation & Usage  

```bash
# Clone the repository
git clone https://github.com/bootkitt/OpenPOI-TR.git
cd OpenPOI-TR

# Install dependencies
pip install -r requirements.txt

# Run the script
python openpoi_tr.py

📂 Example JSON Output
[
  {
    "bayi_adi": "Shell",
    "enlem": 41.015137,
    "boylam": 28.979530,
    "tur": "petrol"
  },
  {
    "bayi_adi": "Ziraat",
    "enlem": 41.022345,
    "boylam": 28.945678,
    "tur": "banka"
  }
]

🔗 References

OpenStreetMap https://www.openstreetmap.org/
Overpass API https://overpass-api.de/

---

```markdown
# OpenPOI-TR  

**OpenPOI-TR**, Türkiye genelinde belirli markalara ait **işletme ve hizmet noktalarını (POI – Point of Interest)** **OpenStreetMap Overpass API** üzerinden toplayan bir Python aracıdır.  
Petrol istasyonları, marketler, bankalar, ATM’ler, telekom bayileri, PTT ve kargo noktalarını sorgulayarak **JSON formatında çıktı** üretir.  

## 🚀 Özellikler  
- Tüm Türkiye’de çalışır (bounding box değiştirilebilir).  
- Marka bazlı kategorize edilmiş sorgulama.  
- Banka şubeleri ve ATM’ler ayrı ayrı işlenir.  
- Standart alanlarla temiz JSON çıktısı.  
- Dahil edilen kategoriler:  
  - ⛽ Petrol  
  - 🛒 Market  
  - 🏦 Banka & ATM  
  - 📡 Telekom  
  - 📮 PTT  
  - 📦 Kargo  

## 🛠 Kullanılan Teknolojiler  
- **Python 3**  
- **requests** – HTTP istekleri için  
- **json** – veri işleme için  
- **OpenStreetMap Overpass API** – veri kaynağı  

## ⭐ Destek ve Katkı
Projeyi faydalı bulduysanız, lütfen **GitHub’da bir star verin**!
Katkılar her zaman memnuniyetle karşılanır – sorun açabilir, özellik önerebilir veya pull request gönderebilirsiniz.

## 📌 Kurulum ve Kullanım  

```bash
# Repoyu klonla
git clone https://github.com/yourusername/OpenPOI-TR.git
cd OpenPOI-TR

# Bağımlılıkları yükle
pip install -r requirements.txt

# Betiği çalıştır
python openpoi_tr.py

📂 Örnek JSON Çıktısı
[
  {
    "bayi_adi": "Shell",
    "enlem": 41.015137,
    "boylam": 28.979530,
    "tur": "petrol"
  },
  {
    "bayi_adi": "Ziraat",
    "enlem": 41.022345,
    "boylam": 28.945678,
    "tur": "banka"
  }
]

🔗 Referanslar

OpenStreetMap https://www.openstreetmap.org/
Overpass API https://overpass-api.de/