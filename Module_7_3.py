class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем имена файлов в виде кортежа

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = line.replace(',', '').replace('.', '').replace('=', '').replace('!', '') \
                        .replace('?', '').replace(';', '').replace(':', '').replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        found_positions = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                found_positions[file_name] = words.index(word) + 1
        return found_positions

    def count(self, word):
        word_counts = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            word_counts[file_name] = words.count(word)
        return word_counts

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TeXt'))
print(finder2.count('teXT'))
