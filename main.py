import telebot
from telebot import types

# Замените на свой токен!
TOKEN = "8438725968:AAGfXvs7jkkq20V5FKk942Lk-G7cvD3s1hc" 

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# --- Обработчики команд ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветствие и выводит главное меню с кнопками"""
    
    # Создаем объект разметки для кнопок
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # Создаем кнопки
    btn_schedule = types.KeyboardButton('Расписание 🗓')
    btn_links = types.KeyboardButton('Важные ссылки 🔗')
    btn_help = types.KeyboardButton('Помощь /help 🆘')
    
    # Добавляем кнопки в разметку
    markup.add(btn_schedule, btn_links, btn_help, )
    
    # Текст приветствия
    welcome_text = (
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Я твой помощник в онлайн-школе.\n"
        "Выбери нужный раздел в меню ниже."
    )
    
    # Отправляем сообщение с кнопками
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=markup
    )


@bot.message_handler(commands=['help'])
def send_help(message):
    """Отправляет список доступных команд"""
    help_text = (
        "Вот что я умею:\n"
        "  /start - Главное меню\n"
        "  /schedule - Узнать расписание\n"
        "  /links - Получить важные ссылки\n"
        "  /help - Показать это сообщение"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    """Отправляет расписание уроков"""
    schedule_text = (
        "📚 Расписание уроков на эту неделю:**\n\n"
        "**Понедельник: Математика (09:00 - 10:00), Литература (10:10 - 11:20), обед (11:30 - 12:20), Русский язык (12:20 - 13:20)\n"
        "Вторник: Физика (09:00 - 10:00), химия (10:10 - 11:20), обед (11:30 - 12:20), История (12:20 - 13.20)\n"
        "Среда: Литература (09:00 - 10:00), география (10:10 - 11:20), обед (11:30 - 12:20), Английский язык (12:20 - 13:20)\n" 
        "Четверг: физкультура (09:00 - 10:00), история (10:10 - 11:20), обед (11:30 - 12:20), обж (12:20 - 13:20)\n" 
        "пятница: Русский язык (09:20 - 10:20), обж (10:30 - 11:20), обед (11:30 - 12:20), труды (12:20 - 13:40)\n" 
        "*(Нажми /start, чтобы вернуться в главное меню)*"
    )
    # Используем 'Markdown' для форматирования текста
    bot.reply_to(message, schedule_text, parse_mode="Markdown")


@bot.message_handler(commands=['links'])
def send_links(message):
    """Отправляет важные ссылки"""
    links_text = (
        "🔗 Важные ссылки:**\n\n"
        "**Платформа обучения: [Перейти к урокам](https://onlineschool.example.com)\n"
        "Общий чат учеников: [Чат в Telegram](https://t.me/school_chat)\n"
        "Техническая поддержка: [Написать в поддержку](mailto:support@school.com)\n"
        "*(Нажми /start, чтобы вернуться в главное меню)*"
    )
    bot.reply_to(message, links_text, parse_mode="Markdown")


# --- Обработчик текстовых сообщений (для кнопок) ---

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Обрабатывает текстовые сообщения, в том числе нажатия кнопок"""
    
    # Приводим текст к нижнему регистру для удобства сравнения
    text = message.text.lower()
    
    if 'расписание' in text:
        send_schedule(message)
    elif 'ссылки' in text:
        send_links(message)
    elif 'помощь' in text or '/help' in text:
        send_help(message)    
    else:
        # Ответ на любое другое текстовое сообщение
        unknown_text = (
            "Я тебя не понял. 🧐\n"
            "Используй команды или кнопки меню.\n"
            "Нажми /start, чтобы увидеть главное меню."
        )
        bot.reply_to(message, unknown_text)

# --- Запуск бота ---

if __name__ == '__main__':
    print("Бот запущен и работает...")
    # Метод infinity_polling() запускает бота в синхронном (неасинхронном) режиме
    # и будет работать, пока вы его не остановите (Ctrl+C).
    bot.infinity_polling()
