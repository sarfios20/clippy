#!/usr/bin/env python3
import argparse

def read_csv(path):
    file = open(path)
    content = file.read()
    file.close()

    return content
    

def main():
    parser = argparse.ArgumentParser(description="Mini CLI")
    parser.add_argument("input", help="input path of file")
    parser.add_argument("output", help="output path of file")
    args = parser.parse_args()


    lines = read_csv(args.input).splitlines()
    header = lines[0].split(",")

    lines.pop(0)

    json = "["

    for line in lines:

        json = json + "{"
        fields = line.split(",")

        for index, field in enumerate(fields):  

            json = json + '"'
            json = json + header[index]
            json = json + '"'
            json = json + ": "
            json = json + '"' + field + '"'
            json = json + ", "
        
        json = json[:-2]

        json = json + "},"

    json = json[:-1]
    json = json + "]"

    with open(args.output, "w") as f:
        f.write(json)




if __name__ == "__main__":
    main()
