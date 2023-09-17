# pgzero
import random
import time

# E-interact
# SPACE-envanter göster
# W A S D-hareket
# F-skip cutscene
# character name = Ezekiel, Zachary, Casey, Cesar, Anakin, Azael, Haesel/Hazel, Alohi

# Değişkenler
mod = "menu"
level = 1
a = False

# Ekran
hucre = Actor("zemin1")
hucre1 = Actor("zemin2")
hucre2 = Actor("karanlık-zemin")
hucre3 = Actor("duvar1")
kapi1 = Actor("kapı")
ekran_g = 12  # Ekranın enindeki hücre sayısı
ekran_y = 9  # Ekranın boyundaki hücre sayısı

# if mod == "menu":
#    hucre.width = 63
#    hucre.height = 40

WIDTH = hucre.width * ekran_g
HEIGHT = hucre.height * ekran_y

TITLE = "5Labirent"  # Oyun Adı
FPS = 30  # Saniyedeki Kare Sayısı

duvarlar = []  # Geçilemez bloklar
dortler = []  # Şalterin karşısındaki blok
inventory = []  # Envanter

# Nesneler
karakter = Actor('karakter')
menu = Actor("menu")
notesmenu = Actor("notesmenu", (WIDTH / 2, 310))
inst = Actor("instructions", (WIDTH / 2, 240))
start = Actor("START", (WIDTH / 2, 170))
dark = Actor("dark")
altin_a = Actor("altın-anahtar", topleft=(hucre1.width * 5, hucre1.height * 7))
demir_a = Actor("demir-anahtar", topleft=(hucre1.width * 7, hucre1.height * 7))
bakir_a = Actor("bakır-anahtar", topleft=(hucre1.width * 3, hucre1.height * 5))
eskibakir_a = Actor("eski-bakır-anahtar", topleft=(hucre1.width * 5, hucre1.height * 7))
painted_key = Actor("boyalı-anahtar", topleft=(hucre1.width * 4, hucre1.height))
lastkey = Actor("lastkey", topleft=(hucre1.width * 7, hucre1.height * 7))
wetkey = Actor("ıslak-anahtar", topleft=(hucre1.width * 7, hucre1.height * 5))
kirli_a = Actor("kirli-anahtar", topleft=(hucre1.width * 1, hucre1.height * 6))
xsign = Actor("x", (WIDTH - 20, 20))

kksalter = Actor("kolu-kayıp-şalter", topleft=(hucre1.width * 4, hucre1.height * 3))
salter = Actor("y-şalter", topleft=(hucre1.width * 5, hucre1.height * 0))
circle = Actor("circle", topleft=(hucre1.width * 5, hucre1.height))
circle2 = Actor("circle2", topleft=(hucre1.width * 4, hucre1.height * 4))
kapi = Actor("kapı", topleft=(hucre1.width * 7, hucre1.height))
ykapi = Actor("ykapı", topleft=(hucre1.width * 6, hucre1.height * 2))
skolu = Actor("şalter-kolu", topleft=(hucre1.width * 1, hucre1.height * 7))

haritam = [[0, 3, 3, 3, 3, 3, 3, 3, 3],
           [1, 1, 3, 0, 1, 1, 3, 1, 3],
           [3, 0, 3, 1, 1, 1, 4, 1, 3],
           [3, 0, 3, 0, 3, 1, 1, 1, 3],
           [3, 1, 3, 1, 3, 1, 0, 1, 3],
           [3, 1, 3, 1, 3, 0, 1, 1, 3],
           [3, 1, 3, 0, 3, 1, 0, 1, 3],
           [3, 1, 1, 1, 3, 2, 1, 1, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3]]

haritam2 = [[0, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 1, 0, 0, 1, 1, 1, 0, 3],
            [3, 3, 3, 3, 3, 0, 3, 1, 3],
            [3, 0, 0, 0, 1, 1, 3, 1, 3],
            [3, 3, 0, 1, 1, 1, 3, 1, 3],
            [3, 1, 1, 1, 1, 0, 3, 1, 3],
            [3, 1, 1, 0, 0, 1, 3, 1, 3],
            [3, 1, 1, 1, 1, 2, 3, 2, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3]]

haritam3 = [[0, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 1, 0, 3, 2, 1, 1, 0, 3],
            [3, 3, 0, 3, 3, 3, 0, 3, 3],
            [3, 3, 0, 0, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 1, 3],
            [3, 1, 1, 1, 1, 0, 3, 1, 3],
            [3, 1, 3, 3, 3, 3, 3, 1, 3],
            [3, 1, 1, 1, 1, 1, 0, 0, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3]]

haritam4 = [[0, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 1, 3, 0, 1, 1, 1, 0, 3],
            [3, 1, 3, 3, 3, 0, 3, 1, 3],
            [3, 0, 0, 0, 3, 1, 3, 1, 3],
            [3, 1, 3, 1, 1, 1, 3, 1, 3],
            [3, 1, 3, 2, 1, 0, 3, 2, 3],
            [3, 1, 3, 3, 3, 1, 3, 1, 3],
            [3, 2, 1, 1, 1, 0, 3, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3]]

haritam5 = [[0, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 1, 0, 0, 1, 1, 1, 0, 3],
            [3, 1, 3, 1, 3, 0, 3, 3, 3],
            [3, 0, 3, 0, 3, 1, 3, 1, 3],
            [3, 1, 3, 1, 3, 1, 3, 1, 3],
            [3, 1, 3, 2, 3, 0, 3, 1, 3],
            [3, 2, 3, 3, 3, 1, 3, 1, 3],
            [3, 0, 1, 1, 1, 0, 1, 2, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3]]


def on_mouse_down(button, pos):
    global mod
    if start.collidepoint(pos) and mod == "menu":
        mod = "oyun"
    if xsign.collidepoint(pos):
        mod = "menu"
    if inst.collidepoint(pos) and mod == "menu":
        mod = "instr"
    if notesmenu.collidepoint(pos) and mod == "menu":
        mod = "notes"


def harita_cizim():
    global duvarlar, dortler
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            if haritam[i][j] == 0:
                hucre.left = hucre.width * j
                hucre.top = hucre.height * i
                hucre.draw()
            elif haritam[i][j] == 1:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                hucre1.draw()
            elif haritam[i][j] == 2:
                hucre2.left = hucre.width * j
                hucre2.top = hucre.height * i
                hucre2.draw()
            elif haritam[i][j] == 3:
                hucre3 = Actor("duvar1")
                hucre3.left = hucre.width * j
                hucre3.top = hucre.height * i
                duvarlar.append(hucre3)
                hucre3.draw()
            elif haritam[i][j] == 4:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                dortler.append(hucre1)
                hucre1.draw()
            elif haritam[i][j] == 5:
                kapi1 = Actor("kapı")
                kapi1.left = hucre.width * j
                kapi1.top = hucre.height * i
                kapi1.draw()


def harita_cizim2():
    global duvarlar, dortler
    for i in range(len(haritam2)):
        for j in range(len(haritam2[0])):
            if haritam2[i][j] == 0:
                hucre.left = hucre.width * j
                hucre.top = hucre.height * i
                hucre.draw()
            elif haritam2[i][j] == 1:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                hucre1.draw()
            elif haritam2[i][j] == 2:
                hucre2.left = hucre.width * j
                hucre2.top = hucre.height * i
                hucre2.draw()
            elif haritam2[i][j] == 3:
                hucre3 = Actor("duvar1")
                hucre3.left = hucre.width * j
                hucre3.top = hucre.height * i
                duvarlar.append(hucre3)
                hucre3.draw()
            elif haritam2[i][j] == 4:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                dortler.append(hucre1)
                hucre1.draw()
            elif haritam2[i][j] == 5:
                kapi1 = Actor("kapı")
                kapi1.left = hucre.width * j
                kapi1.top = hucre.height * i
                kapi1.draw()


def harita_cizim3():
    global duvarlar, dortler
    for i in range(len(haritam3)):
        for j in range(len(haritam3[0])):
            if haritam3[i][j] == 0:
                hucre.left = hucre.width * j
                hucre.top = hucre.height * i
                hucre.draw()
            elif haritam3[i][j] == 1:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                hucre1.draw()
            elif haritam3[i][j] == 2:
                hucre2.left = hucre.width * j
                hucre2.top = hucre.height * i
                hucre2.draw()
            elif haritam3[i][j] == 3:
                hucre3 = Actor("duvar1")
                hucre3.left = hucre.width * j
                hucre3.top = hucre.height * i
                duvarlar.append(hucre3)
                hucre3.draw()
            elif haritam3[i][j] == 4:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                dortler.append(hucre1)
                hucre1.draw()
            elif haritam3[i][j] == 5:
                kapi1 = Actor("kapı")
                kapi1.left = hucre.width * j
                kapi1.top = hucre.height * i
                kapi1.draw()


def harita_cizim4():
    global duvarlar, dortler
    for i in range(len(haritam4)):
        for j in range(len(haritam4[0])):
            if haritam4[i][j] == 0:
                hucre.left = hucre.width * j
                hucre.top = hucre.height * i
                hucre.draw()
            elif haritam4[i][j] == 1:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                hucre1.draw()
            elif haritam4[i][j] == 2:
                hucre2.left = hucre.width * j
                hucre2.top = hucre.height * i
                hucre2.draw()
            elif haritam4[i][j] == 3:
                hucre3 = Actor("duvar1")
                hucre3.left = hucre.width * j
                hucre3.top = hucre.height * i
                duvarlar.append(hucre3)
                hucre3.draw()
            elif haritam4[i][j] == 4:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                dortler.append(hucre1)
                hucre1.draw()
            elif haritam4[i][j] == 5:
                kapi1 = Actor("kapı")
                kapi1.left = hucre.width * j
                kapi1.top = hucre.height * i
                kapi1.draw()


def harita_cizim5():
    global duvarlar, dortler
    for i in range(len(haritam5)):
        for j in range(len(haritam5[0])):
            if haritam5[i][j] == 0:
                hucre.left = hucre.width * j
                hucre.top = hucre.height * i
                hucre.draw()
            elif haritam5[i][j] == 1:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                hucre1.draw()
            elif haritam5[i][j] == 2:
                hucre2.left = hucre.width * j
                hucre2.top = hucre.height * i
                hucre2.draw()
            elif haritam5[i][j] == 3:
                hucre3 = Actor("duvar1")
                hucre3.left = hucre.width * j
                hucre3.top = hucre.height * i
                duvarlar.append(hucre3)
                hucre3.draw()
            elif haritam5[i][j] == 4:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                dortler.append(hucre1)
                hucre1.draw()
            elif haritam5[i][j] == 5:
                kapi1 = Actor("kapı")
                kapi1.left = hucre.width * j
                kapi1.top = hucre.height * i
                kapi1.draw()

            # def inventory_control():


#    for i in inventory:

def draw():
    global mod
    global a
    global inventory
    screen.fill("black")
    menu.draw()
    if mod == "instr":
        dark.draw()
        screen.draw.text("W A S D => movement", center=(WIDTH / 2, 100), color="white", fontsize=36)
        screen.draw.text("E => İnteraction", center=(WIDTH / 2, 160), color="white", fontsize=36)
        screen.draw.text("Q => Place lever hand", center=(WIDTH / 2, 220), color="white", fontsize=36)
        screen.draw.text("SPACE => İnventory", center=(WIDTH / 2, 280), color="white", fontsize=36)
        xsign.draw()

    if mod == "menu":
        notesmenu.draw()
        inst.draw()
        start.draw()
        screen.draw.text("Beş Labirent", center=(WIDTH / 2, 80), color="white", fontsize=36)

    if mod == "son":
        dark.draw()
        screen.draw.text("Thanks For Playing :)", center=(WIDTH / 2, 150), color="white", fontsize=36)
        xsign.draw()

    if mod == "notes":
        dark.draw()
        screen.draw.text("N/A", center=(WIDTH / 2, 170), color="white", fontsize=60)
        xsign.draw()

    if mod == "oyun":
        screen.fill("black")

    if mod == "oyun" and level == 1:
        harita_cizim()
        circle.draw()
        altin_a.draw()
        kapi.draw()
        karakter.draw()
        xsign.draw()
        salter.draw()

    if mod == "oyun" and level == 2:
        harita_cizim2()
        demir_a.draw()
        eskibakir_a.draw()
        kapi.draw()
        salter.draw()
        circle.draw()
        karakter.draw()
        xsign.draw()

    if mod == "oyun" and level == 3:
        harita_cizim3()
        kapi.draw()
        ykapi.draw()
        salter.draw()
        circle.draw()
        painted_key.draw()
        karakter.draw()
        xsign.draw()

    if mod == "oyun" and level == 4:
        harita_cizim4()
        kapi.draw()
        ykapi.draw()
        circle2.draw()
        kksalter.draw()
        skolu.draw()
        wetkey.draw()
        bakir_a.draw()
        karakter.draw()
        xsign.draw()

    if mod == "oyun" and level == 5:
        harita_cizim5()
        kapi.draw()
        salter.draw()
        circle.draw()
        circle2.draw()
        skolu.draw()
        kksalter.draw()
        lastkey.draw()
        kirli_a.draw()
        karakter.draw()
        xsign.draw()

    if a == True and mod == "oyun":
        y = 40
        for item in inventory:
            screen.draw.text(item, pos=(480, y), color="white", fontsize=14)
            y += 30


def on_key_down(key):
    global dortler
    global level
    global duvarlar
    global mod
    global a
    global inventory
    old_x = karakter.x
    old_y = karakter.y

    if (keyboard.right or keyboard.d) and karakter.x + hucre.width < WIDTH - hucre.width:
        karakter.x += hucre.width
        karakter.image = 'karakter'

    elif (keyboard.left or keyboard.a) and karakter.x - hucre.width > hucre.width:
        karakter.x -= hucre.width
        karakter.image = 'karakter-sol'

    elif (keyboard.down or keyboard.s) and karakter.y + hucre.height < HEIGHT - hucre.height:
        karakter.y += hucre.height
        karakter.image = 'karakter-ön'

    elif (keyboard.up or keyboard.w) and karakter.y - hucre.height > hucre.height:
        karakter.y -= hucre.height
        karakter.image = 'karakter-arka'

    if karakter.colliderect(circle) and keyboard.e:
        salter.image = "d-şalter"

    if karakter.colliderect(altin_a) and keyboard.e and level == 1:
        inventory.append("altin_a")
        altin_a.image = "siyah"

    if karakter.colliderect(demir_a) and keyboard.e and level == 2:
        inventory.append("demir_a")
        demir_a.image = "siyah"

    if karakter.colliderect(eskibakir_a) and keyboard.e and level == 2:
        inventory.append("eskibakir_a")
        eskibakir_a.image = "siyah"

    if karakter.colliderect(painted_key) and keyboard.e and level == 3:
        inventory.append("painted_key")
        painted_key.image = "siyah"

    if karakter.colliderect(wetkey) and keyboard.e and level == 4:
        inventory.append("wetkey")
        wetkey.image = "siyah"

    if karakter.colliderect(bakir_a) and keyboard.e and level == 4:
        inventory.append("bakir_a")
        bakir_a.image = "siyah"

    if karakter.colliderect(lastkey) and keyboard.e and level == 5:
        inventory.append("lastkey")
        lastkey.image = "siyah"

    if karakter.colliderect(kirli_a) and keyboard.e and level == 5:
        inventory.append("kirli_a")
        kirli_a.image = "siyah"

    if karakter.colliderect(skolu) and keyboard.e:
        inventory.append("skolu")
        skolu.image = "siyah"

    if karakter.colliderect(circle2) and "skolu" in inventory and keyboard.q:
        kksalter.image = "y-şalter"
        inventory.remove("skolu")

    if karakter.colliderect(circle2) and keyboard.e and kksalter.image == "y-şalter":
        kksalter.image = "d-şalter"

    if "altin_a" in inventory and salter.image == "d-şalter" and karakter.colliderect(kapi) and level == 1:
        level = 2
        karakter.topleft = (hucre1.width * 0, hucre1.height * 0)
        duvarlar = []
        kapi.topleft = (hucre1.width, hucre1.height * 3)
        salter.topleft = (hucre1.width * 4, hucre1.height * 0)
        circle.topleft = (hucre1.width * 4, hucre1.height)
        salter.image = "y-şalter"

    if karakter.collidelist(duvarlar) != -1:
        karakter.x = old_x
        karakter.y = old_y

    if karakter.colliderect(ykapi) and salter.image != "d-şalter" and level == 3:
        karakter.x = old_x
        karakter.y = old_y

    if karakter.colliderect(ykapi) and kksalter.image != "d-şalter" and level == 4:
        karakter.x = old_x
        karakter.y = old_y

    if "demir_a" in inventory and "eskibakir_a" in inventory and salter.image == "d-şalter" and karakter.colliderect(
            kapi) and level == 2:
        level = 3
        karakter.topleft = (hucre1.width * 0, hucre1.height * 0)
        duvarlar = []
        kapi.topleft = (hucre1.width * 5, hucre1.height * 5)
        salter.topleft = (hucre1.width * 5, hucre1.height * 2)
        circle.topleft = (hucre1.width * 5, hucre1.height * 3)
        salter.image = "y-şalter"

    if "painted_key" in inventory and salter.image == "d-şalter" and karakter.colliderect(kapi) and level == 3:
        level = 4
        karakter.topleft = (hucre1.width * 0, hucre1.height * 0)
        duvarlar = []
        kapi.topleft = (hucre1.width * 7, hucre1.height * 7)
        #        circle.topleft = (hucre1.width*4,hucre1.height*4)
        ykapi.topleft = (hucre1.width * 5, hucre1.height * 2)
        salter.image = "y-şalter"

    if "bakir_a" in inventory and "wetkey" in inventory and kksalter.image == "d-şalter" and karakter.colliderect(
            kapi) and level == 4:
        level = 5
        karakter.topleft = (hucre1.width * 0, hucre1.height * 0)
        duvarlar = []
        kapi.topleft = (hucre1.width * 7, hucre1.height)
        salter.topleft = (hucre1.width * 5, hucre1.height * 0)
        circle2.topleft = (hucre1.width * 6, hucre1.height * 7)
        circle.topleft = (hucre1.width * 5, hucre1.height)
        skolu.topleft = (hucre1.width * 3, hucre1.height * 5)
        kksalter.topleft = (hucre1.width * 6, hucre1.height * 6)
        salter.image = "y-şalter"
        skolu.image = "şalter-kolu"
        kksalter.image = "kolu-kayıp-şalter"

    if "kirli_a" in inventory and "lastkey" in inventory and kksalter.image == "d-şalter" and salter.image == "d-şalter" and karakter.colliderect(
            kapi) and level == 5:
        mod = "son"
        level = 1
        duvarlar = []
        inventory = []
        altin_a.topleft = (hucre1.width * 5, hucre1.height * 7)
        karakter.topleft = (hucre1.width * 0, hucre1.height * 0)
        salter.topleft = (hucre1.width * 5, hucre1.height * 0)
        circle.topleft = (hucre1.width * 5, hucre1.height)
        salter.image = "y-şalter"
        skolu.image = "şalter-kolu"
        kksalter.image = "kolu-kayıp-şalter"

    if keyboard.SPACE:
        a = True


