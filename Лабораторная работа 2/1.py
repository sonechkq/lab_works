money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_spend = spend

while True:
    budget = money_capital + salary
    if budget >= current_spend:
        months += 1
        money_capital += salary - current_spend
        current_spend *= (1 + increase)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
