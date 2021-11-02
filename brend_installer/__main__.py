import heroku3
from time import time
import random
import requests
from git import Repo
from brend_installer import *
from .astring import main
import os
import base64 #
from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
from asyncio import get_event_loop
from .language import LANG, COUNTRY, LANGUAGE, TZ
from rich.prompt import Prompt, Confirm

LANG = LANG['MAIN']

def connect (api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        hata(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp (connect):
    appname = "brend" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        hata(LANG['MOST_APP'])
        exit(1)
    return appname

def hgit (connect, repo, appname):
    global api
    app = connect.apps()[appname]
    giturl = app.git_url.replace(
            "https://", "https://api:" + api + "@")

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        hata(LANG['ERROR'] + str(e))

    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    basarili(LANG['SUCCESS_POSTGRE'])
    return app

async def botlog (String, Api, Hash):
    Client = TelegramClient(StringSession(String), Api, Hash)
    await Client.start()

    KanalId = await Client(CreateChannelRequest(
        title='BrendUserbot BotLog',
        about=LANG['AUTO_BOTLOG'],
        megagroup=True
    ))
    KanalId = KanalId.chats[0].id

    Photo = await Client.upload_file(file='brendlogo.jpg')
    await Client(EditPhotoRequest(channel=KanalId, 
        photo=Photo))
    msg = await Client.send_message(KanalId, LANG['DONT_LEAVE'])
    await msg.pin()

    KanalId = str(KanalId)
    if "-100" in KanalId:
        return KanalId
    else:
        return "-100" + KanalId

if __name__ == "__main__":
    logo(LANGUAGE)
    loop = get_event_loop()
    api = soru(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    basarili(LANG['LOGGED'])

    # Telegram İşlemleri #
    onemli(LANG['GETTING_STRING_SESSION'])
    stri, aid, ahash = main()
    basarili(LANG['SUCCESS_STRING'])
    baslangic = time()

    # Heroku İşlemleri #
    bilgi(LANG['CREATING_APP'])
    appname = createApp(heroku)
    basarili(LANG['SUCCESS_APP'])
    onemli(LANG['DOWNLOADING'])

    #Kohne repo https://github.com/brendsupport/brenduserbot
    #Əkənin varyoxunu sikim peyser ble
    #Peyserler:
    #1) Fərid - https://github.com/FaridDadashzade/Installer/blob/1ed448a46d35f4bea4af87ee3b6ba6d684a3e990/cyber_installer/__main__.py#L107
    #
    #
    #====================================#
    # Brend UserBot Auto Deployer Heroku #
    #        Kopyalama Matı... :)        #
    #====================================#
    # 📡
    #
    brend = b"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x62\x72\x65\x6E\x64\x73\x75\x70\x2F\x62\x72\x65\x6E\x64\x75\x73\x65\x72\x62\x6F\x74"
    auto = b"\x2E\x2F\x62\x72\x65\x6E\x64\x75\x73\x65\x72\x62\x6F\x74\x2F"
    deployer = b"\x62\x72\x61\x6E\x63\x68\x3D\x22\x6D\x61\x73\x74\x65\x72\x22"
    soyus_var = b"\x42\x72\x65\x6E\x64\x5F\x69\x6E\x73\x74\x61\x6C\x6C\x65\x72\x20\x40\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x74\xC9\x99\x72\xC9\x99\x66\x69\x6E\x64\xC9\x99\x6E\x20\xC5\x9F\x69\x66\x72\xC4\xB1\x6C\xC9\x99\x6E\x69\x62\x2E\x2E\x2E\x21\x21\x21\x0A\x41\x20\x67\x69\x6A\x64\xC4\xB1\x6C\x6C\x61\x78\x20\x67\x65\x72\x65\x6B\x20\x61\x67\x69\x72\x20\x73\x6F\x79\x75\x73\x20\x71\x6F\x79\x75\x6D\x20\x62\x75\x72\x61\x20\x3F\x20\xF0\x9F\x98\x82\x20\x61\xC3\xA7\x6D\x61\x64\x61\x20\x62\x6C\x65\x74\x20\x6E\x61\x78\x75\x79"
    installer_sifrelenib = brend.decode("utf8")
    cruel = auto.decode("utf8") # 😈
    branch = deployer.decode("utf8") # 😱
    aykhan_s = soyus_var.decode("utf8") # 🤫
    if os.path.isdir("cruel"): # 😳
        rm_r("cruel") # 😎
    repo = Repo.clone_from(installer_sifrelenib,"cruel", branch="master")
    basarili(LANG['DOWNLOADED'])
    onemli(LANG['DEPLOYING'])
    app = hgit(heroku, repo, appname)
    config = app.config()
    #
    #====================================#
    # Brend UserBot Auto Deployer Heroku #
    #        Kopyalama Matı... :)        #
    #====================================#


    onemli(LANG['WRITING_CONFIG'])

    config['ANTI_SPAMBOT'] = 'False'
    config['ANTI_SPAMBOT_SHOUT'] = 'False'
    config['API_HASH'] = ahash
    config['API_KEY'] = str(aid)
    config['BOTLOG'] = "False"
    config['BOTLOG_CHATID'] = "0"
    config['CLEAN_WELCOME'] = "True"
    config['CONSOLE_LOGGER_VERBOSE'] = "False"
    config['COUNTRY'] = COUNTRY
    config['DEFAULT_BIO'] = "@BrendUserBot"
    config['GALERI_SURE'] = "60"
    config['CHROME_DRIVER'] = "/usr/sbin/chromedriver"
    config['GOOGLE_CHROME_BIN'] = "/usr/sbin/chromium"
    config['HEROKU_APIKEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['STRING_SESSION'] = stri
    config['HEROKU_MEMEZ'] = "True"
    config['LOGSPAMMER'] = "False"
    config['PM_AUTO_BAN'] = "False"
    config['PM_AUTO_BAN_LIMIT'] = "4"
    config['ALIVE_LOGO'] = "https://telegra.ph/file/d61b9172fc143fdfc86a2.gif"
    config['TMP_DOWNLOAD_DIRECTORY'] = "./downloads/"
    config['TZ'] = TZ
    config['TZ_NUMBER'] = "1"
    config['UPSTREAM_REPO_URL'] = "https://github.com/BrendSup/brenduserbot"
    config['WARN_LIMIT'] = "3"
    config['WARN_MODE'] = "gmute"
    config['LANGUAGE'] = LANGUAGE

    basarili(LANG['SUCCESS_CONFIG'])
    bilgi(LANG['OPENING_DYNO'])

    try:
        app.process_formation()["worker"].scale(1)
    except:
        hata(LANG['ERROR_DYNO'])
        exit(1)

    basarili(LANG['OPENED_DYNO'])
    basarili(LANG['SUCCESS_DEPLOY'])
    tamamlandi(time() - baslangic)

    Sonra = Confirm.ask(f"[bold yellow]{LANG['AFTERDEPLOY']}[/]", default=True)
    if Sonra == True:
        BotLog = False
        Cevap = ""
        while not Cevap == "4":
            if Cevap == "1":
                bilgi(LANG['OPENING_BOTLOG'])

                KanalId = loop.run_until_complete(botlog(stri, aid, ahash))
                config['BOTLOG'] = "True"
                config['BOTLOG_CHATID'] = KanalId

                basarili(LANG['OPENED_BOTLOG'])
                BotLog = True
            elif Cevap == "3":
                if BotLog:
                    config['LOGSPAMMER'] = "True"
                    basarili(LANG['SUCCESS_LOG'])
                else:
                    hata(LANG['NEED_BOTLOG'])
            elif Cevap == "2":
                config['OTOMATIK_KATILMA'] = "False"
                basarili(LANG['SUCCESS_SUP'])
            
            bilgi(f"\[1] {LANG['BOTLOG']}\n\[2] {LANG['NO_SUP']}\n\[3] {LANG['NO_LOG']}\n\[4] {LANG['CLOSE']}")
            
            Cevap = Prompt.ask(f"[bold yellow]{LANG['WHAT_YOU_WANT']}[/]", choices=["1", "2", "3", "4"], default="4")
        basarili("Görüşmək ümidi ilə!")
