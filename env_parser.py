import argparse

arguments = argparse.ArgumentParser()
arguments.add_argument('--output_name', action='store', \
    help='name for output your file, default is env.example')

args = arguments.parse_args()

output_name = vars(args)["output_name"]

if output_name:
    output_filename = output_name
else:
    output_filename = "env.example"

def dot_env():
    with open(".env", "r") as f:
        env_data = f.readlines()

    output_file = open(output_filename, "w")
    for line in env_data:
        if line.startswith("#"):
            output_file.write(line)
        elif "=" in line:
            data = line.split("=")[0]
            output_file.write(data+"=")
            output_file.write("\n")
        elif line == "\n":
            output_file.write("\n")
        else:
            output_file.write(line)

    output_file.close()

if __name__ == "__main__":
    dot_env()