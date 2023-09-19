# excel-translator
CLI application for excel translation with deepl.
## Clone Repository
```shell
git clone git@github.com:HiKami172/excel-translator.git
cd excel-translator
```
## Install Requirements
```shell
pip install -r requirements.txt
```
## Usage
To use the script, run the following command in your terminal:
```shell
python excel_translator.py translate_column FILEPATH COLUMN_NAME NEW_COLUMN_NAME AUTH_KEY TARGET_LANGUAGE
```
Where:

- `FILEPATH` is the path to the Excel file you want to translate.
- `COLUMN_NAME` is the name of the column in the Excel file that you want to translate.
- `NEW_COLUMN_NAME` is the name for the new column where the translated text will be stored.
- `AUTH_KEY` is your authentication key for deepl API.
- `TARGET_LANGUAGE` is the deepl code of target language.

### Optional Flags

- `--outfile`: Use this flag if you want to specify a different output file. By default, the script will overwrite the original Excel file.