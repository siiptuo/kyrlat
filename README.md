<!--
SPDX-FileCopyrightText: 2021 Tuomas Siipola
SPDX-License-Identifier: MIT
-->

# Kyrlat

Python library for romanizing Cyrillic script according to the Finnish SFS 4900
standard:

- Supports Belarusian, Bulgarian, Macedonian, Russian and Ukrainian.
- Handles capitalization (lower case, upper case and all caps) though
  abbreviations are capitalized incorrectly (e.g. "ЧК" is romanized as "TŠK"
  instead of "TšK").
- Removes diacritics used to mark stress (e.g. "Влади́мир" is romanized as
  "Vladimir").
- Handles Unicode equivalence (i.e. both composed and decomposed code points).

## Installation

Yet to be released.

## Usage

```python
import kyrlat
kyrlat.romanize_ru('Влади́мир') # => 'Vladimir'
```

## License

MIT

## Links

- [SFS 4900: Kyrillisten kirjainten translitterointi. Slaavilaiset kielet](https://sales.sfs.fi/fi/index/tuotteet/SFS/SFS/ID2/4/1983.html.stx)
- [Venäjän translitterointi](https://fi.wikipedia.org/wiki/Ven%C3%A4j%C3%A4n_translitterointi) on Wikipedia
- Jukka Korpela: [Venäjän ja muiden slaavilaisten kielten translitterointi](https://jkorpela.fi/iso9.html8)
- [sfs-4900](https://github.com/NatLibFi/sfs-4900): JavaScript implementation
