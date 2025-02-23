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
🔹 30.000 VND/tháng 
🔹 150.000 VND/năm (TẶNG Locket Gold và Spotify Pre )
💁 BAO GỒM:
⚡️ FILE + HDSD 
⚡️ PHÍM TẮT AUTO RESET IP
⚡️ ID SHADOWROCKET 
⚡️ TẶNG Locket Gold và Spotify Pre (VIP)

📌 Các lệnh có thể sử dụng:
/tk - Kiểm tra số dư tài khoản
/qr - Nhận mã QR nạp tiền
/buyadr - Mua gói dịch tháng vụ cho Android 
/buyios - Mua gói dịch tháng vụ cho iOS
/buyadrvip - Mua gói VIP năm cho Android
/buyiosvip - Mua gói VIP năm cho iOS
/nap - Nạp tiền vào tài khoản (Chỉ admin)
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

# Lệnh /nap - Nạp tiền vào tài khoản
@bot.message_handler(commands=['nap'])
def add_balance(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "🙅‍♂️ Bạn không có quyền sử dụng lệnh này.❌")
        return
    
    try:
        _, uid, amount = message.text.split()
        uid = int(uid)
        amount = int(amount)
        update_balance(uid, amount)
        bot.send_message(message.chat.id, f"🎲 Đã nạp {amount} VNĐ vào tài khoản UID {uid}.")
        
        # Thông báo cho người dùng được nạp tiền
        bot.send_message(uid, f"🎉 Tài khoản của bạn đã được admin nạp {amount} VNĐ! Số dư hiện tại của bạn là {get_balance(uid)} VNĐ.")
        
    except ValueError:
        bot.send_message(message.chat.id, "🙅‍♂️ Sai cú pháp! Vui lòng nhập lệnh đúng định dạng: /nap <UID> <Số tiền>❌")

# Các lệnh mua hàng
def process_purchase(message, price, image_url, caption):
    user_id = message.from_user.id
    balance = get_balance(user_id)
    if balance < price:
        bot.send_message(message.chat.id, "🙅‍♂️ Số dư không đủ! Vui lòng nạp thêm tiền.❌")
        return
    update_balance(user_id, -price)
    bot.send_photo(message.chat.id, image_url, caption=caption)

@bot.message_handler(commands=['buyios'])
def buy_ios(message):
    process_purchase(message, 35000, "https://i.postimg.cc/mgt2wDjp/photo-2025-02-23-15-29-22.jpg", 
    """🙇 Cảm ơn quý khách đã ủng hộ VMmod
📲 Hãy lưu và dán vào V2ray để sử dụng
⚠️ Lưu ý dò đúng IP
❤️ Mãi YÊUUUUUUUUUU

📍 Miền bắc 5 215 216
📍 Miền trung 215 216 19
📍 Miền nam 19 125
📍 Shadowrocket ID FREE: https://idapple.htpn.vn/share.php
📍 Phím tắt AUTO RESET IP: https://www.icloud.com/shortcuts/d626e1053f494de9b5e03bfd29cd1240
📍 Anh chị cần LOCKET GOLD và SPOTIFY PREMIUM thì ib em Việt @Vmmod11""")

@bot.message_handler(commands=['buyiosvip'])
def buy_iosvip(message):
    process_purchase(message, 150000, "https://i.postimg.cc/MGkGswv7/photo-2025-02-23-16-44-39.jpg",
    """🙇 Cảm ơn quý khách đã ủng hộ VMmod
📲 Hãy lưu và dán vào V2ray để sử dụng
⚠️ Lưu ý dò đúng IP
❤️ Mãi YÊUUUUUUUUUU

📍 Miền bắc 5 215 216
📍 Miền trung 215 216 19
📍 Miền nam 19 125
📍 Shadowrocket ID FREE: https://idapple.htpn.vn/share.php
📍 Phím tắt AUTO RESET IP: https://www.icloud.com/shortcuts/d626e1053f494de9b5e03bfd29cd1240
🎁 Tặng module: LOCKET GOLD VÀ SPOTIFY PRE
🔗 LOCKET GOLD: [MODULE](https://raw.githubusercontent.com/quocchienn/lockcrack/refs/heads/module/Locket_Gold.sgmodule)
🎵 SPOTIFY PRE: [MODULE](https://yfamily.vercel.app/module/spotifyVIP.module)""")

@bot.message_handler(commands=['buyadr'])
def buy_adr(message):
    process_purchase(message, 35000, "https://i.postimg.cc/nhXk44Ds/nh-ch-p-m-n-h-nh-2025-02-23-170903.png", 
    """🙇 Cảm ơn quý khách đã ủng hộ VMmod
📲 Hãy lưu và dán vào V2ray để sử dụng
⚠️ Lưu ý dò đúng IP
❤️ Mãi YÊUUUUUUUUUU

📍 Miền bắc 5 215 216
📍 Miền trung 215 216 19
📍 Miền nam 19 125""")

@bot.message_handler(commands=['buyadrvip'])
def buy_adrvip(message):
    process_purchase(message, 150000, "https://i.postimg.cc/nhXk44Ds/nh-ch-p-m-n-h-nh-2025-02-23-170903.png", 
    """🙇 Cảm ơn quý khách đã ủng hộ VMmod
📲 Hãy lưu và dán vào V2ray để sử dụng
⚠️ Lưu ý dò đúng IP
❤️ Mãi YÊUUUUUUUUUU

📍 Miền bắc 5 215 216
📍 Miền trung 215 216 19
📍 Miền nam 19 125""")

# Chạy bot
bot.polling()
print("Bot đã cập nhật phiên bản mới") 
