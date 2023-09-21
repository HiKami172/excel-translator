# excel-translator
CLI application for Excel translation with deepl.
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
### Available Commands
| Command             | Arguments             | Description                |
|---------------------|-----------------------|----------------------------|
| `translate_column`  | `FILE`<br/>`COLUMN`   | Translate one column.      |
| `translate_columns` | `FILE`<br/>`*COLUMNS` | Translate several columns. |


Signature:
```shell
python excel_translator.py translate_column FILE COLUMN <flags>
```
Example:
```shell
python excel_translator.py translate_column "path/to/file.xlsx" "Title" --target RU 
```
Where:
- `FILE` is the path to Excel file.
- `COLUMN` is the name of the column to translate.
- `*COLUMNS` is several column names to translate.

### Optional Flags

- `--auth_key`: DeepL API key. If not provided, uses DEEPL_API_KEY env variable.
- `--overwrite`: Substitute cells' values with translations. 
- `--outfile`: Output file path. By default, the script will overwrite the original Excel file.
- `--source`: Language code for the source language. If not provided, DeepL tries to detect it.
- `--target`: Language code for the language you want to translate the text into. English by default

Language codes for DeepL API can be found here: https://www.deepl.com/docs-api/translate-text/