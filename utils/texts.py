
START_MESSAGE = """
<b>
Salom! 🎉 Men Beshariq tumanida online telefon raqamlarini sotish bilan shug'ullanadigan botman! 📱

Sizga telefon raqamlarini tanlash, xarid qilish va ular bilan bog'liq barcha savollarga yordam beraman. Agar sizda telefon raqamlariga oid biron bir savol yoki so'rov bo'lsa, men bilan bog'laning!

Sizga yordam bera olishim uchun sizning savollaringizni kutaman! 🤖

📲 Telegram: @Bakhodir_3123
📞 Telefon: +998 94 915 92 68
</b>
"""

CONTACT_MESSAGE = """
<b>
📲 Telegram: @Bakhodir_3123
📞 Telefon: +998 94 915 92 68
</b>
"""




def create_number_info(selected_number):
    """
    Tanlangan raqam haqidagi ma'lumotlarni formatlaydi.
    
    :param selected_number: Tanlangan raqam ma'lumotlari
    :return: Raqam haqida formatlangan xabar
    """
    number_info = (
        f"📱 **Nomer:** {selected_number['number']}\n"
        f"💵 **Narxi:** {'bepul' if selected_number['price'] == 0 else f'{selected_number['price']} so\'m'}\n"
        f"🔖 **Chegirma:** {'yo\'q' if selected_number['discount'] == 0 else f'{selected_number['discount']}%'}\n"
    )
    
    return number_info