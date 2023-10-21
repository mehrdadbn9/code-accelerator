def count_words_and_lines(filename):
    word_count = 0
    line_count = 0
    lines_with_more_than_4_words = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)

            if len(words) > 4:
                lines_with_more_than_4_words += 1

    return word_count, lines_with_more_than_4_words

# نمونه ورودی
filename = "sample.txt"

word_count, lines_with_more_than_4_words = count_words_and_lines(filename)

print("تعداد کلمات:", word_count)
print("تعداد خطوط با بیشتر از 4 کلمه:", lines_with_more_than_4_words)