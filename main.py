# from utils import read_csv
import argparse
import pathlib

parser = argparse.ArgumentParser(
        description='Preproccess files to match expect card format in Arches')
parser.add_argument(
        '-in', "--input", metavar='str', type=str,
        help='folder to be preprocessed', default='data')
parser.add_argument(
        '-out', "--output", metavar='str', type=str,
        help='folder to be written to', default='output')

args = parser.parse_args()


def preprocess(args):
    input_folder = pathlib.Path(args.input)
    output_folder = pathlib.Path(args.output)


if __name__ == "main":
    preprocess(args)
