salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_shortfall = 0

current_spend = spend

for month in range(months):
    if salary < current_spend:
        shortfall = current_spend - salary
        total_shortfall += shortfall

    current_spend *= (1 + increase)

required_money_capital = round(total_shortfall)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {required_money_capital} руб.")
