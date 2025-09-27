#!/usr/bin/env python3
import argparse

def read_csv(path):

    file = open(path)
    content = file.read()
    file.close()

    return content

def write_json(path, text):

    with open(path, "w") as f:
        f.write(text)

def csv_to_json(lines):

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
    
    return json

def main():

    parser = argparse.ArgumentParser(description="Mini CLI")
    parser.add_argument("input", help="input path of file")
    parser.add_argument("output", help="output path of file")
    args = parser.parse_args()

    lines = read_csv(args.input).splitlines()

    json = csv_to_json(lines)

    write_json(args.output, json)


if __name__ == "__main__":
    main()
