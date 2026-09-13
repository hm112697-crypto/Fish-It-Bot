import os
import discord
import requests

# ================= CONFIGURATION =================
# Anda bisa langsung mengisi text di bawah atau menggunakan Environment Variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "MTU0ODcxNTYyMDg0ODM3ODA1Ng.GuQSQ-.3q3kcsuxtokW0iWdbggdRlCIU3owlzztSjN0Hw")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "1548219437751210044"))

GREEN_API_ID = os.getenv("GREEN_API_ID", "710722735473")
GREEN_API_TOKEN = os.getenv("GREEN_API_TOKEN", "201f297001584d1cb286d3e3efd2d791cc28c682dc6e44e69c")
WA_TARGET_NUMBER = os.getenv("WA_TARGET_NUMBER", "62821273156742") # Gunakan kode negara tanpa tanda +
# =================================================

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def send_to_whatsapp(text):
    url = f"https://green-api.com{GREEN_API_ID}/sendMessage/{GREEN_API_TOKEN}"
    payload = {
        "chatId": f"{WA_TARGET_NUMBER}@c.us",
        "message": text
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Pesan berhasil diteruskan ke WhatsApp.")
        else:
            print(f"Gagal mengirim ke WA: {response.text}")
    except Exception as e:
        print(f"Terjadi kesalahan saat kirim WA: {e}")

@client.event
async def on_ready():
    print(f'Bot Discord aktif sebagai {client.user}')

@client.event
async def on_message(message):
    # Mengabaikan pesan dari bot itu sendiri
    if message.author == client.user:
        return
        
    # Hanya membaca pesan dari channel spesifik yang ditentukan
    if message.channel.id == DISCORD_CHANNEL_ID:
        format_pesan = f"*[Pesan Baru dari Discord]*\n\n*Pengirim:* {message.author.name}\n*Isi:* {message.content}"
        print(f"Mendeteksi pesan dari {message.author.name}, meneruskan...")
        send_to_whatsapp(format_pesan)

client.run(DISCORD_TOKEN)
