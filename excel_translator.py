from concurrent.futures import ThreadPoolExecutor
from functools import partial

import deepl
import fire
import os
import pandas as pd


def translate_text(text, auth_key, source_language, target_language):
    translator = deepl.Translator(auth_key)
    translation = translator.translate_text(
        text,
        source_lang=source_language,
        target_lang=target_language,
    )
    return translation.text


def translate_values(values, auth_key, source_language, target_language):
    translate_function = partial(
        translate_text,
        auth_key=auth_key,
        source_language=source_language,
        target_language=target_language,
    )
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(translate_function, values))

    translations = dict(zip(values, results))
    return translations


def save_to_file(save_path, df):
    excel_file = save_path
    with pd.ExcelWriter(excel_file, engine='openpyxl') as excel_writer:
        df.to_excel(excel_writer, index=False)


def verify_auth_key(auth_key):
    if not auth_key:
        try:
            auth_key = os.environ['DEEPL_API_KEY']
        except KeyError:
            raise fire.core.FireError("No auth key provided.\n"
                                      "Use --auth_key flag or set DEEPL_API_KEY env variable.")

    translator = deepl.Translator(auth_key)
    try:
        translator.translate_text("Hello, world!", target_lang="FR")
    except deepl.DeepLException:
        raise fire.core.FireError(f"Invalid auth key: {auth_key}")
    return auth_key


########################################################################################################################

def translate_column(file, column, auth_key=None, source_language=None,
                     target_language="EN", overwrite=False, outfile=None):
    if not outfile:
        outfile = file
    auth_key = verify_auth_key(auth_key)

    df = pd.read_excel(file)
    values = list(df[column].astype(str).apply(lambda x: x.strip()).unique())
    print(f"Unique values: {len(values)}")

    translations = translate_values(values, auth_key, source_language, target_language)
    new_column = column if overwrite else f"{column}_new"
    df[new_column] = df[column].map(translations)

    save_to_file(outfile, df)
    print(f"Saved to {outfile}")


def translate_columns(file, *columns, auth_key=None, source_language=None,
                      target_language="EN", overwrite=False, outfile=None):
    if not outfile:
        outfile = file
    auth_key = verify_auth_key(auth_key)

    df = pd.read_excel(file)
    values = set()
    for column in columns:
        col_values = list(df[column].astype(str).apply(lambda x: x.strip()).unique())
        values.update(col_values)
    print(f"Unique values: {len(values)}")

    translations = translate_values(values, auth_key, source_language, target_language)
    for column in columns:
        new_column = column if overwrite else f"{column}_new"
        df[new_column] = df[column].map(translations)

    save_to_file(outfile, df)
    print(f"Saved to {outfile}")


########################################################################################################################
if __name__ == '__main__':
    fire.Fire({
        'translate_column': translate_column,
        'translate_columns': translate_columns,
    })
