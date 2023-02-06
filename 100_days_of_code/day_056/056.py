# Day 56: Music Streaming Service
import csv
import os


def normalize_unicode(text: str) -> str:
    """Normalize unicode hyphens and whitespaces."""
    unicode_hyphens = (
        '\u002d', '\u007e', '\u00ad', '\u058a', '\u05be',
        '\u1400', '\u1806', '\u2010', '\u2011', '\u2012',
        '\u2013', '\u2014', '\u2015', '\u2053', '\u207b',
        '\u208b', '\u2212', '\u2e17', '\u2e3a', '\u2e3b',
        '\u301c', '\u3030', '\u30a0', '\ufe31', '\ufe32',
        '\ufe58', '\ufe63', '\uff0d',
    )
    unicode_whitespaces = (
        '\u0020', '\u00a0', '\u1680', '\u180e', '\u2000',
        '\u2001', '\u2002', '\u2003', '\u2004', '\u2005',
        '\u2006', '\u2007', '\u2008', '\u2009', '\u200a',
        '\u200b', '\u202f', '\u205f', '\u3000',
    )

    if isinstance(text, str):
        for i in unicode_hyphens:
            if i in text:
                text = text.replace(i, '-')
        for k in unicode_whitespaces:
            if k in text:
                text = text.replace(k, ' ')
        text = text.strip()
    return text


def main() -> None:
    print('Building ...')
    with open('100MostStreamedSongs.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f'{row}')
            directory = os.listdir()
            artist = normalize_unicode(
                row.get('Artist(s)')).title().replace(' ', '_')
            print(f'{artist = }')
            if artist not in directory:
                os.mkdir(artist)
            song = normalize_unicode(
                row.get('Song')).title().replace(' ', '_')
            song_file = os.path.join(f'{artist}/', song)
            print(f'{song_file} created.')
            # with open(song_file, 'w') as f_out:
            #     pass


if __name__ == '__main__':
    main()
