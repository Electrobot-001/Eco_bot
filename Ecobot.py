import random
import discord
from discord.ext import commands
#Ecco le liste
ado_co=["Spegni la luce quando nn sei in una stanza.", "Fai la raccolta diff.", "Nn usare spesso l'IA."]
ado_ca=["Usare troppa energia elettrica spreca acqua e la stessa energia elettrica.", "Riciclare gli oggetti nn riempie le discariche.", "L'IA spreca UN BOTTO di acqua."]
ado_fa=["I vestiti si possono riciclare e diventare di nuovo filato?", "Si può creare del cotone dalle arance? Ed è 100% made-in-Italy.", "Il miele disinfetta le ferite?"]
adu_co=["Spegni la luce quando non sei in una stanza.", "Fai la raccolta differenziata", "Non usare spesso l'Intelligenza Artificiale."]
adu_ca=["Usare troppa energia elettrica spreca acqua e la stessa energia elettrica.", "Fare la raccolta differenziata non riempie le discariche.", "L'Intelligenza Artificiale spreca moltissima acqua."]
adu_fa=["I vestiti si possono riciclare e diventare di nuovo filato.", "Si può creare del cotone dalle arance. Ed è stato fatto per la prima volta in Italia.", "Il miele disinfetta le ferite a causa del suo PH dolce."]
al_co=["Spegni la luce quando non sei in una stanza.", "Fai la raccolta differenziata.", "Non usare spesso l'Intelligenza Artificiale. (se vuoi sapere cos'è copia questo link:https://www.bing.com/search?q=cos%27%C3%A8+l%27ai&form=ANNTH1&refig=6ae24078d4954cc6b7c5e229e7e11575&pc=ACTS)"]
al_ca=["Usare troppa energia elettrica spreca acqua e la stessa energia elettrica.", "Fare la raccolta differenziata non riempie le discariche.", "L'Intelligenza Artificiale spreca moltissima acqua. Anche se è unoi strumento molto utile ai giorni nostri."]
al_fa=["I vestiti si possono riciclare e diventare di nuovo filato.", "Si può creare del cotone dalle arance. Ed è stato fatto per la prima volta in Italia.", "Il miele disinfetta le ferite a causa del suo PH dolce."]
# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='@', intents=intents)


@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')
    print("Ciao, sono un bot che ti darà consigli su come ridurre l'inquinamento! Usa il comando @ecobot e inserisci la tua fascia di età(scegli tra: adolescente, adulto, altro) e lo scopo(scegli tra: consigli, cause, fatti)")

@bot.command()
async def explain(ctx):
    await ctx.send("Ciao, sono un bot che ti darà consigli su come ridurre l'inquinamento! Usa il comando @ecobot e inserisci la tua fascia di età(scegli tra: adolescente, adulto, altro) e lo scopo(scegli tra: consigli, cause, fatti)")

@bot.command()
async def ecobot(ctx, cliente, scopo):
    if cliente=="adolescente":
        if scopo=="consigli":
            random_responce_consiglio_adolescente=ado_co[(random.randint(0,3))]
            await ctx.send(random_responce_consiglio_adolescente+" Se vuoi sapere pk, scrivi cause.")
        elif scopo=="cause":
            random_responce_cause_adolescente=ado_ca[(random.randint(0,3))]
            await ctx.send(random_responce_cause_adolescente+" Se vuoi sapere dei fatti curiosi, scrivi fatti.")
        elif scopo=="fatti":
            random_responce_fatti_adolescente=ado_fa[(random.randint(0,3))]
            await ctx.send("Lo sapevi che... " + random_responce_fatti_adolescente)
    elif cliente=="adulto":
        if scopo=="consigli":
            random_responce_consiglio_adulto=adu_co[(random.randint(0,3))]
            await ctx.send(random_responce_consiglio_adulto+" Se vuoi sapere il perchè di questi consigli, scrivi cause nel secondo parametro.")
        elif scopo=="cause":
            random_responce_cause_adulto=adu_ca[(random.randint(0,3))]
            await ctx.send(random_responce_cause_adulto+" Se vuoi sapere dei fatti curiosi, scrivi fatti nel secondo parametro.")
        elif scopo=="fatti":
            random_responce_fatti_adulto=adu_fa[(random.randint(0,3))]
            await ctx.send("Un fatto curioso: " + random_responce_fatti_adulto)
    elif cliente=="altro":
        if scopo=="consigli":
            random_responce_consiglio_altro=al_co[(random.randint(0,3))]
            await ctx.send(random_responce_consiglio_altro+" Se vuoi sapere il perchè di questi consigli, scrivi cause nel secondo parametro.")
        elif scopo=="cause":
            random_responce_cause_altro=al_ca[(random.randint(0,3))]
            await ctx.send(random_responce_cause_altro+" Se vuoi sapere dei fatti curiosi, scrivi fatti nel secondo parametro.")
        elif scopo=="fatti":
            random_responce_fatti_altro=al_fa[(random.randint(0,3))]
            await ctx.send("Un fatto curioso: " + random_responce_fatti_altro)
    




bot.run("token")
