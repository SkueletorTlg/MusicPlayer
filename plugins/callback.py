#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import MessageNotModified
from pyrogram import Client, emoji
from utils import mp, playlist
from config import Config


HELP = """

<b>
Utiliza /play <nombre de la canción> o use /play como respuesta a un archivo de audio o enlace de youtube.

Utilice /yplay para reproducir todas las canciones de una lista de reproducción de YouTube.

También puedes utilizar el comando /cplay <ID de algún canal o @username> para reproducir los audios de ese canal en el chat de voz.

🎶 **Comandos para miembros**:
• **/play**:  Responda a un archivo de audio o enlace de YouTube para reproducirlo o use /play <nombre de la canción>.
• **/player**:  Mostrar la canción que se está reproduciendo actualmente.
• **/upload**: Sube la canción que se está reproduciendo actualmente como archivo de audio.
• **/help**: Mostrar ayuda para los comandos
• **/playlist**: Muestra la lista de reproducción.
🎶 **Admin Commands**:
• **/skip**: Salta la canción actual
• **/cplay**: Reproduce música de los archivos de música de un canal.
• **/yplay**: Reproduce música de una lista de reproducción de YouTube.
• **/join**:  Mete al bot al chat de voz.
• **/leave**:  Saque al bot del chat de voz actual
• **/shuffle**: Lista de reproducción aleatoria.
• **/stop**:  Detiene la música.
• **/radio**: Inicia la Radio.
• **/stopradio**: Detiene la radio.
• **/clearplaylist**: Elimina la playlist
• **/export**: Exporta la lista de reproducción actual para usarla en el futuro.
• **/import**: Importa una lista de reproducción exportada anteriormente.
• **/replay**: Reproduce desde el principio.
• **/clean**: Elimine los archivos RAW PCM no utilizados.
• **/pause**: Pausa la música.
• **/resume**: Reanuda la música
• **/volume**: Establece el nivel de volumen entre 1 a 200
• **/mute**:  Silencia el bot en la llamada
• **/unmute**:  Quita el silencio al bot en la llamada
• **/restart**:  Actualiza y reinicia el Bot.
"""



@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    admins = await mp.get_admins(Config.CHAT)
    if query.from_user.id not in admins and query.data != "help":
        await query.answer(
            "😒 Played Joji.mp3",
            show_alert=True
            )
        return
    else:
        await query.answer()
    if query.data == "replay":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} Playlist vacía"
        else:
            if len(playlist)>=25:
                tplaylist=playlist[:25]
                pl=f"Lista de las primeras 25 canciones del total de {len (lista de reproducción)} canciones.\n"
                pl += f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}"
                    for i, x in enumerate(tplaylist)
                    ])
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}\n"
                    for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(
                    f"{pl}",
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔄", callback_data="Repetir"),
                                InlineKeyboardButton("⏯", callback_data="Pause"),
                                InlineKeyboardButton("⏩", callback_data="Saltar")
                            ],
                        ]
                    )
                )
        except MessageNotModified:
            pass

    elif query.data == "pause":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            if len(playlist)>=25:
                tplaylist=playlist[:25]
                pl=f"Lista de las primeras 25 canciones del total de {len (lista de reproducción)} canciones.\n"
                pl += f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}"
                    for i, x in enumerate(tplaylist)
                    ])
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}\n"
                    for i, x in enumerate(playlist)
                ])

        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl},",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                          [
                                InlineKeyboardButton("🔄", callback_data="Repetir"),
                                InlineKeyboardButton("⏯", callback_data="Pause"),
                                InlineKeyboardButton("⏩", callback_data="Saltar")
                          ],
                    ]
                )
            )
        except MessageNotModified:
            pass
    
    elif query.data == "resume":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            if len(playlist)>=25:
                tplaylist=playlist[:25]
                pl=f"Lista de las primeras 25 canciones del total de {len (lista de reproducción)} canciones.\n"
                pl += f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}"
                    for i, x in enumerate(tplaylist)
                    ])
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}\n"
                    for i, x in enumerate(playlist)
                ])

        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                            [
                                InlineKeyboardButton("🔄", callback_data="Repetir"),
                                InlineKeyboardButton("⏯", callback_data="Pause"),
                                InlineKeyboardButton("⏩", callback_data="Saltar")
                            ],
                    ]
                )
            )
        except MessageNotModified:
            pass

    elif query.data=="skip":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            if len(playlist)>=25:
                tplaylist=playlist[:25]
                pl=f"Lista de las primeras 25 canciones del total de {len (lista de reproducción)} canciones.\n"
                pl += f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}"
                    for i, x in enumerate(tplaylist)
                    ])
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                    f"**{i}**. **🎸{x[1]}**\n   👤**Solicitada por:** {x[4]}\n"
                    for i, x in enumerate(playlist)
                ])

        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                            [
                                InlineKeyboardButton("🔄", callback_data="Repetir"),
                                InlineKeyboardButton("⏯", callback_data="Pause"),
                                InlineKeyboardButton("⏩", callback_data="Saltar")
                            ],
                    ]
                )
            )
        except MessageNotModified:
            pass

    elif query.data=="help":
        buttons = [
            [
              InlineKeyboardButton('🍃 AsA Ecos', url='https://t.me/AsAEcos'),
              InlineKeyboardButton('👤 Soporte', url='https://t.me/DKzippO'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        try:
            await query.edit_message_text(
                HELP,
                reply_markup=reply_markup

            )
        except MessageNotModified:
            pass

