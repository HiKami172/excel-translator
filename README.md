# excel-translator
CLI application for excel translation with deepl.
## Clone Repository
```shell
git clone git@github.com:HiKami172/excel-translator.git
cd excel-translator
```
## Installation
### Install pip requirements
```shell
pip install -r requirements.txt
```
### Set DeepL API key environment variable
#### Windows Shell:
```shell
$env:DEEPL_API_KEY = <key>
```
#### Linux:
```shell
export DEEPL_API_KEY = <key>
```
The key can be found here: https://www.deepl.com/account/summary/ \
As an alternative, it can be specified as optional argument.
## Usage
To use the script, run the following command in your terminal:
```shell
python excel_translator.py translate_column FILE COLUMN_NAME <flags>
```
Where:
- `FILE` is the path to Excel file.\
- `COLUMN_NAME` is the name of the column to translate.

### Optional Flags


- `--new_column_name`: Name for the new column with translations.
- `--auth_key`: DeepL API key. If not provided, uses DEEPL_API_KEY env variable
- `--outfile`: Output file path. By default, the script will overwrite the original Excel file.
- `--source_language`: Language code for the source language. If not provided, DeepL tries to detect it.
- `--target_language`: Language code for the language you want to translate the text into. English by default

Language codes for DeepL API can be found here: https://www.deepl.com/docs-api/translate-text/