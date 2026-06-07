import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# fungsi untuk memuat data
def load_data(file_path):
    print(f"Memuat data dari: {file_path}")
    return pd.read_csv(file_path)

# fungsi untuk memproses data
def preprocess_data(df):
    print("Memulai proses preprocessing...")

    # menghapus kolom yang tidak diperlukan
    kolom_dibuang = ['UDI', 'Product ID', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF']
    df_bersih = df.drop(columns=kolom_dibuang)

    # memisahkan Fitur (X) dan Target (y)
    X = df_bersih.drop(columns=['Machine failure'])
    y = df_bersih['Machine failure']

    # melakukan encoding pada kolom 'Type'
    type_mapping = {'L': 0, 'M': 1, 'H': 2}
    X['Type'] = X['Type'].map(type_mapping)

    # melakukan Scaling pada kolom sensor numerik
    kolom_numerik = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    scaler = StandardScaler()
    X[kolom_numerik] = scaler.fit_transform(X[kolom_numerik])

    # menggabungkan kembali data
    df_final = X.copy()
    df_final['Machine failure'] = y

    print("Preprocessing selesai!")
    return df_final

# fungsi untuk menyimpan data hasil proses
def save_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data bersih berhasil disimpan di: {output_path}")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)

    RAW_DATA_PATH = os.path.join(ROOT_DIR, 'ai4i2020_raw', 'ai4i2020.csv')
    PROCESSED_DATA_PATH = os.path.join(ROOT_DIR, 'ai4i2020_preprocessing', 'ai4i2020_processed.csv')

    print("=== Memulai Pipeline Otomatisasi Data ===")
    raw_df = load_data(RAW_DATA_PATH)
    processed_df = preprocess_data(raw_df)
    save_data(processed_df, PROCESSED_DATA_PATH)
    print("=== Pipeline Selesai ===")