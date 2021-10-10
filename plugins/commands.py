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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Hola, [{}](tg://user?id={})\n\nSoy un bot que reproduce música en canales y grupos las 24 horas del día, los 7 días de la semana.\n\nIncluso puedo transmitir YouTube en vivo en tu chat de voz.\n\nEscribe /help para conocer todos los comandos disponibles.</b>"
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




@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('🍃 AsA Ecos', url='https://t.me/AsAEcos'),
        InlineKeyboardButton('👤 Soporte', url='https://t.me/DKzippO'),
    ],
    [
        InlineKeyboardButton('👨🏼‍🦯 Ayuda', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
        InlineKeyboardButton('🍃 AsA Ecos', url='https://t.me/AsAEcos'),
        InlineKeyboardButton('👤 Soporte', url='https://t.me/DKzippO'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
