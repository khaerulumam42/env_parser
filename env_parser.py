import argparse
from utils.parser import dot_env

arguments = argparse.ArgumentParser()
arguments.add_argument('--output_name', action='store', \
        help='name for output your file, default is env.example')

args = arguments.parse_args()

output_name = vars(args)["output_name"]

if output_name:
    output_filename = output_name
else:
    output_filename = "env.example"

if __name__ == "__main__":
    dot_env(output_filename)
