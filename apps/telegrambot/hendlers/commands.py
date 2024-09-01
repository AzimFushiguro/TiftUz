from apps.telegrambot.models import TelegramUser


def start(update, context):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    telegram_id = user.id

    TelegramUser.objects.update_or_create(  # update_or_create bu boradi bor bolsa yangilab qoyadi yoq bolsa yaratadi
        telegram_id=telegram_id,
        defaults={  # defaultsda update ishlaganda qaysi fieldlar upate bolishi kerakligi beriladi
            "last_name": last_name,
            "first_name": first_name
        }
    )
    update.message.reply_text("Hello, Welcome to the bot ")


def help(update, context):
    update.message.reply_text("Yordam")
