import dice

def average(method):
    scores = [0] * 21
    attempts = 1000000
    for i in range(attempts):
        stats = method()
        for stat in stats:
            scores[stat] += 1
    print(f'generated stats using {attempts} attempts')
    scores = [x / attempts for x in scores]
    return scores


def total(method):
    totals = [0] * 110
    attempts = 1000000
    for i in range(attempts):
        stats = method()
        totals[sum(stats)] += 1
    print(f'generated stats using {attempts} attempts')
    scores = [x / attempts for x in totals]
    return scores


def roll3d6():
    scores = []
    for i in range(6):
        score = dice.roll() + dice.roll() + dice.roll()
        scores.append(score)
    return scores


def roll4d6droplowest():
    scores = []
    for i in range(6):
        rolls = [dice.roll(), dice.roll(), dice.roll(), dice.roll()]
        rolls.sort()
        score = sum(rolls[1:])
        scores.append(score)
    return scores


def roll3d6pools(pools):
    scores = []
    minimums = [x - 18 for x in pools]
    for i in range(3):
        score = dice.roll() + dice.roll() + dice.roll()
        score = max(score, minimums[i])
        otherscore = pools[i] - score
        scores.append(score)
        scores.append(otherscore)
    return scores