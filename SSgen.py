  
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print("""processing.......""")

API_KEY = '1754367'
API_HASH = "231b8cc6cca12ee51a85cf543321f476"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"** TELEGRAM STRING SESSION**👇\n(Kopyalamak İçin Dokun) \n\n `{session}`\n\n\n **")
      print("Telegram Dizisi oturumunuz, Telegram Kayıtlı Mesajlarınıza başarıyla kaydedildi. Lütfen Kayıtlı Mesajlarınızı kontrol edin ")
      print("Güvenli bir yerde saklayın!!")
  except:
   print ("")
   print ("Yanlış telefon numarası \n ülke kodunun doğru olduğundan emin olun")
   print ("")
   continue
  break
