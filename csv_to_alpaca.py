import csv
import json

# CSV dosyasının yolu
csv_file_path = "galaFormat.csv"
alpaca_json = []

# CSV dosyasını oku
with open(csv_file_path, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)

    # Her satır için işlemleri yap
    for row in reader:
        # Veriyi parçalara ayır
        data = row[0]  # CSV'de tüm veri tek sütunda olduğu varsayılmış
        if "<s>[INST]" in data:
            # Instruction ve Output'u ayır
            instruction_part = data.split("[INST]")[1].split("[/INST]")[0].strip()
            output_part = data.split("[/INST]")[1].replace("</s>", "").strip()

            # Alpaca formatına uygun bir veri yapısı oluştur
            alpaca_json.append({
                "instruction": instruction_part,
                "input": "",
                "output": output_part
            })

# JSON dosyasına kaydet
with open("alpaca_format.json", "w", encoding="utf-8") as json_file:
    json.dump(alpaca_json, json_file, ensure_ascii=False, indent=4)

print("Alpaca formatına dönüştürüldü ve kaydedildi: alpaca_format.json")
