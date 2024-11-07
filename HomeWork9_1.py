def popular_words (text, words):
    dict_words = {}
    text = text.lower()
    word_array = text.split()
    for i in range(len(words)): dict_words[words[i]] = word_array.count(words[i])
    return dict_words

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
