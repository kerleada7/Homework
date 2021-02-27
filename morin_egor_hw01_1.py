''''
1.	Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a.	до минуты: <s> сек;
b.	до часа: <m> мин <s> сек;
c.	до суток: <h> час <m> мин <s> сек;
d.	* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

try:
    #Константы времени
    CONST_MIN = 60
    CONST_HOUR = CONST_MIN**2
    CONST_DAY = 24*CONST_HOUR

    #Заготовка строки вывода
    representation_duration = 'Продолжительность времени: '

    #запросим количество секунд
    duration_input = input('Введите время в секундах: \n')

    #конвертируем строку в число
    duration_sec = int(duration_input)

    #получаем сколько дней в веденых секундах
    day_duration = duration_sec // CONST_DAY
    #Если получилось выделить количество дней, вычтим из общего количества секунд и добавим в заготовку
    if day_duration > 0:
        duration_sec = duration_sec - day_duration * CONST_DAY
        representation_duration = representation_duration + str(day_duration) + ' дн '

    # получаем сколько часов в веденых секундах
    hour_duration = duration_sec // CONST_HOUR
    # Если получилось выделить количество часов, вычтим из общего количества секунд и добавим в заготовку
    if hour_duration > 0:
        duration_sec = duration_sec - hour_duration * CONST_HOUR
        representation_duration = representation_duration + str(hour_duration) + ' час '

    # получаем сколько минут в веденых секундах
    min_duration = duration_sec // CONST_MIN
    # Если получилось выделить количество минут, вычтим из общего количества секунд и добавим в заготовку
    if min_duration > 0:
        duration_sec = duration_sec - min_duration * CONST_MIN
        representation_duration = representation_duration + str(min_duration) + ' мин '

    representation_duration = representation_duration + str(duration_sec) + ' сек'

    #Вывод представления промежуток времени
    print(representation_duration)

except:
    print('Введены не корректные данные. Секунды указываются числом')
