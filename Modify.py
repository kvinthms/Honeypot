class Modify:

    def file_len(self):
        with open(self) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    current = 0
    linecount = file_len("session.json")
    file = open("modsession.json", "w")
    with open("session.json") as infile:
        file.write("[\n")
        for line in infile:
            if current + 1 == linecount:
                newline = line
            else:
                newline = line.rstrip() + ",\n"
            file.write(newline)
            current += 1
        file.write("]")
    infile.close()
    file.close()


