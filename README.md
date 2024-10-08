# client-server_application

|**Ветвь**|**Содержимое**|
|---------|--------------|
|main|Версия с мониторингом|
|SQL|Все про БД|

-----------------

# Введение

*«Реализовав»* [мониторинг по клавиатурному почерку](https://github.com/DerbiLow/Authentication-by-keyboard-handwriting) и [Steam-парсер с БД](https://github.com/DerbiLow/Steam-Parser) появилась идея освоить Python, SQL и клиент-серверную архитектуру. С появлением второго ПК реализация этой идеи стала возможна.

# Суть 

Логирование  — это процесс формирования логов, а именно: фиксация и структурирование информации о работе системы в отдельные лог-файлы/базы данных с возможностью быстрого доступа к ним в случае необходимости.<br>
В качестве клиента, с которого будут собираться логи, будет задействован первый ПК. На нем при помощи бесконечного цикла и Py-библиотек будет собираться данные: загрузка дисков, процент использования процессора/ядер, процент использования оперативной памяти/памяти подкачки, температура, процент загрузки, процент использования видеокарты. Учитывая, что при нагрузке компьютер стал активно выдавать фризы, система мониторинга/логирования должна помочь выявить причину.

Второй ПК будет использоваться, как сервер, на котором будет обрабатываться полученная информация, храниться в БД.

# Клиентская часть

В начале работы происходит подключение к серверу, чтобы избежать возможного подключения ни к тому хосту, оба компьютера проходят процесс идентификации, обмениваясь основной технической информацией и проверяя ее. <br>
Каждое сообщение проходит через простейшую функцию шифровки/дешифровки, чтобы в канале связи не «гуляли» числа и важная информация.<br>

Параметры собираются ежесекундно.<br> 
Результат собранных параметров выглядит так: **2024-07-27 18:56:53.183_22.5_14.5_10.8_1.5_7.7_0.0_4.7_1.5_4.7_0.0_2.4_0.0_29.3_0.0_38.0_0.0_** <br>
Расшифровка: **time_C:_D:_core1_core2_core3_core4_core5_core6_core7_core8_CPU_RAM_VRAM_GPU_load_GPU_temp_GPU_ram_**

Для включения мониторинга или взаимодействия с БД реализовано ветвление, которое сейчас не работает :)

# Серверная часть

БД - MS SQL, находится на втором ПК. Подключение между Py-сервером и MS SQL локальное.

В начале работы сервер ждет подключения клиента, после подключается к БД. Оба компьютера проходят процесс идентификации, обмениваясь основной технической информацией и проверяя ее.<br>

Все необходимые переменные очищаются перед началом работы программы. Каждую секунду шифрованные строки, содержащие информацию попадают на сервер. Сервер дешифрует их и парсит на переменные, которые записываются в массивы. При достижении 60 секунд начинается процесс проверки переменных и запись их в базу данных.

При проверке ищутся критические параметры работы компьютера, в случае обнаружения формируется сообщение, содержащее время и проблемный параметр, который тоже записывается в отдельную ячейку для анализа.

|**Параметр**|**Критическое значение**|**Описание проблемы**|
|---------|--------------|-----------------|
| Диск C: (D:) | Более 75%| При перегрузе дисков, замедляется скорость обработки информации|
|Ядра (процессор), видеокарта|100 % --> 30 % --> 100%| Тротлинг, вероятнее всего из-за перегрева|
|Оперативная память <br> Память подкачки <br> Видеопамять| Более 85% |  При перегрузе «быстрой» памяти, замедляется скорость обработки информации|
|Температура видеокарты | Более 88°С| Тротлинг из-за перегрева|

После идет процесс очистки переменных и сбор информации повторяется

# Пример работы программы

Таблица после создания<br>
![Снимок2](https://github.com/user-attachments/assets/992b4d1c-40d4-4a5c-806f-701f1ec22ea1)

Процесс сбора информации<br>
![Снимок1](https://github.com/user-attachments/assets/e8d2af21-76d8-44c1-b3a1-3817deea37b8)
![Снимок](https://github.com/user-attachments/assets/e1cd1e3d-070b-4eae-b6f4-ceca29013cdb)<br>
![Снимок3](https://github.com/user-attachments/assets/2b4df12d-0d34-4edd-b720-5cae711bd6b9)<br>

Процесс обработки информации и записи ее в БД<br>
![Снимок4](https://github.com/user-attachments/assets/24cbc5e2-2ecd-44b6-b3f4-a16568cf1931)

Информация в БД<br>
![Снимок5](https://github.com/user-attachments/assets/fa744478-8261-493f-b0da-6cf1a5b7e542)

Пример критического сообщения<br>
![Снимок6](https://github.com/user-attachments/assets/6fb0bcde-b632-45b5-ac6c-3a6a493e4da9)


# Техническая информация

Скрипт создания таблицы - SQLQuery1.sql<br>
Клиентская часть - logger1.py<br>
Серверная часть - logger_server.py
