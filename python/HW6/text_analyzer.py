def analyze_file(path):
    with open(path, 'r', encoding='utf-8') as textfile:
        lst = textfile.readlines()
        cnt_str = len(lst)
        word = []
        for str in lst:
            word.extend(str.split())
        cnt_word = len(word)
        long_word = max(word, key=len)
        return f'Количество строк: {cnt_str}, Количество слов: {cnt_word}, Длинное слово: {long_word}'

            

            