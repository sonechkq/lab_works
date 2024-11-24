list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_players = len(list_players)
print("Общее количество игроков:", total_players)

# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)
