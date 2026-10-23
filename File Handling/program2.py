def game():
    return 1000

score = game()

with open("File Handling/score.txt") as f:
    hiscore = int(f.read())

if hiscore < score:
    with open("File Handling/score.txt",'w') as f:
        f.write(str(score))