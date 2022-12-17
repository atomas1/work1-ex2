from random import randint, shuffle


def lottof():
    '''Play Lotto with computer'''
    chosen = []
    for i in range(1, 7):
        while True:
            a = input(f"Podaj liczbę {i}: ")
            try:
                a = int(a)
                if a in range(1, 50) and a not in chosen:
                    chosen.append(a)
                    break
                else:
                    raise Exception("Podaj liczbę z zakresu 1-49 różną od poprzednich!")

            except Exception as e:
                print(e)

    chosen.sort()
    print(f"Wybrane liczby to: {chosen}")
    randomized = list(range(1, 50))
    shuffle(randomized)
    randomized = randomized[:6]
    randomized.sort()
    print(f"Wylosowane liczby to: {randomized}")

    j2 = 0
    won = 0
    for j in chosen:
        if j in randomized:
            won += 1
    print(f"Trafileś {won} liczb.")

if __name__ == '__main__':
    lottof()
