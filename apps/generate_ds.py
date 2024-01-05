import pandas as pd
import numpy as np

def generate_random_dataframe(num_rows):
    # Menghasilkan data acak untuk setiap kolom
    age = np.random.randint(28, 66, num_rows)
    sex = np.random.choice([0.0, 1.0], num_rows)
    cp = np.random.choice([1.0, 2.0, 3.0], num_rows)
    trestbps = np.random.uniform(140, 160, num_rows)
    chol = np.random.uniform(180, 290, num_rows)
    fbs = np.random.choice([0.0, 1.0], num_rows)
    restecg = np.random.choice([0.0], num_rows)  # Menggunakan 0.0 sebagai nilai konstan
    thalach = np.random.uniform(150, 180, num_rows)
    exang = np.random.choice([0.0, 1.0], num_rows)
    oldpeak = np.random.uniform(0.0, 1.0, num_rows)
    # target = np.random.choice([1.0, 2.0, 3.0, 4.0], num_rows)

    # Membuat DataFrame
    data = {'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
            'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
            'oldpeak': oldpeak}

    df = pd.DataFrame(data)
    
    return df


if __name__ == "__main__":
    # Menentukan jumlah baris (misalnya, 20 baris)
    num_rows = 20

    # Menggunakan fungsi untuk membuat DataFrame
    random_df = generate_random_dataframe(num_rows)

    # Menampilkan DataFrame
    print(random_df)