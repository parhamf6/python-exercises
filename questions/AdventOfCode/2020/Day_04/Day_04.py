import re

def parse_file(file_path):
    passports = []
    passport = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip('\n')

            if line == "":
                passports.append(" ".join(passport))
                passport = []
            else:
                passport.append(line)
        if passport:
            passports.append(" ".join(passport))
    return passports

puzzle_input = parse_file("Day_4.txt")

def check_fields_part1():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for passport in puzzle_input:
        valid_fields = 0
        for f in required_fields:
            if f in passport:
                valid_fields+=1
        if valid_fields==len(required_fields):
            valid_passports+=1
    return valid_passports
    

def check_fields_part2():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for passport in puzzle_input:
        passport_edited = passport.split(" ")
        valid_fields = 0
        for val in passport_edited:
            check_val = val.split(":")
            if check_val[0]=="byr":
                if int(check_val[1])>=1920 and int(check_val[1])<=2002:
                    valid_fields+=1
            if check_val[0]=="iyr":
                if int(check_val[1])>=2010 and int(check_val[1])<=2020:
                    valid_fields+=1
            if check_val[0]=="eyr":
                if int(check_val[1])>=2020 and int(check_val[1])<=2030:
                    valid_fields+=1
            if check_val[0] == "hgt":
                match = re.fullmatch(r"(\d+)(cm|in)", check_val[1])
                if match:
                    value = int(match.group(1))
                    unit = match.group(2)
                    if (unit == "cm" and 150 <= value <= 193) or (unit == "in" and 59 <= value <= 76):
                        valid_fields += 1
            if check_val[0]=="hcl":
                if re.fullmatch(r"#[0-9a-f]{6}", check_val[1]):
                    valid_fields+=1
            if check_val[0]=="ecl":
                if check_val[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    valid_fields+=1
            if check_val[0]=="pid":
                if check_val[1].isdigit() and len(check_val[1])==9:
                    valid_fields+=1
        if valid_fields==len(required_fields):
            valid_passports+=1
    return valid_passports


part1 = check_fields_part1()
part2 = check_fields_part2()

print(part1,part2)