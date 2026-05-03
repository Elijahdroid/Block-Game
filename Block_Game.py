file = open("block.in", "r")
N = int(file.readline())
words = file.readlines()
single_letters = []
letters = []
for i in range(0, N):
    for j in range(0, len(words[i])):
        if words[i][j].isalpha():
            if words[i][j] not in single_letters:
                single_letters.append(words[i][j])
    letters.append(single_letters)
    single_letters = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for k in range(0, len(alphabet)):
    for l in range(0, len(letters)):
        for m in range(0, len(letters[l])):
            if letters[l][m] == alphabet[k]:
                letter_count[k] += 1
file2 = open("block.out", "w")
for i in range(0, len(letter_count)):
    file2.writelines(alphabet[i] + ": " + str(letter_count[i]) + "\n")

