from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>ππ» Haii Guys! {message.from_user.first_name}!</b>

I am Pemutar Musik!, Kamu Di-Telegram Bisa Mendengarkan Lagu!.

Silahkan Klik Kotak Dibawah Ini, Apabila Kurang Paham Bisa Dibantu Nanti!.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Owner!", url="https://t.me/afterdaytoxic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π¬ Group", url="https://t.me/humangabutguys"
                    ),
                    InlineKeyboardButton(
                        "Channel π", url="https://t.me/captionanakmuda"
                ],
                [
                    InlineKeyboardButton(
                        "Panduanku Buat Bermusik π", url="https://telegra.ph/ππͺπΆπͺ-ππ΄πΎ-03-19"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
