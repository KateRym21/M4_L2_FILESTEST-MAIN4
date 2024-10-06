# напиши код для виконання завдань тут
sum  = 0
with open('my_file.txt','r') as file:
    for string in file:
        string_list = string.map(int.string.split(''))
        string_list = map(int, string_list)
        for symbol in string_list:
            sum+= symbol

print(sum)


with open('my_file.txt','r') as file1:
    lines = file1.readlines()
    line = lines[14].split('')
    item = line[8]
    print(item)