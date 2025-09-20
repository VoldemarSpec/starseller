from app.database.models import async_session
from app.database.models import Orders
from sqlalchemy import select, update


async def set_order(chat_id, username, amount, purchase_method, accepted, payment_status):
    async with async_session() as session:
        new_order = Orders(
            chat_id=chat_id,
            uuid="None",
            amount=amount,
            purchase_method=purchase_method,
            is_accepted=accepted,
            payment_status=payment_status,
            username=username
        )
        session.add(new_order)
        await session.commit()
        await session.refresh(new_order)
        return new_order


async def update_payment_status(order_id: int, new_status: str):
    async with async_session() as session:
        stmt = update(Orders).where(Orders.id == order_id).values(payment_status=new_status)
        await session.execute(stmt)
        await session.commit()
        return True


async def get_chat_id(order_id: int):
    async with async_session() as session:
        return await session.scalars(select(Orders).where(Orders.id == order_id))


async def add_uuid(order_id: int, new_status: str):
    async with async_session() as session:
        stmt = update(Orders).where(Orders.id == order_id).values(uuid=new_status)
        await session.execute(stmt)
        await session.commit()
        return True
