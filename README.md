# 🌟 StarsSellerBot

**StarBot** is a Telegram bot for buying and sending "stars" via **Fragment**.
It is both a pet project and a working service, designed for experimenting with bots, microtransactions, and cryptocurrency payments.

The bot is built with **asyncio** and uses **SQLite** via **SQLAlchemy ORM** (`sqlite+aiosqlite`) to store information about clients and their orders.
Star purchases are processed through an unofficial **Fragment API** using **aiohttp**. Payments can be made with cryptocurrency through **Crypto Cloud**, and exchange rates from UAH to USD are retrieved via **PrivatBank API**.

---

## ⚙️ Installation & Running

```bash
# Clone the repository
git clone https://github.com/VoldemarSpec/starseller.git
cd repository

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

---

## 🛠 Technologies

* Python (asyncio)
* Telegram Bot API
* SQLite + SQLAlchemy ORM (sqlite+aiosqlite)
* aiohttp
* Fragment (unofficial API)
* Crypto Cloud
* PrivatBank API
* dotenv

---

## 📖 Usage

1. Start the bot in Telegram (`/start`).

2. Choose an action from the menu:

   * **Buy Stars ⭐** – select the number of stars and enter the recipient's username.
   * **Price 💲** – see the current price of a star in different currencies.
   * **Support** – contact the admin via email.
   * **How it works 🛠️** – view the step-by-step buying process.
   * **Privacy Policy** – view privacy rules and data usage.

3. Select the payment method: **UAH, RUB, or USDT (crypto)**.

4. Confirm the payment in the bot. The admin verifies it manually.

5. Stars are credited to the recipient after verification. ✅

---

## 💡 How It Works

1. **Choose Stars** – select how many stars you want to buy. ✨
2. **Recipient** – enter the Telegram username of the recipient.
3. **Payment** – choose the payment method (crypto, UAH, RUB). 💰
4. **Confirmation** – confirm your payment in the bot; the admin verifies the transaction.
5. **Credit** – after verification, stars are credited to the recipient’s account instantly. ✅

---

## 📜 License

MIT
