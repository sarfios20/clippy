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


def splitter(text, delimiter, escaper):

    result = []

    pointer = 0

    escaped = False

    buffer = []

    while (pointer < len(text)):

        if(text[pointer] == delimiter and not escaped):
            result.append("".join(buffer))
            buffer.clear()
        elif(text[pointer] != escaper):
            buffer.append(text[pointer])
        else:
            escaped = not escaped
            if (text[pointer-1] == escaper):
                buffer.append(text[pointer])
    
        pointer += 1
    
    result.append("".join(buffer))

    return result


def csv_to_json(lines):

    header = splitter(lines[0], ',', '"')
    lines.pop(0)

    json = ["["]

    for line in lines:

        record = ["{"]

        fields = splitter(line, ',', '"')

        for index, field in enumerate(fields):  

            record.extend(['"', header[index], '"', ':', '"', field, '"', ','])
        
        record.pop()
        record.extend(['}', ','])
        json.extend(record)

    json.pop()
    json.append(']')

    text = "".join(json)
    
    return text

def main():

    # input collection
    parser = argparse.ArgumentParser(description="Mini CLI")
    parser.add_argument("input", help="input path of file")
    parser.add_argument("output", help="output path of file")
    args = parser.parse_args()

    # read file into lines to process
    lines = read_csv(args.input).splitlines()

    # conversion logic
    json = csv_to_json(lines)

    # writting to output
    write_json(args.output, json)


if __name__ == "__main__":
    main()