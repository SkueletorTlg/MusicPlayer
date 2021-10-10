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
try:
    import asyncio
    from pyrogram import Client, idle, filters
    import os
    from config import Config
    from utils import mp, USERNAME, FFMPEG_PROCESSES
    from pyrogram.raw import functions, types
    import os
    import sys
    from time import sleep
    from threading import Thread
    from signal import SIGINT
    import subprocess
    
except ModuleNotFoundError:
    import os
    import sys
    import subprocess
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)


CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()
def stop_and_restart():
    bot.stop()
    os.system("git pull")
    sleep(10)
    os.execl(sys.executable, sys.executable, *sys.argv)


bot.run(main())
bot.start()

@bot.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(Config.ADMINS) & (filters.chat(CHAT) | filters.private))
async def restart(client, message):
    await message.reply_text("🔄 Actualizando y reiniciando...")
    await asyncio.sleep(3)
    try:
        await message.delete()
    except:
        pass
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(e)
            pass
        FFMPEG_PROCESSES[CHAT] = ""
    Thread(
        target=stop_and_restart
        ).start()    


bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Revisa si el bot está activo"
            ),
            types.BotCommand(
                command="help",
                description="Muestra el mensaje de ayuda"
            ),
            types.BotCommand(
                command="play",
                description="Reproduce una canción de YT o audio"
            ),
            types.BotCommand(
                command="cplay",
                description="Reproduce archivos de música de un canal.."
            ),
            types.BotCommand(
                command="yplay",
                description="Reproduce archivos de música de una lista de reproducción de YouTube."
            ),
            types.BotCommand(
                command="player",
                description="Muestra la canción que se está reproduciendo actualmente con controles"
            ),
            types.BotCommand(
                command="playlist",
                description="Muestra la playlist"
            ),
            types.BotCommand(
                command="clearplaylist",
                description="Elimina la playlist actual"
            ),
            types.BotCommand(
                command="shuffle",
                description="Reproducir aleatoriamente la playlist"
            ),
            types.BotCommand(
                command="export",
                description="Exporte la playlist actual como archivo json para un uso futuro."
            ),
            types.BotCommand(
                command="import",
                description="Importa una lista de reproducción exportada anteriormente."
            ),
            types.BotCommand(
                command="upload",
                description="Sube la canción que se está reproduciendo como archivo de audio."
            ),
            types.BotCommand(
                command="skip",
                description="Omitir la canción actual"
            ),           
            types.BotCommand(
                command="join",
                description="Ingresar a la llamada"
            ),
            types.BotCommand(
                command="leave",
                description="Salir de la llamada"
            ),
            types.BotCommand(
                command="vc",
                description="Compruebe si VC está iniciado"
            ),
            types.BotCommand(
                command="stop",
                description="Pausa la canción"
            ),
            types.BotCommand(
                command="radio",
                description="Inicia la radio"
            ),
            types.BotCommand(
                command="stopradio",
                description="Detén la radio"
            ),
            types.BotCommand(
                command="replay",
                description="Repetir desde el principio"
            ),
            types.BotCommand(
                command="clean",
                description="Limpia archivos RAW"
            ),
            types.BotCommand(
                command="pause",
                description="Pausa la canción actual"
            ),
            types.BotCommand(
                command="resume",
                description="Reproduce la canción pausada"
            ),
            types.BotCommand(
                command="mute",
                description="Silencia el bot en la llamada"
            ),
            types.BotCommand(
                command="volume",
                description="Ajusta el volumen entre 0-200"
            ),
            types.BotCommand(
                command="unmute",
                description="Activar sonido en la llamada"
            ),
            types.BotCommand(
                command="restart",
                description="Actualiza y reinicia el bot "
            )
        ]
    )
)

idle()
bot.stop()
