def single_root_words (root_word, *other_words):
    root_word_lower = root_word.lower()
    same_word = []
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_word.append(word)
    return same_word
result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result_1)
print(result_2)

