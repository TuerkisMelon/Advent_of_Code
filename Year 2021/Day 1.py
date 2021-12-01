import requests

# get Input from adventofcode
uri = 'https://adventofcode.com/2021/day/1/input'
response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USERAGENT})
vallist = []

if __name__ == "__main__":
    val = ""                        # output in list
    for num in response.text:
        if num.isnumeric():
            val += str(num)
        elif "\n" in num:
            vallist.append(int(val))
            val = ""
        else:
            pass
        
    
    count = 0                       # Part 1
    larger = 0
    smaller = 0
    same = 0
    old_num = 100000

    for num in vallist:            
        num = int(num)
        if old_num < num:               # check if old number is larger than new number
            larger += 1
        elif old_num > num:
            smaller += 1
        else:
            same += 1
        count += 1
        old_num = num
    print(f"PART1= old_num: {old_num} larger: {larger} smaller: {smaller} same: {same} count: {count}")    # printing out the Result

    
    count = 0                   # Part 2
    larger = 0
    smaller = 0
    same = 0
    old_num = 100000
    
    numb = (None, None, None)
    for num in vallist:
        numb = (0, 0, 0)
        num = int(num)
        if count + 3 >= len(vallist):           # check if count is on the end of the list 
            temp = count - len(vallist)
            if temp == -3:      
                numb = (vallist[count], vallist[count + 1], vallist[count + 2])
            elif temp == -2:
                numb = (vallist[count], vallist[count + 1], 0)
            elif temp == -1:
                numb = (vallist[count], 0, 0)
        else:
            numb = (vallist[count], vallist[count + 1], vallist[count + 2])

        if old_num < int(numb[0]) + int(numb[1]) + int(numb[2]):            # check if old number is smaller than new number
            larger += 1
        elif old_num == int(numb[0]) + int(numb[1]) + int(numb[2]):
            same += 1
        elif old_num > int(numb[0]) + int(numb[1]) + int(numb[2]):
            smaller += 1
        old_num = int(numb[0]) + int(numb[1]) + int(numb[2])
        count += 1
    print(f"PART2= larger: {larger} smaller: {smaller} same: {same} count: {count}")
