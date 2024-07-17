team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


def resultat():
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        return "Победа команды  Мастера кода!"
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        return "Победа команды Волшебники Данных!"
    else:
        return "Ничья!"


print("В команде Мастера кода участников: %(team1_num)s" % {"team1_num": 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !" % {"team1_num": 5, "team2_num": 6})
print("Команда Волшебники данных решила задач: {score_2} !".format(score_2=42))
print("Волшебники данных решили задачи за {team1_time} c !".format(team1_time=18015.2))

print(f"Команды решили {score1} и {score2} задач")
print(f"Результат битвы: {resultat()} ")
print(
    f"Сегогдня было решено {score1 + score2} задач, в среднем по {(team1_time + team2_time) // (score2 + score1)} секунды на задачу!")
