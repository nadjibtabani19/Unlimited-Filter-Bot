import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# تفعيل تسجيل الأحداث لمساعدتك في تصحيح الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# تعريف وظيفة للتعامل مع أمر البدء ("/start")
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="مرحبًا بك! أنا بوت تيليجرام.")

# تعريف وظيفة للتعامل مع الرسائل النصية
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # استبدال "TOKEN" برمز الوصول الخاص بك الذي حصلت عليه من BotFather في تيليجرام
    updater = Updater(token='TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # تعيين وظيفة التعامل مع أمر البدء ("/start")
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # تعيين وظيفة التعامل مع الرسائل النصية
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # بدء الاستماع على الأحداث الواردة من تيليجرام
    updater.start_polling()

    # استخدم "Ctrl + C" لإيقاف البوت بشكل صحيح
    updater.idle()

if __name__ == '__main__':
    main()
