def calculate_streaks(rachas):
    streaks = 0
    previous = rachas[0]

    for index in range(1, len(rachas) - 1):
        if rachas[index] != previous:
            streaks += 1
            previous = rachas[index]

    if rachas[-1] == previous:
        streaks += 1
    else:
        streaks += 2

    return streaks
