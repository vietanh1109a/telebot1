import telebot

# Token bot Telegram
TOKEN = "7165323948:AAGe59mWIO0IhabXkeXPUyBikXmYcMeaQj4"
bot = telebot.TeleBot(TOKEN)

# UID Admin
ADMIN_ID = 6929210318

# Database tài khoản (số dư)
accounts = {}

# File ID của video gửi khi bấm /start
VIDEO_FILE_ID = "BAACAgUAAxkBAAIBRGe4t9Lhs8ieOR5fc29x_YdF-KUqAALrFgACim3JVaHzo7dizxFTNgQ"

# Link ảnh QR để nạp tiền
QR_IMAGE_URL = "https://i.postimg.cc/YSgHpX2H/d4d5ece1-9476-4cec-a70c-fb71326aef0c.jpg"

# Hàm lấy số dư
def get_balance(uid):
    return accounts.get(uid, 0)

# Hàm cập nhật số dư
def update_balance(uid, amount):
    accounts[uid] = get_balance(uid) + amount

# Lệnh /start - Chào mừng
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_video(message.chat.id, VIDEO_FILE_ID, caption=f"""
🎉 Chào mừng bạn! UID của bạn là {user_id}. Hãy gửi UID cho @Vmmod11 và nhập lệnh /qr để lấy mã QR nạp tiền.

💰 GIÁ NIÊM YẾT:
🔹 30.000 VND - Bao gồm:
✔️ File + Phím tắt auto reset IP
✔️ ID Shadow + Config
🎁 TẶNG: Locket Gold + HDSD

📌 Các lệnh có thể sử dụng:
/tk - Kiểm tra số dư tài khoản
/buy - Mua gói dịch vụ
/nap - Nạp tiền vào tài khoản (Chỉ admin)
/qr - Nhận mã QR nạp tiền
    """)

# Lệnh /qr - Gửi ảnh QR từ link
@bot.message_handler(commands=['qr'])
def send_qr_image(message):
    bot.send_photo(message.chat.id, QR_IMAGE_URL, caption="📷 Đây là mã QR để nạp tiền!")

# Lệnh /tk - Kiểm tra số dư
@bot.message_handler(commands=['tk'])
def check_account(message):
    user_id = message.from_user.id
    balance = get_balance(user_id)
    bot.send_message(message.chat.id, f"💰 Tài khoản UID {user_id}: Số dư hiện tại là {balance} VNĐ.")

# Lệnh /nap - Admin nạp tiền cho user
@bot.message_handler(regexp=r"^/nap (\d+) (\d+)$")
def nap_tien(message):
    if message.from_user.id == ADMIN_ID:
        uid, so_tien = message.text.split()[1:3]
        so_tien = int(so_tien)
        update_balance(int(uid), so_tien)
        bot.send_message(message.chat.id, f"✅ Đã nạp {so_tien} VNĐ cho UID {uid}.")
    else:
        bot.send_message(message.chat.id, "❌ Bạn không có quyền sử dụng lệnh này!")

# Lệnh /buy - Mua sản phẩm
@bot.message_handler(commands=['buy'])
def buy_product(message):
    user_id = message.from_user.id
    cost = 30000
    balance = get_balance(user_id)

    if balance >= cost:
        update_balance(user_id, -cost)
        bot.send_message(message.chat.id, f"✅ Bạn đã mua hàng thành công! Số dư còn lại: {get_balance(user_id)} VNĐ")

        # Gửi ảnh sau khi mua
        product_photo = "https://i.postimg.cc/G2tGvHZR/photo-2025-02-22-00-01-44.jpg"
        bot.send_photo(message.chat.id, product_photo, caption="🔑 Nhập vào shadow để sử dụng!")
    else:
        bot.send_message(message.chat.id, f"❌ Số dư không đủ! Số dư hiện tại của bạn là {balance} VNĐ.")

# Chạy bot
bot.polling()
print("Bot đã cập nhật phiên bản mới")
