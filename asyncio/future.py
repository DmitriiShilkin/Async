import asyncio


async def set_after(fut, delay, value):
    #асинхронное ожидание в течение заданного времени
    await asyncio.sleep(delay)

    #устанавливаем значение футуры fut
    fut.set_result(value)


async def main():
    #Получаем объект цикла событий
    loop = asyncio.get_running_loop()

    #Создаем объект футуры при помощи метода create_future()
    fut = loop.create_future()

    # делаем из корутины set_after асинхронную задачу
    # передаем ей в качестве аргумента футуру, задержку и остальные параметры
    # помним что create_task ставит задачу в расписание на выполнение
    loop.create_task(set_after(fut, 1, '... world'))

    print('hello ...')

    # ждем пока футура перейдет в конечное состояние
    print(await fut)


# запуск основной корутины main()
asyncio.run(main())
