MESAJ="BrendUserbot Avtomatik qurulum başladı"
MESAJ="t.me/BrendUserbot t.me/BrendSup"
pkg update -y
clear
echo -e $MESAJ
echo "Python yüklənir"
pkg install python -y
clear
echo -e $MESAJ
echo "Git Yüklənir"
pkg install git -y
clear
echo -e $MESAJ
echo "TeleThon Yüklənir"
pip install telethon
echo "Son addımlar"
git clone https://github.com/brendsup/qurulum
clear
echo -e $MESAJ
cd brend_installler
clear
echo "Bitmək üzərədir..."
echo -e $MESAJ
pip install wheel
pip install -r requirements.txt
python3 -m brend_installer
