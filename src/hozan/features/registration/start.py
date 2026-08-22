from titan import Router


router = Router()


@router.command("start")
async def start(ctx):
    await ctx.reply(
        "مرحباً بك في Hozan.\n\n"
        "سنبدأ بإنشاء حسابك في المنصة."
    )
