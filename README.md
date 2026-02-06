# 雲林縣淹水模擬資料前處理 (YL Flood Prediction Data Preprocessing)

本專案用於將颱風降雨資料與淹水模擬數據進行前處理，生成用於深度學習模型 (如 UNet) 的網格化訓練資料。

## 專案結構

- `inputs/`: 輸入資料存放區
  - `t5/flood/`: 莫拉克颱風 (Reference) 的淹水模擬資料，用於取得網格 Metadata 與 Mask。
  - `typhoon_hourly_rain_up_to_2023_OK.xlsx`: 颱風時雨量資料。
  - `CWA_rain_targets_20251126_2323.csv`: 氣象署測站座標資料。
- `sw_data_preprocessing/`: 資料前處理程式碼
  - `preprocess_rain.py`: 將測站降雨資料利用 IDW 內插法轉為網格資料，並對齊淹水網格。
  - `config.py`: 路徑配置與颱風代號對照表。
- `sw_data_all/`: (自動生成) 輸出的處理後資料。

## 環境設定

本專案使用 Python 3.11。請使用以下指令安裝相依套件：

```bash
pip install -r requirements.txt
```

`requirements.txt` 內容包含：
- pandas
- numpy
- pyproj
- openpyxl

## 使用方式

1. **確認輸入資料**：
   確保 `inputs/` 資料夾內已有 `typhoon_hourly_rain_up_to_2023_OK.xlsx` 與 `t5/flood/` 相關參考資料。

2. **執行降雨資料網格化**：
   此步驟會讀取 Excel 中的降雨資料，篩選位於網格內的測站（排除中文名稱測站），並輸出 IDW 內插後的雨量網格 CSV。

   ```bash
   cd sw_data_preprocessing
   python preprocess_rain.py
   ```

3. **輸出結果**：
   處理完成的資料將存放於 `sw_data_all/{tX}/rain/` 目錄下。

## 注意事項

- `preprocess_rain.py` 會自動跳過包含中文字元的測站欄位，僅使用英文或數字編號的測站進行內插。
- 網格範圍與解析度由 `t5` (2009 莫拉克) 的 `metadata.txt` 決定。
