import argparse
from os import walk, path
from utils.parser import dot_env

arguments = argparse.ArgumentParser()
arguments.add_argument('--output_name', action='store', \
    help='name for output your file, default is env.example')

args = arguments.parse_args()

output_name = vars(args)["output_name"]

configs_file = {".env":dot_env}

if output_name:
    output_filename = output_name
else:
    output_filename = "env.example"

file_paths = []
for (dirpath, dirnames, filenames) in walk('.'):
    for filename in filenames:
        for conf in configs_file:
            if filename.endswith(conf):
                file_paths.append(path.join(dirpath, filename))

for file_path in file_paths:
    directory = file_path.split("/")[:-1]
    fname = file_path.split("/")[-1]
    fname_prefix = ".".join(fname.split(".")[:-1])
    extension = "."+fname.split(".")[-1]

    configs_file[extension](directory, in_path=fname_prefix+extension, \
        out_path=fname_prefix+".example")
