async def quote(ctx):
  await bot.say(random.choice(open("Quotes.txt").read().splitlines()))
