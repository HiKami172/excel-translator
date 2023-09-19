from concurrent.futures import ThreadPoolExecutor
from functools import partial

import deepl
import fire
import os
import pandas as pd


def translate_text(text, auth_key, source_language, target_language):
    translator = deepl.Translator(auth_key)
    translation = translator.translate_text(text, target_lang=target_language)
    return translation.text


def save_to_file(save_path, df):
    excel_file = save_path
    with pd.ExcelWriter(excel_file, engine='openpyxl') as excel_writer:
        df.to_excel(excel_writer, index=False)


########################################################################################################################

def translate_column(file, column_name, new_column_name="Translations", auth_key=None, source_language=None,
                     target_language="EN", outfile=None):
    if not outfile:
        outfile = file

    if not auth_key:
        try:
            auth_key = os.environ['DEEPL_API_KEY']
        except KeyError:
            raise fire.core.FireError("No auth key provided.")

    translate_function = partial(
        translate_text,
        auth_key=auth_key,
        source_language=source_language,
        target_language=target_language,
    )

    df = pd.read_excel(file)
    cells = list(df[column_name].astype(str).apply(lambda x: x.strip()).unique())
    print(f"Unique cells: {len(cells)}")

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(translate_function, cells))

    translations = dict(zip(cells, results))
    df[new_column_name] = df[column_name].map(translations)
    save_to_file(outfile, df)
    print(f"Saved to {outfile}")


########################################################################################################################
if __name__ == '__main__':
    fire.Fire({
        'translate_column': translate_column
    })
