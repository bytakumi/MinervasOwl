from platform_client.discord import Discord
import os


def main():
    client_it = Discord(os.environ.get("DISCORD_WEBHOOK_IT"))
    client_it.post("IT系のポスト")

main()
