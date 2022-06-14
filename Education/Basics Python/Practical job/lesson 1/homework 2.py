time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

print(f'Заданное время ({time} секунд) приведено к виду часы:минуты:секунды - {hours:02d}:{minutes:02d}:{seconds:02d}')