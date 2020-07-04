def dot_env(output_path="env.example", input_path=".env"):
    with open(input_path, "r") as f:
        env_data = f.readlines()

    output_file = open(output_path, "w")
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
