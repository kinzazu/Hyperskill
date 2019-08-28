import random

def start_game():
    choosen = input('Type "play" to play the game, "exit" to quit:')
    if choosen == 'play':
        tt = 8
    else:
        tt = -1
    return tt
def bukva_nomer(origin_list:str,finding_char:str):  #сосет индексы иcкомой буквы
    b =[0]
    for chara in range(len(origin_list)):
        if origin_list.find(finding_char,b[-1]+1) == -1:
            break
        if chara < b[-1]:
            b.append(origin_list.find(finding_char, b[-1] + 1))
        else:
            b.append(origin_list.find(finding_char, chara))
    if len(b) > 1:
        b.remove(0)
    return b
def ubiraem_palku(spryat_slovo:list,naiden_bukva:str,mesta_bukv:list):
    for n in mesta_bukv:
        spryat_slovo.insert(n,naiden_bukva)
        spryat_slovo.pop(n + 1)
    return
def correct_input(bukva:str):
    if len(bukva) > 1:
        print('You should print a single letter')
        return -1
    if  not bukva.isalpha() or not bukva.islower():
        print('It is not an ASCII lowercase letter')
        return -1
    else:
        return 1
guess_words = ['python', 'java', 'kotlin', 'javascript']
hidden_word = random.choice(guess_words)
hidden_bukva = ['-' for n in range(len(hidden_word))]
indexex = []
correct_bukvs = []
wrong_bukvs = []
print('H A N G M A N')
tries = start_game()
while True:
    if tries == -1:
        break
    elif tries == 0:
        print("You are hanged!")
        tries = start_game()
        continue

    a = ''.join(hidden_bukva)
    if a == hidden_word:
        del a
        del hidden_word
        hidden_bukva.clear()
        correct_bukvs.clear()
        wrong_bukvs.clear()
        hidden_word = random.choice(guess_words)
        hidden_bukva = ['-' for n in range(len(hidden_word))]
        print('You survived!')
        tries = start_game()
        continue

    print()
    print(a)
    del a
    letter_input = input('Input a letter:')
    if correct_input(letter_input) == -1 :
        continue

    if letter_input in correct_bukvs or letter_input in wrong_bukvs:
        print('You already typed this letter')
        continue
    elif letter_input not in hidden_word:
        print('No such letter in the word')
        wrong_bukvs.append(letter_input)
        tries -= 1
    elif letter_input in hidden_word:
        correct_bukvs.append(letter_input)
        indexex = bukva_nomer(hidden_word, letter_input)
        ubiraem_palku(hidden_bukva, letter_input, indexex)
