import telebot

bot = telebot.TeleBot("7165323948:AAGe59mWIO0IhabXkeXPUyBikXmYcMeaQj4")

ADMIN_ID = 6929210318
accounts = {}

def get_balance(uid):
    return accounts.get(uid, 0)

def update_balance(uid, amount):
    accounts[uid] = get_balance(uid) + amount

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(
        message.chat.id,
        f"""4G Không nền Xin chào! UID của bạn là {user_id}. Hãy gửi UID cho @Vmmod11 và quét QR để nạp tiền.
GIÁ NIÊM YẾT:
30000 VND
bao gồm file+phím tắt auto reset IP+id shadow+config  
 TẶNG locket gold +HDSD

Các lệnh có thể sử dụng:
/tk - Kiểm tra số dư tài khoản
/buy - Mua gói dịch vụ 
/nap - Nạp tiền vào tài khoản (Chỉ admin mới có quyền sử dụng)
"""
    )
    
    photo_url = "https://i.postimg.cc/YSgHpX2H/d4d5ece1-9476-4cec-a70c-fb71326aef0c.jpg"
    bot.send_photo(message.chat.id, photo_url, caption="Đây là mã QR để nạp tiền")

@bot.message_handler(commands=['tk'])
def check_account(message):
    user_id = message.from_user.id
    balance = get_balance(user_id)
    bot.send_message(message.chat.id, f"Tài khoản UID {user_id}: Số dư của bạn là {balance} VNĐ")

@bot.message_handler(regexp=r"^/nap (\d+) (\d+)$")
def nap_tien(message):
    if message.from_user.id == ADMIN_ID:
        uid, so_tien = message.text.split()[1:3]
        so_tien = int(so_tien)
        update_balance(int(uid), so_tien)
        bot.send_message(message.chat.id, f"Đã nạp {so_tien} VNĐ cho UID {uid}")
    else:
        bot.send_message(message.chat.id, "Bạn không có quyền sử dụng lệnh này!")

@bot.message_handler(commands=['buy'])
def buy_product(message):
    user_id = message.from_user.id
    cost = 30000
    balance = get_balance(user_id)
    
    if balance >= cost:
        update_balance(user_id, -cost)
        bot.send_message(message.chat.id, f"Bạn đã mua hàng thành công! Số dư còn lại: {get_balance(user_id)} VNĐ")
        
        photo_url = "https://i.postimg.cc/X7wvncLd/photo-2025-02-21-12-55-33.jpg"
        bot.send_photo(message.chat.id, photo_url, caption="Nhập vào shadow để sử dụng!")
    else:
        bot.send_message(message.chat.id, f"Số dư không đủ! Số dư hiện tại của bạn là {balance} VNĐ")

bot.polling()
