import pandas as pd
from datasets import Dataset

def generate_and_clean_data(output_csv_path="data/dataset.csv"):
    raw_data = {
        "text": [
            "El motor presenta fugas de aceite en el sello principal",
            "Error de autenticación al intentar iniciar sesión en el software de diagnóstico",
            "La presión hidráulica cae rápidamente durante la operación en carga",
            "No se puede exportar el reporte en formato PDF desde el panel",
            "Ruido inusual y sobrecalentamiento en la bomba hidrostática",
            "Requerimos restablecer la contraseña del usuario administrador"
        ],
        "label": [0, 1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(raw_data)
    # Limpieza básica de caracteres y espacios
    df['text'] = df['text'].str.strip().str.lower()
    df.to_csv(output_csv_path, index=False)
    print(f"Dataset generado y guardado en {output_csv_path}")

if __name__ == "__main__":
    generate_and_clean_data()