import requests

# get input from adventofcode
uri = 'https://adventofcode.com/2021/day/2/input'
response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USERAGENT})
vallist = []

if __name__ == "__main__":       
    val = ""
    for num in response.text:       # put input into list
        if "\n" in num:
            vallist.append(val)
            val = ""
        else:
            val += str(num)

    x = 0
    y = 0

    for elem in vallist:                  # Part 1
        new_val = int(elem[len(elem) - 1])
        if "forward" in elem:
            x += new_val
        elif "up" in elem:
            y -= new_val
        elif "down" in elem:
            y += new_val

    print(f"PART1 = x: {x} * y: {y} = " + str(x * y))

    x = 0
    y = 0
    aim = 0

    for elem in vallist:            # Part 2
        new_val = int(elem[len(elem) - 1])
        if "forward" in elem:
            x += new_val
            y += new_val * aim
        elif "up" in elem:
            aim -= new_val
        elif "down" in elem:
            aim += new_val

    print(f"PART2 = aim: {aim} x: {x} * y: {y} = " + str(x * y))
