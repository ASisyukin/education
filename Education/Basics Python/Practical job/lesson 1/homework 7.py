start_distance = float(input('Введите дистанцию пробежки в первый день: '))
required_distance = float(input('Введите дистанцию пробежки, которую желаете достигнуть: '))
increase = float(input('Введите значение прироста дистанции пробежки за каждое занятие, в процентах: '))
progress_distance = start_distance
day = 0
while True:
    day += 1
    progress_distance = start_distance * (((increase / 100) + 1) ** (day - 1))
    print(f' Дистанция пробежки в {day}-й день равна {progress_distance:.2f}')
    if progress_distance >= required_distance:
        print(f'Желаемая дистанция пробежки {required_distance} будет достигнута на {day}-й день')
        break
    else:
        continue
