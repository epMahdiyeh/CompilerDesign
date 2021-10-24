from os import path

input_path = "input.txt"
for char in file:
    with open (file) as in_file:
        with open(path.join(base_path,"%s_tokenized.txt" % file)) as out_file:  #ATTENTION
            for line in in_file:
                words = line.split()
                for word in words:
                out_file.write(word)
                out_file.write("\n")