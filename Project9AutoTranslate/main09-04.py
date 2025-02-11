from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"Project9AutoTranslate.txt"
write_file_path = r"Project9AutoTranslate.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='pt')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')