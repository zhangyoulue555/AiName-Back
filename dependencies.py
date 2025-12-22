from fastapi_mail import FastMail

from core.mail import create_mail_instance


async def get_mail() -> FastMail:
    return create_mail_instance()