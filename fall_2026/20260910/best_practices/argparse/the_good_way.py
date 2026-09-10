import argparse

parser = argparse.ArgumentParser(
            description='The right way to pass parameters.',
            prog='the_good_way')

parser.add_argument('--file_name',
                    type=str,
                    help='Name of the file',
                    required=True)

parser.add_argument('--column_number',
                    type=str,
                    help='The column number',
                    required=True)

args = parser.parse_args()

print(args.file_name, args.column_number)
