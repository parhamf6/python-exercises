def parse_file(path: str):
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            lines.append(line)

    return lines
    

diagram_lines = parse_file("Day_7.txt")


def find_beam_spliting_count_v1():
    start_index = (diagram_lines[0]).find("S")
    beams_indexed = [start_index]
    count = 0
    for i in range(1,len(diagram_lines)):
        line = diagram_lines[i]
        line_len = len(line)
        for l in range(line_len):
            if l in beams_indexed:
                if line[l]=="^":
                    beams_indexed.remove(l)
                    count+=1
                    if l<line_len-1 and l>1:
                        if l-1 not in beams_indexed:
                            beams_indexed.append(l-1)
                        if l+1 not in beams_indexed:
                            beams_indexed.append(l+1)
                    elif l==line_len-1:
                        if l-1 not in beams_indexed:
                            beams_indexed.append(l-1)
                    elif l==0:
                        if l+1 not in beams_indexed:
                            beams_indexed.append(l+1)
    return(count)
    
    
def find_beam_spliting_count_v2():
    width = len(diagram_lines[0])
    start_index = diagram_lines[0].find("S")
    ways = [0] * width
    ways[start_index] = 1
    for i in range(1, len(diagram_lines)):
        line = diagram_lines[i]
        next_ways = [0] * width

        for col in range(width):
            way_index = ways[col]
            if way_index == 0:
                continue

            if line[col] == ".":
                # continue straight down
                next_ways[col] += way_index

            elif line[col] == "^":
                if col > 0:
                    next_ways[col - 1] += way_index
                if col < width - 1:
                    next_ways[col + 1] += way_index
        
        ways = next_ways
    return sum(ways)
    
    

v1 = find_beam_spliting_count_v1()
v2 = find_beam_spliting_count_v2()

print(v1, v2)