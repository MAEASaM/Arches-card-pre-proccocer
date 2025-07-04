from utils import read_csv, write_csv
import argparse
import pathlib

parser = argparse.ArgumentParser(
        description='Preproccess files to match expect card format in Arches')
parser.add_argument(
        '-iof', "--input_data_folder", metavar='str', type=str,
        help='folder to be preprocessed', default='data')
parser.add_argument( '-f', "--file", metavar='str', type=str,
        help='file to be preprocessed', default='data.csv')
parser.add_argument(
        '-od', "--output_directory", metavar='str', type=str,
        help='folder to be written to', default='output')

args = parser.parse_args()


def preprocess(args):
    input_data_folder = pathlib.Path(args.input_data_folder)
    output_folder = pathlib.Path(args.output_directory)
    data_file = pathlib.Path(args.file)
    df = read_csv(input_data_folder / data_file)
    output_file = data_file.stem + '_processed.csv'
    write_csv(df, output_folder / output_file)
    print(f"Input folder: {input_data_folder}")
    print(f"{output_folder=}")


if __name__ == "__main__":
    preprocess(args)
