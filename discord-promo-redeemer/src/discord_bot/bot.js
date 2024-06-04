const Discord = require('discord.js');
const bot = new Discord.Client();
const config = require('../settings/config');

bot.on('ready', () => {
  console.log(`Logged in as ${bot.user.tag}!`);
});

bot.on('message', async (message) => {
  if (message.content.startsWith(config.prefix)) {
    const args = message.content.slice(config.prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === 'redeem') {
      // Implement promo code redemption logic here
    } else if (command === 'settings') {
      // Implement customizable settings logic here
    }
  }
});

bot.login(config.token);

module.exports = bot;