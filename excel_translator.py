from concurrent.futures import ThreadPoolExecutor
from functools import partial

import deepl
import fire
import pandas as pd


def translate_text(text, auth_key, target_language):
    translator = deepl.Translator(auth_key)
    translation = translator.translate_text(text, target_lang=target_language)
    return translation.text


def save_to_file(save_path, df):
    excel_file = save_path
    with pd.ExcelWriter(excel_file, engine='openpyxl') as excel_writer:
        df.to_excel(excel_writer, index=False)


########################################################################################################################

def translate_column(filepath, column_name, new_column_name, auth_key, target_language, outfile=None):
    if not outfile:
        outfile = filepath

    df = pd.read_excel(filepath)
    print(df.head())
    words = list(df[column_name].astype(str).unique())
    print(f"unique words: {len(words)}")

    translate_function = partial(
        translate_text,
        auth_key=auth_key,
        target_language=target_language,
    )

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(translate_function, words))

    translations = dict(zip(words, results))
    df[new_column_name] = df[column_name].map(translations)
    save_to_file(outfile, df)


########################################################################################################################
if __name__ == '__main__':
    fire.Fire({
        'translate_column': translate_column
    })
