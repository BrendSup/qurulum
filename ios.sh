MESAJ="BrendUserbot Avtomatik qurulum başladı"
MESAJ="t.me/BrendUserbot t.me/BrendSup"
echo y | apk update
clear
echo -e $MESAJ
echo "Python yüklənir"
echo y | apk add python3
clear
echo -e $MESAJ
echo "Git Yüklənir"
echo y | apk add git
clear
echo -e $MESAJ
echo "TeleThon Yüklənir"
python3 -m pip install telethon
echo "Son addımlar..."
git clone https://github.com/brendsupport/brend_installler
clear
echo -e $MESAJ
clear
echo -e $MESAJ
echo "Bitmək üzərədir..."
cd brend_installler
python3 -m pip install wheel
python3 -m pip install -r requirements.txt
clear
python3 -m brend_installer
