from main import Wordle


file_path = 'Data/unigram_freq.txt'
wordle = Wordle(file_path=file_path)
result = wordle.words
print(result)

wordle.run()