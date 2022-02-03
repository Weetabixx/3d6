import dice

def average():
    scores = [0] * 21
    attempts = 1000000
    for i in range(attempts):
        stats = rollscores()
        for stat in stats:
            scores[stat] += 1
    print(f'generated stats using {attempts} attempts')
    scores = [x / attempts for x in scores]
    return scores


def rollscores():
    scores = []
    for i in range(6):
        score = dice.roll() + dice.roll() + dice.roll()
        scores.append(score)
    return scores