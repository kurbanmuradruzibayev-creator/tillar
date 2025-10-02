import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging sozlamalari
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Lug'at: Inglizcha so'zlar va o'zbekcha tarjimasi
dictionary = {
    'hello': 'salom (o\'zbekcha)',
    'world': 'dunyo',
    'python': 'Python dasturlash tili',
    'learn': 'o\'rganish',
    'bot': 'bot (avtomatlashtirilgan dastur)'
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Botni ishga tushirish buyrug'i"""
    await update.message.reply_text(
        'Assalomu alaykum! Men til o\'rgatuvchi botman. Ingliz tili so\'zlarini o\'rganing!\n'
        '/learn - Yangi so\'z o\'rganish\n'
        'Biror so\'z yuboring, men tushuntiraman!'
    )

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Yangi so'z o'rgatish buyrug'i"""
    example_word = 'hello'
    await update.message.reply_text(
        f"Misol: '{example_word}' inglizcha so\'z '{dictionary[example_word]}' degani.\n"
        'Boshqa so\'zlar uchun ularni yuboring!'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Foydalanuvchi xabariga javob berish"""
    user_message = update.message.text.lower().strip()
    
    if user_message in dictionary:
        await update.message.reply_text(f"'{user_message}' so\'zi: {dictionary[user_message]}")
    else:
        await update.message.reply_text(
            f"'{user_message}' so\'zini topa olmadim. Lug\'atga qo\'shing yoki /learn buyrug\'ini sinab ko\'ring!\n"
            f"Misollar: hello, world, python."
        )

def main() -> None:
    """Asosiy funksiya"""
    # Bot tokenini shu yerga qo'ying
    TOKEN = 'YOUR_TOKEN_HERE'
    
    # Application yaratish
    application = Application.builder().token(TOKEN).build()
    
    # Buyruqlar qo'shish
    application.add_handler(CommandHandler("start", start))
    application
