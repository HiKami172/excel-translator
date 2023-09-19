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
| Argument          | Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
| `FILEPATH`        | Path to the Excel file.                                                                          |
| `COLUMN_NAME`     | Name of the column to translate.                                                                 |
| `NEW_COLUMN_NAME` | Name of the new column with translations.                                                        |
| `AUTH_KEY`        | Deepl API key. Can be found at https://www.deepl.com/ru/account/summary/                         |
| `TARGET_LANGUAGE` | Deepl code of the target language. Can be found at https://www.deepl.com/docs-api/translate-text |


### Optional Flags

- `--outfile`: Use this flag if you want to specify a different output file. By default, the script will overwrite the original Excel file.