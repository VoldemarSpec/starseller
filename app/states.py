from aiogram.fsm.state import State, StatesGroup


class Purchase(StatesGroup):
    chat_id = State()
    amount = State()
    username = State()
    purchase_method = State()
    accepted = State()
    payment_status = State()
