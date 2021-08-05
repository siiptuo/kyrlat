# SPDX-FileCopyrightText: 2021 Tuomas Siipola
# SPDX-License-Identifier: MIT

import re
from functools import partial
import unicodedata

ru_alphabet = set('АЕИОЁУЫЭЮЯБВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪ')
ru_consonants = set('БВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
ru_mapping = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ж': 'Ž',
              'З': 'Z', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
              'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
              'Х': 'H', 'Ц': 'TS', 'Ч': 'TŠ', 'Ш': 'Š', 'Щ': 'ŠTŠ', 'Ъ': '',
              'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'JU', 'Я': 'JA'}

def ru_map(text, i):
    if text[i] == 'Е':
        return 'E' if i > 0 and text[i-1] in ru_consonants else 'JE'
    if text[i] == 'Ё':
        return 'O' if i > 0 and text[i-1] in 'ЖЧШЩ' else 'JO'
    if text[i] == 'И':
        return 'JI' if i > 0 and text[i-1] == 'Ь' else 'I'
    if text[i] == 'Й':
        if i == 0:
            return 'J'
        if text[i-1] == 'И':
            return '' if i == len(text)-1 else 'J'
        return 'I'
    return ru_mapping[text[i]]

uk_alphabet = set('АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯЬ\u02bcЪ')
uk_mapping = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D',
              'Е': 'E', 'Є': 'JE', 'Ж': 'Ž', 'З': 'Z', 'И': 'Y', 'І': 'I',
              'Ї': 'JI', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
              'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
              'Х': 'H\u02bc', 'Ц': 'TS', 'Ч': 'TŠ', 'Ш': 'Š', 'Щ': 'ŠTŠ',
              'Ю': 'JU', 'Я': 'JA', 'Ь': '', '\u02bc': '', 'Ъ': ''}

def uk_map(text, i):
    if text[i] == 'Й':
        if i == 0:
            return 'J'
        if text[i-1] == 'І':
            return '' if i == len(text)-1 else 'J'
        return 'I'
    return uk_mapping[text[i]]

be_alphabet = set('АБВГДЕЁЖЗІЙКЛМНОПРСТУЎФХЦЧШ\u02bcЫЬЭЮЯҐИЪѢ')
be_consonants = set('БВГДЖКЛМНПРСТЎФХЦЧШЬЭҐИЪѢ')
be_mapping = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Д': 'D', 'Ё': 'JO',
              'Ж': 'Ž', 'З': 'Z', 'І': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
              'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
              'У': 'U', 'Ў': 'U', 'Ф': 'F', 'Х': 'H\u02bc', 'Ц': 'TS',
              'Ч': 'TŠ', 'Ш': 'Š', '\u02bc': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
              'Ю': 'JU', 'Я': 'JA', 'Ґ': 'G', 'И': 'I', 'Ъ': ''}

def be_map(text, i):
    if text[i] == 'Е':
        return 'E' if i > 0 and text[i-1] in be_consonants else 'JE'
    if text[i] == 'Й':
        if i == 0:
            return 'J'
        if i == len(text)-1 and text[i-1] == 'І':
            return ''
        return 'I'
    if text[i] == 'Ѣ':
        return 'E' if i > 0 and text[i-1] in be_consonants else 'JE'
    return be_mapping[text[i]]

bg_alphabet = set('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯІЫѢѪ')
bg_mapping = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
              'Ж': 'Ž', 'З': 'Z', 'И': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
              'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
              'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'TS', 'Ч': 'TŠ', 'Ш': 'Š',
              'Щ': 'ŠT', 'Ь': 'J', 'Ю': 'JU', 'Я': 'JA', 'І': 'I', 'Ы': 'Y',
              'Ѣ': 'E', 'Ѫ': 'Ă'}

def bg_map(text, i):
    if text[i] == 'Й':
        return 'J' if i == 0 or text[i-1] == 'И' else 'I'
    if text[i] == 'Ъ':
        return '' if i == len(text) - 1 else 'Ă'
    return bg_mapping[text[i]]

mk_alphabet = set('АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ')
mk_mapping = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ѓ': 'G\u02bc',
              'Е': 'E', 'Ж': 'Ž', 'З': 'Z', 'Ѕ': 'DZ', 'И': 'I', 'Ј': 'J',
              'К': 'K', 'Л': 'L', 'Љ': 'LJ', 'М': 'M', 'Н': 'N', 'Њ': 'NJ',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'Ќ': 'K\u02bc',
              'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Џ': 'DŽ',
              'Ш': 'Š'}

def mk_map(text, i):
    return mk_mapping[text[i]]

def romanize_word(text, alphabet, fn):
    text = text.group(0)
    # Normalize apostrophes to modifier letter apostrophe (U+02BC) which should
    # look identical to right single quotation mark (U+2019) but is considered
    # to be a part of a word instead of punctuation.
    if '\u02bc' in alphabet:
        text = text.replace('\u0027', '\u02bc').replace('\u2019', '\u02bc')
    out = ''
    i = 0
    while i < len(text):
        # Pass through characters outside of the alphabet.
        if text[i].upper() not in alphabet:
            out += text[i]
            i += 1
            continue
        d = fn(text.upper(), i)
        if len(d) == 0:
            i += 1
            continue
        if text[i].isupper():
            if i < len(text)-1 and text[i+1].islower():
                d = d.capitalize()
        else:
            d = d.lower()
        out += d
        i += 1
        # Ignore diacritics used to mark stress. In Cyrillic Unicode characters
        # these diacritics are always separate combining characters.
        while i < len(text) and '\u0300' <= text[i] <= '\u036f':
            i += 1
    return out

def romanize_ru(text):
    '''Romanize Russian text according to SFS 4900.'''
    return re.sub(r'[\w\u0300-\u036f]+', partial(romanize_word, fn=ru_map, alphabet=ru_alphabet), unicodedata.normalize('NFC', text))

def romanize_uk(text):
    '''Romanize Ukrainian text according to SFS 4900.'''
    return re.sub(r'[\w\u0027\u2019\u0300-\u036f]+', partial(romanize_word, fn=uk_map, alphabet=uk_alphabet), unicodedata.normalize('NFC', text))

def romanize_be(text):
    '''Romanize Belarusian text according to SFS 4900.'''
    return re.sub(r'[\w\u0027\u2019\u0300-\u036f]+', partial(romanize_word, fn=be_map, alphabet=be_alphabet), unicodedata.normalize('NFC', text))

def romanize_bg(text):
    '''Romanize Bulgarian text according to SFS 4900.'''
    return re.sub(r'[\w\u0300-\u036f]+', partial(romanize_word, fn=bg_map, alphabet=bg_alphabet), unicodedata.normalize('NFC', text))

def romanize_mk(text):
    '''Romanize Macedonian text according to SFS 4900.'''
    return re.sub(r'[\w\u0300-\u036f]+', partial(romanize_word, fn=mk_map, alphabet=mk_alphabet), unicodedata.normalize('NFC', text))
