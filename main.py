# from utils import read_csv
import argparse
import pathlib

parser = argparse.ArgumentParser(
        description='Preproccess files to match expect card format in Arches')
parser.add_argument(
        '-in', "--input", metavar='str', type=str,
        help='file to be preprocessed')
# parser.add_argument(
#         '--log', default=sys.stdout, type=argparse.FileType('w'),
#         help='the file where the sum should be written')
args = parser.parse_args()


def preprocess(args):
    print(args.input)






if __name__ == "main":
    preprocess(args)
