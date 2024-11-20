import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройки Telegram бота
TOKEN = '7724259783:AAEl9tLTILDhIvShP2JZcxRQEZ8y3sWnTWg'

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Play Ping Pong", web_app=InlineKeyboardButton.web_app_info(url="https://your-domain.com/ping_pong_game.html"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Это игра Пинг-понг. Нажмите кнопку ниже, чтобы начать игру.', reply_markup=reply_markup)

def main():
    # Настройка логирования
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Создание Application и Dispatcher
    application = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
