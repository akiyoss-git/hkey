# -*- coding: utf8 -*-
import vk_api
from vk_api import VkUpload
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType


def write_message(sender, message, attachments=''):
    print(attachments)
    print(authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(), 'attachment': attachments}))


token = "vk1.a.zghiAfyboZX0DSu3hX7eSWH36m2paeiEe4PrljpjI-WmlSA43TpaXR3V-yVBIZOp_NIDr6UIQsMZERppIFps5eDmuu3SJ_4Yu11V-GFj1DvlZjABwYGZysmJS9NTp_PfYsS3aQa2d0Z4H6_Y_FjuHqIV3iFycuhVvoR0VFLYY5Ywa-88rKHdYMj8i5QPZrSssksfRGOH8Q9JKH7ae4on0w"

image_3 = 'photo-182673295_457239148'
image_3_1 = 'photo-182673295_457239147'
image_6 = 'photo-182673295_457239149'
image_8 = 'photo-182673295_457239146'
image_10 = 'photo-182673295_457239145'

authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)

for event in longpoll.listen(): 
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_message = event.text.lower()
        sender = event.user_id

        if reseived_message == 'начать':      #этап 1
            write_message(sender, 'Приветствую тебя, мой дорогой хакер!\n\nВот тебе задание №1:\n\nПереходи по ссылке!\nНайди ответ.\n\nНайди ответ.\n\nhttps://drive.google.com/drive/folders/16jNXjM4Di9SV-jI32J_jdmUm8m1TddCq?usp=sharing')

        elif reseived_message == 'тысяча и одна папка':      #этап 2
            write_message(sender, 'Вот тебе задание №2 😚\n\nПереходи по ссылке и скачай файл для задания!\n\nПопробуй решить эту непростую задачу\n\nhttps://drive.google.com/drive/folders/1vjtFi8FRMsFMFIUDAml3WUx_ODXx2hkW?usp=share_link')

        elif reseived_message == 'назначение':      #этап 3
            write_message(sender, 'Задание №3:\n\nНайди ответ на вопрос, что такое ТЗ?', attachments=str(image_3 + ',' + image_3_1))

        elif reseived_message == 'фраза':      #этап 4
            write_message(sender, 'Задание №4:\n\nРазгадать зашифрованную фразу, используя путеводитель первокурсника\n\nhttps://www.nntu.ru/frontend/web/ngtu/files/studentam/Putevoditel_pervokursnika_NNTU.pdf\n\n4.2.3 27.15.5 59.21.7 4.3.1 48.11.10 7.3.3 3.30.3 14.7.5 23.30.8 42.17.5')

        elif reseived_message == 'последовательность':      #этап 5
            write_message(sender, 'Задание №5:\n\nУкажите последовательность языков, с помощью которой можно добиться изменения текста из “Залог успеха - диплом Политеха” в “Желательно наличие диплома Политехнического университета". Каждый из перечисленных языков можно использовать лишь один раз, помимо русского: русский, тигринья, кечуа, каннада, луганда')

        elif reseived_message == 'найди меня':      #этап 6
            write_message(sender, 'Задание №6:\n\n(56.320468, 44.033610).(56.325664, 44.022497).(56.322749, 44.018635)(56.325629, 44.018913)', attachments=image_6)

        elif reseived_message == 'шифр':      #этап 7
            write_message(sender, 'Задание №7:\n\nРасшифровать фразу "Шмец нашел свое пидег". подсказка: фраза "печенег мандецброд - традиционный рецепт"')

        elif reseived_message == 'кошкомир':      #этап 8
            write_message(sender, 'Задание №8:\n\nhttps://vk.com/world_of_kot\nОтвет: ... - .... .. .. ', attachments=image_8)

        elif reseived_message == 'там где нас любят':      #этап 9
            write_message(sender, 'Задание №9:\n\n_ _ _ _ + _ _ _ _ = 7 _ _ _')
    
        elif reseived_message == 'коллаборация':      #этап 10
            write_message(sender, 'И последнее десятое задание:\n\nНа картинке необходимо найти 7 слов или словосочетаний', attachments=image_10)

            