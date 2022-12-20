from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randrange

TOKEN = '2022693630:AAH9X3xvTYYY85er7JC5NA41xSROusxAGIo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

country_to_link = {"Россия": 'https://www.youtube.com/watch?v=79ODF4QJeWc',
                   "США": 'https://www.youtube.com/watch?v=iPbpReERnoc',
                   "Уганда": 'https://www.youtube.com/watch?v=eJeFVVunZlE',
                   "Армения": 'https://www.youtube.com/watch?v=1A4YX1_6LTk',
                   "Украина": 'https://www.youtube.com/watch?v=nybtOIxlku8',
                   "Тайланд": 'https://www.youtube.com/watch?v=DVmkmj8XlVI'}

scryptonite = ['https://www.youtube.com/watch?v=eXLSBdxm_cs', 'https://www.youtube.com/watch?v=V8XsbtoGKtg',
               'https://www.youtube.com/watch?v=dylyj3xObJo', 'https://www.youtube.com/watch?v=kBPu7Elrq1U',
               'https://www.youtube.com/watch?v=m-lyZS-gB_g', 'https://www.youtube.com/watch?v=KCWhKolVDIY',
               'https://www.youtube.com/watch?v=znxvk65wY4E', 'https://www.youtube.com/watch?v=DI0j4rAlBFs']

films = ['Побег из Шоушенка	1994	Фрэнк Дарабонт	драма',
         'Крёстный отец	1972	Фрэнсис Форд Коппола	детектив, драма',
         'Тёмный рыцарь	2008	Кристофер Нолан	боевик, детектив, драма',
         'Крёстный отец 2	1974	Фрэнсис Форд Коппола	детектив, драма',
         '12 разгневанных мужчин	1957	Сидни Люмет	драма, детектив',
         'Список Шиндлера	1993	Стивен Спилберг	драма, биография, исторический фильм',
         'Властелин колец: Возвращение короля	2003	Питер Джексон	фэнтези, приключение, боевик',
         'Криминальное чтиво	1994	Квентин Тарантино	чёрная комедия, драма',
         'Властелин колец: Братство Кольца	2001	Питер Джексон	фэнтези, приключение, боевик',
         'Хороший, плохой, злой	1966	Серджо Леоне	приключение, вестерн',
         'Форрест Гамп	1994	Роберт Земекис	драма, мелодрама',
         'Бойцовский клуб	1999	Дэвид Финчер	драма, триллер, мистический фильм',
         'Начало	2010	Кристофер Нолан	боевик, мистический фильм, научная фантастика',
         'Матрица	1999	Энди и Ларри Вачовски	научная фантастика, боевик, приключение',
         'Жизнь других	2006	Флориан Хенкель фон Доннерсмарк	драма, триллер',
         'Тропы славы	1957	Стэнли Кубрик	драма, детектив, военный фильм',
         'Чужие	1986	Джеймс Кэмерон	фильм ужасов, научная фантастика, боевик',
         'Красота по-американски	1999	Сэм Мендес	драма']


@dp.message_handler(commands=['start', 'menu'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nВот список функций, которые тебе доступны:\n"
                        "/menu - информация о доступных функциях \n"
                        "/stat - получить информацию о чате \n"
                        "/scryptonite - получи рандомный клип скриптонита\n"
                        "/country - выбери страну и получи видео его гимна\n"
                        "/film - получи рекомендацию, какой фильм тебе посмотреть сегодня\n"
                        "/exit - бот покинет чат\n"
                        "/whats_new - новость дня")


@dp.message_handler(commands=['film'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, films[randrange(1000) % len(films)])


@dp.message_handler(commands=['exit'])
async def process_help_command(message: types.Message):
    await bot.leave_chat(message.chat.id)


@dp.message_handler(commands=['whats_new'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, "Бэбры не существует")
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG3NBjncKvxnNEjqoLX4NRxdBeqsPCTgACyRAAAvmKyEs-lPyXrCDQ9SwE')


@dp.message_handler(commands=['scryptonite'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, scryptonite[randrange(1000) % len(scryptonite)])


@dp.message_handler(commands=['stat'])
async def process_help_command(message: types.Message):
    man1 = await bot.get_chat_member_count(message.chat.id)
    man = str(man1)
    adm = await bot.get_chat_administrators(message.chat.id)
    all_amd = []
    for i in adm:
        all_amd.append(i.user.username)
    a = str('\n'.join(all_amd))
    await bot.send_message(message.chat.id,
                           f'Пользователей: {man} \nАдминов: {len(all_amd)} \nСписок админов: {a}')


@dp.message_handler(commands=['country'])
async def process_help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ctr1 = types.KeyboardButton("Россия")
    ctr2 = types.KeyboardButton("США")
    ctr3 = types.KeyboardButton("Уганда")
    ctr4 = types.KeyboardButton("Армения")
    ctr5 = types.KeyboardButton("Украина")
    ctr6 = types.KeyboardButton("Тайланд")
    markup.add(ctr1, ctr2, ctr3, ctr4, ctr5, ctr6)
    await bot.send_message(message.chat.id, 'Выбирай страну', reply_markup=markup)


@dp.message_handler(content_types='text')
async def message_reply(message):
    await bot.send_message(message.chat.id, country_to_link[message.text])


if __name__ == '__main__':
    print('st')
    executor.start_polling(dp)

