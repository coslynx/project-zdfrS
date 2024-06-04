import discord
import asyncio
import sqlite3
import requests

from email_verification import verify_email
from captcha_solver import solve_captcha
from logging_system import log_attempt

DATABASE = 'code_database.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

async def redeem_code(code, email, captcha):
    if verify_email(email):
        solved_captcha = solve_captcha(captcha)
        if solved_captcha:
            # Add code redemption logic here
            # Ensure to log successful or failed attempts
            log_attempt(email, code, success=True)
        else:
            log_attempt(email, code, success=False, message="Failed to solve captcha")
    else:
        log_attempt(email, code, success=False, message="Invalid email address")

async def main():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.content.startswith('!redeem'):
            code, email, captcha = message.content.split()[1:]
            await redeem_code(code, email, captcha)

    await client.start('TOKEN')

if __name__ == "__main__":
    asyncio.run(main())