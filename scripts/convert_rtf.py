"""Converts the data dictionaries in their original rtf format to plain text.

Currently runs in Python 2.7 only, as the dependency `pyth` does not support Python 3.
"""
from pathlib import Path

import click
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter


class _PathParamType(click.ParamType):
    name = 'Path'

    def convert(self, value, param, ctx):
        path = Path(value)
        if not path.exists():
            self.fail('Path "{}" does not exist.'.format(value))
        return path


@click.command(name='datadict-converter')
@click.argument('folder_with_rtfs', type=_PathParamType())
@click.argument('folder_for_text', type=_PathParamType())
def convert_rtf_data_dictionaries(folder_with_rtfs, folder_for_text):
    """Converts PyTUS2000 data dictionaries from rtf to plain text.

    \b
    Parameters:
        folder_with_rtfs: The folder containing the data dictionaries in rich text media format.
        folder_for_text:  The folder into which the converted data dictionaries shall be written
                          to.
    """
    for path in folder_with_rtfs.glob('*.rtf'):
        path_to_text_file = folder_for_text / path.with_suffix('.txt').name
        print('Converting {} to {}...'.format(path, path_to_text_file))
        convert_rtf_to_text(path_to_rtf_file=path, path_to_text_file=path_to_text_file)
    print('All done.')


def convert_rtf_to_text(path_to_rtf_file, path_to_text_file):
    """Converts a Rich Text Media file to a plain text file."""
    with open(path_to_rtf_file.as_posix(), 'r') as rtf_file:
        doc = Rtf15Reader.read(rtf_file)
    with open(path_to_text_file.as_posix(), 'w') as text_file:
        PlaintextWriter.write(doc, target=text_file)


if __name__ == '__main__':
    convert_rtf_data_dictionaries()
