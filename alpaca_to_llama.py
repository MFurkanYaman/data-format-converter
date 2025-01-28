import json
import pandas as pd


def convert_alpaca_to_llama2(input_json_path, output_csv_path):
    """
    Alpaca formatındaki JSON dosyasını Llama 2 formatında CSV'ye dönüştürür.

    Parametreler:
        input_json_path (str): Kaynak Alpaca JSON dosyasının yolu
        output_csv_path (str): Çıktı CSV dosyasının yolu
    """
    # JSON dosyasını oku
    with open(input_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

    # Dönüştürülmüş metinleri saklamak için liste
    converted_texts = []

    # Her veri noktası için Llama 2 formatında metin oluştur
    for item in data:
        instruction = item['instruction']
        output = item['output']

        # Llama 2 formatında metni oluştur
        llama2_format = f"""<s>[INST] {instruction} [/INST] {output}</s>"""

        converted_texts.append(llama2_format)

    # DataFrame oluştur
    df = pd.DataFrame({'Text': converted_texts})

    # CSV olarak kaydet
    df.to_csv(output_csv_path, index=False)

    print(f"Toplam {len(converted_texts)} örnek dönüştürüldü")
    print("\nÖrnek dönüştürülmüş veri:")
    print(converted_texts[0])


if __name__ == "__main__":
    # Dosya yollarını belirle
    input_path = "./dataset/edk-alpaca.v.1.0.json"  # Mevcut Alpaca JSON dosyanız
    output_path = "./dataset/llama2_format.csv"  # Oluşturulacak CSV dosyası

    # Dönüşümü gerçekleştir
    convert_alpaca_to_llama2(input_path, output_path)
