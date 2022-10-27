import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
START, GENDER, AGE, PHOTO, VIDEO, LOCATION, WAYF, FAMILY, MUSIC, HOBBI, BIO = range(
    11)


board = list(map(str, range(1, 10)))


def play_board():
    print('-'*20)
    for i in range(3):
        for j in range(3):
            print(f'{board[j+i*3]:^5}', end=' ')
        print(f"\n{'-'*20}")
    print()


def place_sign(sign):
    global board
    while True:
        request = input(f'Enter position from 1 to 9 for {sign}: ')
        if request.isdigit() and int(request) in range(1, 10):
            request = int(request)
            pos = board[request-1]
            if pos not in (chr(10060), chr(11093)):
                board[request-1] = chr(10060) if sign == "X" else chr(11093)
                break
            else:
                print(f'Already occupied {chr(129335)}')
        else:
            print(f'incorrect value {chr(128581)}')


def check_win():
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win = [board[x[0]]
           for x in win_comb if board[x[0]] == board[x[1]] == board[x[2]]]
    return win[0] if win else win


def game():
    play_board()
    counter = 0
    while True:
        place_sign('0') if counter % 2 else place_sign('X')
        play_board()
        if counter > 3:
            if check_win():
                print(f"{check_win()} Win! {chr(129395)}")
                break
        if counter == 8:
            print(f'Draw {chr(129309)} . Would you like replay?')
            break
        counter += 1


game()

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("5735131343:AAHlO1Ppv0VktsGV4-B8Rhzf3oKPFdlsfPQ")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', hi_command)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            START: [MessageHandler(Filters.text & ~Filters.command, start)],
            GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, age), CommandHandler('skip', skip_age)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            VIDEO: [MessageHandler(Filters.video, video), CommandHandler('skip', skip_video)],
            LOCATION: [
                MessageHandler(Filters.location, location),
                CommandHandler('skip', skip_location),
            ],
            WAYF: [MessageHandler(Filters.text & ~Filters.command, wh_a_y_from), CommandHandler('skip', skip_wh_a_y_from)],
            FAMILY: [MessageHandler(Filters.text & ~Filters.command, family), CommandHandler('skip', skip_family)],
            MUSIC: [MessageHandler(Filters.text & ~Filters.command, music), CommandHandler('skip', skip_music)],
            HOBBI: [MessageHandler(Filters.text & ~Filters.command, hobbi), CommandHandler('skip', skip_hobbi)],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio), CommandHandler('skip', skip_bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()