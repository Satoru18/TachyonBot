import random
import asyncio
from discord import FFmpegPCMAudio

async def reproducir_musica(message, ruta, nombre, rutas=None, current_key=None, canciones=None):
    if not message.author.voice:
        await message.channel.send("Debes estar en un canal de voz para reproducir música.")
        return
    
    voice_channel = message.author.voice.channel
    voice_client = message.guild.voice_client
    
    if voice_client and voice_client.is_connected():
        pass
    else:
        voice_client = await voice_channel.connect()
    
    if voice_client.is_playing():
        voice_client.stop()
    
    async def after_playing(error):
        if error:
            print(f'Error: {error}')
        else:
            await message.channel.send(f"Canción terminada: {nombre}")
            if rutas and current_key and canciones:
                try:
                    next_key = str(int(current_key) + 1)
                    if next_key in rutas:
                        next_ruta = rutas[next_key]
                        next_nombre = canciones[int(next_key) - 1]
                        await reproducir_musica(message, next_ruta, next_nombre, rutas, next_key, canciones)
                except ValueError:
                    pass
    
    voice_client.play(FFmpegPCMAudio(ruta), after=lambda e: asyncio.run_coroutine_threadsafe(after_playing(e), voice_client.loop))
    await message.channel.send(f"Reproduciendo: {nombre}")

import random
import asyncio # Necesario para el tiempo
import discord

# Agregamos 'message' como argumento para que la función pueda enviar mensajes
async def jujutsu(message):
    personajes = [
        "Satoru Gojo", "Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", 
        "Sukuna", "Kento Nanami", "Toge Inumaki", "Panda", "Maki Zenin", 
        "Aoi Todo", "Mahito", "Yuta Okkotsu", "let's let it all out!"
    ]
            
    # Probabilidades configuradas
    probabilidades = [80, 80, 80, 80, 80, 70, 65, 50, 50, 40, 30, 20, 90]
    personaje = random.choices(personajes, weights=probabilidades, k=1)[0]

    if personaje == "let's let it all out!":
        # 1. Definimos los enlaces directamente
        link1 = "videos/first_jjk.webm" 
        link2 = "https://files.catbox.moe/bgl8up.webm" 
        
        await message.channel.send(" **let's let it all out!** ")
        await asyncio.sleep(2)
        
        # 2. ENVIAR PRIMER ENLACE (Discord lo mostrará como video)
        await message.channel.send(link1)

        # 3. PAUSA DE 10 SEGUNDOS
        await asyncio.sleep(10)
        
        # 4. ENVIAR SEGUNDO ENLACE
        await message.channel.send(link2)
            
        return 

    # Respuesta normal si no sale el especial
    await message.channel.send(f"Te tocó: **{personaje}**")

async def problema_mundial(message):
    problemas = [
        "Contaminación del aire",
        "Cambio climático",
        "Pobreza extrema",
        "Falta de acceso a agua potable",
        "Deforestación masiva",
        "Extinción de especies",
        "Desigualdad social",
        "Crisis de refugiados",
        "Enfermedades infecciosas",
        "Conflictos armados"
    ]
    
    problema = random.choice(problemas)
    await message.channel.send(f"El problema más grande del mundo es: **{problema}**")