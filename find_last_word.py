# Загрузка списка слов BIP-39
bip39_wordlist = []
with open("bip39_wordlist.txt") as f:
    bip39_wordlist = f.read().splitlines()

# Функция для проверки мнемонической фразы
def check_mnemonic(mnemonic):
    words = mnemonic.split()
    incorrect_words = []

    for word in words:
        if word not in bip39_wordlist:
            incorrect_words.append(word)

    return incorrect_words

# Ваша мнемоническая фраза
mnemonic_phrase = "top castle bot paper decade arrest rebel property busy game soup until abandon"

# Проверка мнемонической фразы
incorrect_words = check_mnemonic(mnemonic_phrase)

if incorrect_words:
    print("Неправильные слова:", incorrect_words)
else:
    print("Все слова правильные.")
