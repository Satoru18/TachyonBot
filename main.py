from settings import settings
import discord
from bot_logic import jujutsu, reproducir_musica, problema_mundial

# 1. Configuración de permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sistemas activos. Bot conectado como: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # --- COMANDO DE MÚSICA ---
    if message.content.startswith(".music"):
        canciones = [
            "Shugoshin - The Guardian", "Enamorado Tuyo", "Rule", 
            "Kanjite Kingth", "Gods Only Knows", "Strategy", 
            "The Cruel Angel's Thesis", "Cry for me", "Iris Out", 
            "It's Going Down Now", "Young Girl A"
        ]
        
        menu = "\n".join([f"{i+1}. {c}" for i, c in enumerate(canciones)])
        await message.channel.send(f" **Lista de música:**\n{menu}\n\nSelecciona un número:")

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            seleccion = await client.wait_for('message', check=check, timeout=30.0)
            
            rutas = {
                "1": "songs/shugoshin.mp3",
                "2": "songs/enamorado.mp3",
                "3": "songs/rule.mp4",
                "4": "songs/kanjite.mp3",
                "5": "songs/godsonly.mp3",
                "6": "songs/strategy.mp3",
                "7": "songs/evangelion.mp3",
                "8": "songs/cryforme.mp3",
                "9": "songs/irisout.mp3",
                "10": "songs/igdn.mp3",
                "11": "songs/younggirla.mp3"
            }

            if seleccion.content in rutas:
                await reproducir_musica(message, rutas[seleccion.content], canciones[int(seleccion.content)-1], rutas, seleccion.content, canciones)
            else:
                await message.channel.send("Opción no válida.")
                
        except Exception as e:
            print(f"Error o tiempo agotado: {e}")

    # --- COMANDO PARA DETENER ---
    elif message.content.startswith(".disconnect"):
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
        if voice_client:
            voice_client.stop()
            await voice_client.disconnect()
            await message.channel.send("Bot desconectado")
        else:
            await message.channel.send("No estoy en ningún canal de voz.")

    # --- COMANDO PARA PAUSAR ---
    elif message.content.startswith(".pause"):
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_playing():
            voice_client.pause()
            await message.channel.send("Musica pausada")
        else:
            await message.channel.send("No hay música sonando.")

    # --- COMANDO PARA REANUDAR ---
    elif message.content.startswith(".resume"):
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_paused():
            voice_client.resume()
            await message.channel.send("Música reanudada.")

    

    elif message.content.startswith(".help"):
        await message.channel.send("Comandos disponibles:\n `.music` - Reproducir música\n `.disconnect` - Desconectar bot\n `.pause` - Pausar música\n `.resume` - Reanudar música")

    elif message.content.startswith(".jjk"):
        await jujutsu(message)
        
    elif message.content.startswith(".world"):
        await message.channel.send("El problema mas grande del mundo es la contaminacion mundial")
        await problema_mundial(message)

client.run(settings["TOKEN"])