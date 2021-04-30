from instabot import Bot
bot = Bot()
bot.login(username = 'ersul17b',  password = 'reddevil17', use_cookie=False, device='samsung_galaxy_s7')

medias = bot.get_your_medias()

print(medias)
for i in medias:
    print(bot.get_media_comments_all(i))