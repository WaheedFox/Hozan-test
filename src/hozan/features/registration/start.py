from __future__ import annotations

from titan import Router

from hozan.features.identity import HozanIdentityService


def build_router(identity: HozanIdentityService) -> Router:
    router = Router()

    @router.command("start")
    async def start(ctx):
        account = await identity.get_or_create_account(
            telegram_user_id=ctx.user_id,
            name=ctx.sender.first_name if ctx.sender else "Telegram user",
        )
        identity_item = account.free_identity
        if identity_item is None:
            await ctx.reply("مرحباً بعودتك إلى Hozan.")
            return
        await ctx.reply(
            "مرحباً بك في Hozan.\n\n"
            "تم إنشاء حسابك بنجاح.\n\n"
            f"Hozan ID: {identity_item.value}\n"
            f"Name: {account.name}\n\n"
            "استخدم /assets و /settings لإدارة حسابك."
        )

    return router
