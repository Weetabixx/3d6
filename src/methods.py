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