def make_piece(line):
    piece = []
    val = ""
    for i in line:
        if i != ' ':
            val += i
        else:
            piece += [int(val)]
            val = ""
    piece += [int(val)]
    return piece

def parse_input(file):
    file = open(file, "r")
    aux = -1
    set_ = []
    sets = []
    for line in file:
        if len(line) == 2:
            if int(line) == 0:
                break
            else:
                aux = int(line)
        else:
            set_ += [make_piece(line)]
            aux -= 1
            if aux == 0:
                sets += [set_]
                set_ = []
    return sets