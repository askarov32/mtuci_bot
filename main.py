import telebot
from telebot import types
import pandas as pd

bot = telebot.TeleBot('6225751356:AAGc_CgSnlfbcSVOfmcMgCmBYAalLwIX680')
df = pd.read_excel("dd.xlsx")
dff = pd.read_excel("ddd.xlsx")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>! Напиши фамилию преподавателя, и я отправлю тебе информацию о нем.'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    faculty = types.KeyboardButton('Факультеты')
    markup.add(faculty)
    bot.send_message(message.chat.id, 'Также можно ознакомиться с информацией о всех факультетах университета. Для этого нажми кнопку "Факультеты"', reply_markup=markup)

@bot.message_handler(commands=['website'])
def faculty(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://mtuci.ru"))
    bot.send_message(message.chat.id, 'Ссылка на сайт университета', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    a = False

    # КНОПКИ ДЛЯ ФАКУЛЬТЕТОВ

    if message.text == 'Факультеты':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        RIT = types.KeyboardButton('Радио и Телевидение')
        SiSS = types.KeyboardButton('Сети и Системы Связи')
        IT = types.KeyboardButton('Информационные Технологии')
        Kiib = types.KeyboardButton('Кибернетика и Информационная Безопасность')
        Econ = types.KeyboardButton('Цифровая Экономика и Массовые Коммуникации')
        markup.add(RIT, SiSS, IT, Kiib, Econ)
        bot.send_message(message.chat.id, 'Выбери факультет', reply_markup=markup)

    if message.text == 'Радио и Телевидение':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        Admin = types.KeyboardButton('Администрация факультета РиТ')
        Kaf = types.KeyboardButton('Кафедры РиТ')
        History = types.KeyboardButton('История факультета РиТ')
        Back = types.KeyboardButton('Назад')
        markup.add(Admin, Kaf, History, Back)
        bot.send_message(message.chat.id, 'Выбери информацию, которую хочешь узнать', reply_markup=markup)

    if message.text == 'Сети и Системы Связи':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        Info = types.KeyboardButton('')
        Admin = types.KeyboardButton('Администрация факультета СиСС')
        Kaf = types.KeyboardButton('Кафедры СиСС')
        History = types.KeyboardButton('История факультета СиСС')
        Back = types.KeyboardButton('Назад')
        markup.add(Admin, Kaf, History, Back)
        bot.send_message(message.chat.id, 'Выбери информацию, которую хочешь узнать', reply_markup=markup)

    if message.text == 'Информационные Технологии':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        Admin = types.KeyboardButton('Администрация факультета ИТ')
        Kaf = types.KeyboardButton('Кафедры ИТ')
        History = types.KeyboardButton('История факультета ИТ')
        Back = types.KeyboardButton('Назад')
        markup.add(Admin, Kaf, History, Back)
        bot.send_message(message.chat.id, 'Выбери информацию, которую хочешь узнать', reply_markup=markup)

    if message.text == 'Кибернетика и Информационная Безопасность':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        Admin = types.KeyboardButton('Администрация факультета КиИБ')
        Kaf = types.KeyboardButton('Кафедры КиИБ')
        History = types.KeyboardButton('История факультета КиИБ')
        Back = types.KeyboardButton('Назад')
        markup.add(Admin, Kaf, History, Back)
        bot.send_message(message.chat.id, 'Выбери информацию, которую хочешь узнать', reply_markup=markup)

    if message.text == 'Цифровая Экономика и Массовые Коммуникации':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, )
        Admin = types.KeyboardButton('Администрация факультета ЦЭиМК')
        Kaf = types.KeyboardButton('Кафедры ЦЭиМК')
        History = types.KeyboardButton('История факультета ЦЭиМК')
        Back = types.KeyboardButton('Назад')
        markup.add(Admin, Kaf, History, Back)
        bot.send_message(message.chat.id, 'Выбери информацию, которую хочешь узнать', reply_markup=markup)

    # КНОПКА НАЗАД

    if message.text == 'Назад':
        a = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        RIT = types.KeyboardButton('Радио и Телевидение')
        SiSS = types.KeyboardButton('Сети и Системы Связи')
        IT = types.KeyboardButton('Информационные Технологии')
        Kiib = types.KeyboardButton('Кибернетика и Информационная Безопасность')
        Econ = types.KeyboardButton('Цифровая Экономика и Массовые Коммуникации')
        markup.add(RIT, SiSS, IT, Kiib, Econ)
        bot.send_message(message.chat.id, 'Выбери факультет', reply_markup=markup)

    # АДМИНИСТРАЦИИ ФАКУЛЬТЕТОВ

    if message.text == 'Администрация факультета РиТ':
        a = True
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/028/0012.jpg')
        bot.send_message(message.chat.id,
                         'Руководитель Бен Режеб Тауфик Бен Камель\n Декан факультета «Радио и Телевидение»\n Кандидат технических наук, доцент кафедры «Информационная безопасность».\n Email: t.benrejeb@mtuci.ru')
        bot.send_message(message.chat.id, 'Другие сотрудники деканата:')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/334/DSC_9097.jpg')
        bot.send_message(message.chat.id,
                         'Шубина Мария Валерьевна\n Заместитель декана по учебно-воспитательной работе факультета «Радио и Телевидение», старший преподаватель кафедры "Радиотехнические системы", зав. учебных лабораторий каф. РТС, секретарь методического совета МТУСИ\n Email: m.v.shubina@mtuci.ru')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/666/DSC_8752.jpg')
        bot.send_message(message.chat.id,
                         'Фролов Алексей Андреевич\n Заместитель декана по научной работе факультета «Радио и Телевидение», к.т.н. доцент, зам. зав. каф. РТС, ученый секретарь научно-исследовательской части МТУСИ, ученый секретарь научно-технического совета МТУСИк.т.н., доцент\n Email: a.a.frolov@mtuci.ru')

    if message.text == 'Администрация факультета ИТ':
        a = True
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/548/DSC_3949.jpg')
        bot.send_message(message.chat.id,
                         'Городничев Михаил Геннадьевич\n Декан факультета\n Преподаваемые дисциплины\n •	Архитектура вычислительных систем\n •	Интеллектуальные системы\n •	Распределенные программные системы и технологии\n Направление подготовки: 09.03.01 Информатика и вычислительная техника\n Общий стаж работы - 12 лет\n Стаж научно-педагогической работы 7 лет\n Email:  m.g.gorodnichev@mtuci.ru')
        bot.send_message(message.chat.id, 'Другие сотрудники деканата:')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/716/DSC_5204.jpg')
        bot.send_message(message.chat.id,
                         'Манжос Марина Сергеевна\n Ассистент кафедры "Математическая кибернетика и информационные технологии", исполняющий обязанности заместителя декана факультета "Информационные технологии"\n Email:  it@mtuci.ru')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/f4e/DSC_6733.jpg')
        bot.send_message(message.chat.id,
                         'Полянцева Ксения Андреевна\n Старший преподаватель кафедры "Математическая кибернетика и информационные технологии", исполняющий обязанности заместителя декана факультета "Информационные технологии"\n Email:  k.a.poliantseva@mtuci.ru')

    if message.text == 'Администрация факультета КиИБ':
        a = True
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/122/DSC_6280.jpg')
        bot.send_message(message.chat.id,
                         'Иевлев Олег Павлович\n Декан факультета «Кибернетика и информационная безопасность»\n Направления подготовки\n 01.03.04 - Прикладная математика\n 10.03.01, 10.04.01 - Информационная безопасность\n 10.05.02 - Информационная безопасность телекоммуникационных систем\n 15.03.04, 15.04.04 - Автоматизация технологических процессов и производств\n 27.03.04, 27.04.04 - Управление в технических системах\n Общий стаж работы - 32 года\n Стаж научно-педагогической работы - 31 год\n Email:  ievlev@mtuci.ru')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/992/DSC_6309.jpg')
        bot.send_message(message.chat.id,
                         'Безумнов Данил Николаевич\n Старший преподаватель кафедры «Интеллектуальные системы в управлении и автоматизации» (ИСУиА), заместитель декана факультета "Кибернетика и информационная безопасность" (КиИБ) по учебно-воспитательной работе\n Email: d.n.bezumnov@mtuci.ru')

    if message.text == 'Администрация факультета СиСС':
        a = True
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/08e/DSC_6846.jpg')
        bot.send_message(message.chat.id,
                         'Миронов Юрий Борисович\n Декан факультета «Сети и системы связи»\n Email: i.b.mironov@mtuci.ru')
        bot.send_message(message.chat.id, 'Другие сотрудники деканата:')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/b5c/DSC_9010.jpg')
        bot.send_message(message.chat.id,
                         'Воронкова Маргарита Николаевна\n старший преподаватель кафедры НТС , исполняющий обязанности заместителя декана по учебной и воспитательной работе\n Email: vrn@mtuci.ru')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/e0c/WhatsApp-Image-2022_02_22-at-11.44.52.jpeg')
        bot.send_message(message.chat.id,
                         'Степанов Михаил Сергеевич\n Доцент кафедры ССиСК, исполняющий обязанности заместителя декана по научной работе\n Email: m.s.stepanov@mtuci.ru')

    if message.text == 'Администрация факультета ЦЭиМК':
        a = True
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/587/IMG_7101_1_.jpg')
        bot.send_message(message.chat.id,
                         'Гатауллин Сергей Тимурович\n Декан факультета «Цифровая экономика и массовые коммуникации»\n Email: s.t.gataullin@mtuci.ru')
        bot.send_message(message.chat.id, 'Другие сотрудники деканата:')
        bot.send_photo(message.chat.id,
                       'https://mtuci.ru/upload/iblock/237/5jo63wzgvkrttkkula9s8u3b0l0stujh/jIPA84f8ZrQ.jpg')
        bot.send_message(message.chat.id,
                         'Осипов Алексей Викторович\n зам. декана факультета по научной работе, доцент кафедры «Бизнес-информатика»\n Email: a.v.osipov@mtuci.ru')
        bot.send_photo(message.chat.id, 'https://mtuci.ru/upload/iblock/4c4/0016.jpg')
        bot.send_message(message.chat.id,
                         'Фролова Елена Александровна\n зам. декана факультета по учебно-воспитательной работе, ст. преподаватель кафедры «Бизнес-информатика»\n Email: e.a.frolova@mtuci.ru')

    # КАФЕДРЫ ФАКУЛЬТЕТОВ

    if message.text == 'Кафедры РиТ':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Радио и Телевидение']['kafedry'])

    if message.text == 'Кафедры ИТ':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Информационные технологии']['kafedry'])

    if message.text == 'Кафедры КиИБ':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Кибернетика и информационная безопасность']['kafedry'])

    if message.text == 'Кафедры СиСС':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Сети и системы связи']['kafedry'])

    if message.text == 'Кафедры ЦЭиМК':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'оЦЭиМК']['kafedry'])

    # ИСТОРИИ ФАКУЛЬТЕТОВ

    if message.text == 'История факультета РиТ':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Радио и Телевидение']['history'])

    if message.text == 'История факультета ИТ':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Информационные технологии']['history'])

    if message.text == 'История факультета КиИБ':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Кибернетика и информационная безопасность']['history'])

    if message.text == 'История факультета СиСС':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'Сети и системы связи']['history'])

    if message.text == 'История факультета ЦЭиМК':
        a = True
        bot.send_message(message.chat.id, dff.loc[dff['dekanat'] == 'оЦЭиМК']['history'])

    # ПРЕПОДАВАТЕЛИ

    message.text = message.text.lower()

    for prepod in df['name'].unique():
        if message.text == prepod:
            a = True
            o = list(df['Image'].loc[df['name'] == str(message.text)].index)
            if len(o) > 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                d = str(df.iloc[o[0]].loc['Prepod'])
                e = str(df.iloc[o[1]].loc['Prepod'])
                Back = types.KeyboardButton('Назад')
                markup.add(d, e, Back)
                bot.send_message(message.chat.id, f'Я нашел {len(o)} преподавателей. Выбери того, информацию о котором ты хочешь узнать.', reply_markup=markup)

                bot.register_next_step_handler(message, reply_to_user)


            else:
                for index in df['Image'].loc[df['name'] == str(message.text)].index:
                    bot.send_photo(message.chat.id, df['Image'].iloc[index])
                    bot.send_message(message.chat.id,
                                 df['Prepod'].loc[df['name'] == str(message.text)] + '\n' + df['Faculty'].iloc[
                                     index] + '\n' + df['Kafedra'].iloc[
                                     index] + '\n' + df['Dolzhnost'].iloc[
                                     index] + '\n' + df['Stepen'].iloc[
                                     index] + '\n' + df['Contact'].iloc[
                                     index])
    if a == False:
        bot.send_message(message.chat.id, 'Информации о данном преподавателе нет на сайте.')

def reply_to_user(message):
    global df
    bot.send_message(message.chat.id, df.loc[df['Prepod'] == message.text]['Image'])
    bot.send_message(message.chat.id,
                     str(message.text) + '\n' + df.loc[df[
                         'Prepod'] == message.text]['Faculty'] + '\n' + df.loc[df[
                         'Prepod'] == message.text]['Kafedra'] + '\n' + df.loc[df[
                         'Prepod'] == message.text]['Dolzhnost'] + '\n' + df.loc[df[
                         'Prepod'] == message.text]['Stepen'] + '\n' + df.loc[df[
                         'Prepod'] == message.text]['Contact'])





bot.polling(none_stop=True)




