def popular_words (text, words):
    text = text.lower()
    word_array = text.split()
    print(word_array)
    dict_words = {}


    for i in range(len(words)):
        if words[i] in dict_words:
        dict_words[words[i]] = text.count(words[i])


    return dict_words
print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
#assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 1 }, 'Test1'
print('OK')