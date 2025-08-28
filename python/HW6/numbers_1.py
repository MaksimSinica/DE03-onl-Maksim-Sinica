def filter_even_numbers(input_file, output_file):
    with open(input_file,'r') as i_f:
        r = i_f.readlines()
        for i in r:
            if int(i) % 2 == 0:
                with open(output_file, 'a+') as o_f: #Не понял почему при применении w+ в файл пишется только одна строчка, а не набор всех четных
                   o_f.write(i)
                   o_f.seek(0) # Не понимаю почему без этой команды ничего не работает
                   read = o_f.readlines()
    return len(read)
    