# 🔬 Eksperimen_SML_MalifDM — Predictive Maintenance

Repository ini berisi tahap **eksperimen dan otomatisasi preprocessing data** untuk project *predictive maintenance* (prediksi kegagalan mesin), menggunakan dataset **AI4I 2020 Predictive Maintenance**. Preprocessing data dilakukan secara otomatis melalui **GitHub Actions** setiap kali data mentah berubah.

## 📖 Tentang Project

Project ini merupakan tahap awal dari alur *Sistem Machine Learning (SML)*: eksplorasi data mentah, penentuan langkah-langkah preprocessing, lalu pembuatan script otomatisasi (`automate_MalifDM.py`) yang menghasilkan dataset bersih dan siap dipakai untuk pelatihan model.

Alur kerja repo ini:

1. Data mentah (`ai4i2020.csv`) dieksplorasi dan diproses secara manual pada notebook eksperimen.
2. Langkah-langkah preprocessing yang terbukti berhasil dituangkan ke dalam script Python (`automate_MalifDM.py`).
3. GitHub Actions otomatis menjalankan script tersebut setiap kali `ai4i2020_raw/` atau script preprocessing diubah, lalu meng-commit dataset bersih yang baru (`ai4i2020_processed.csv`) kembali ke repository.

## 📂 Struktur Project

```
Eksperimen_SML_MalifDM/
├── .github/workflows/
│   └── automate.yml                    # Workflow GitHub Actions untuk otomatisasi preprocessing
├── ai4i2020_raw/
│   └── ai4i2020.csv                    # Dataset mentah (raw)
├── ai4i2020_preprocessing/
│   └── ai4i2020_processed.csv          # Dataset hasil preprocessing (auto-generated)
└── preprocessing/
    ├── Eksperimen_MalifDM.ipynb        # Notebook eksperimen (EDA & eksplorasi preprocessing)
    └── automate_MalifDM.py             # Script otomatisasi preprocessing
```

## 📊 Dataset

**AI4I 2020 Predictive Maintenance Dataset** dari UCI Machine Learning Repository — berisi data sensor mesin (10.000 baris) yang digunakan untuk memprediksi kegagalan mesin.

Fitur pada data mentah antara lain:
- `Type` — tipe kualitas produk (L/M/H)
- `Air temperature [K]`, `Process temperature [K]` — suhu udara & proses
- `Rotational speed [rpm]`, `Torque [Nm]` — kecepatan rotasi & torsi
- `Tool wear [min]` — durasi keausan alat
- `Machine failure` — target (0 = normal, 1 = gagal)

## ⚙️ Tahapan Preprocessing (`automate_MalifDM.py`)

1. **Menghapus kolom tidak relevan** — `UDI`, `Product ID`, dan kolom mode kegagalan spesifik (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`).
2. **Memisahkan fitur (X) dan target (y)** — target adalah kolom `Machine failure`.
3. **Encoding kolom kategorikal** — `Type` diubah menjadi numerik (`L` → 0, `M` → 1, `H` → 2).
4. **Scaling fitur numerik** — kolom sensor (suhu, kecepatan rotasi, torsi, keausan alat) dinormalisasi menggunakan `StandardScaler`.
5. **Menyimpan hasil** — dataset bersih disimpan ke `ai4i2020_preprocessing/ai4i2020_processed.csv`.

## 🤖 Otomatisasi dengan GitHub Actions

Workflow `automate.yml` akan berjalan otomatis ketika:
- Ada perubahan pada `ai4i2020_raw/**` atau `preprocessing/automate_MalifDM.py` di branch `main`, atau
- Dijalankan manual melalui `workflow_dispatch`.

Workflow ini akan menginstal dependency, menjalankan script preprocessing, lalu meng-commit dan push otomatis dataset hasil olahan ke repository.

## 🛠️ Tech Stack

- **Python 3.12**
- **Pandas** — manipulasi data
- **Scikit-learn** — `StandardScaler` untuk preprocessing
- **Matplotlib** & **Seaborn** — visualisasi (pada tahap eksperimen)
- **GitHub Actions** — otomatisasi pipeline

## ▶️ Menjalankan Secara Lokal

1. **Clone repository**
   ```sh
   git clone https://github.com/alfdmsr/Eksperimen_SML_MalifDM.git
   cd Eksperimen_SML_MalifDM
   ```

2. **Install dependencies**
   ```sh
   pip install pandas scikit-learn
   ```

3. **Jalankan script preprocessing**
   ```sh
   python preprocessing/automate_MalifDM.py
   ```
   Dataset bersih akan dihasilkan di `ai4i2020_preprocessing/ai4i2020_processed.csv`.

4. **(Opsional) Jalankan notebook eksperimen** untuk melihat proses eksplorasi data secara lengkap:
   ```sh
   jupyter notebook preprocessing/Eksperimen_MalifDM.ipynb
   ```

## 🔗 Project Terkait

Dataset hasil preprocessing pada repository ini digunakan sebagai input pada tahap pelatihan model di repository [**Workflow-CI**](https://github.com/alfdmsr/Workflow-CI), yang melakukan training model, tracking dengan MLflow, dan deployment ke Docker Hub.
