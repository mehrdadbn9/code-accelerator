def count_duplicate_words(filename):
    word_count = {}
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    for word, count in word_count.items():
        if count > 1:
            print(f'کلمه {word}: {count}')

count_duplicate_words('example.txt')