from doc import Doc
from cyf import Cyf
from bday import Bday
from kosz import Kosz
import folium
import webbrowser

print("Cyferki by Zbigniew Szurman\nLoading... ")


def make_list_dok():
    return [
        Doc("Dowód Osobisty Zbyszek", "30.05.2027",
            "Wydany 30.05.2017 przez Wójta Gminy Gorzyce", "Seria CEU 826 321\nPESEL 640426 06934"),

        Doc("Dowód Osobisty Jola", "28.01.2026",
            "Wydany 28.01.2016 przez Wójta Gminy Gorzyce", "Seria CBU 037 122\nPESEL 641110 04689"),

        Doc("EKUZ Zbyszek", "1.03.2022",
            "Nr identyfikacyjny karty: 8061 6000 1200 2149 7568 ",
            "Nr identyfikacyjny instytucji: NFZ KATOWICE - WF12"),

        Doc("EKUZ Jola", "30.04.2020",
            "Karta nieważna", "Nr identyfikacyjny instytucji: NFZ KATOWICE - WF12"),

        Doc("Ferbi Szczepienie", "5.11.2021",
            "Zwierzakowo Lek. Wet. Beata Mazur", "tel. +48 607 476 314"),

        Doc("Internet Luksus", "1.02.2023",
            "65 zł./m-c\nID 137\nPIN 561280", "sxr6h2dt"),

        Doc("Dom PZU", "30.12.2021",
            "Nr karty rabatowej 102 107 202 254", "466 zł./rok"),

        Doc("Karta PKO MC Zbyszek", "31.01.2026",
            "Mastercard", "konto Aurum"),

        Doc("Karta PKO VISA Jola", "31.01.2026",
            "Karta VISA", "konto Aurum"),

        Doc("Baleno Przegląd Gwarancyjny", "29.05.2021",
            "33 197 km - maksymalny przebieg", "Suzuki Rybnik"),

        Doc("Baleno Badania Techniczne", "30.05.2022",
            "Po 3 latach użytkowania", "100 zł."),

        Doc("Baleno PZU", "30.05.2021",
            "Nr karty rabatowej 102 107 202 254", "1 614 zł."),

        Doc("Komórka Jola", "27.03.2022",
            "Tel. +48 698 385 284 ", "T-Mobile"),

        Doc("Komórka Zbyszek", "30.09.2021",
            "Tel. +48 604 733 938", "PIN1 5855\nPIN2 7419\nPUK1 14908437\nPUK2 65294624"),

        Doc("Komórka Tosia", "30.06.2021",
            "Tel. +48 724 104 003, 42 doładowania po 30 zł.", "Plus"),

        Doc("Kredyt PKO", "26.03.2022",
            "Rata 1 571.08 zł.", "pobierana automatycznie 26 dnia m-ca"),

        Doc("Router", "16.04.2022",
            "Tel. 882 061 921, login admin, hasło admin",
            "hasło do routera 2l5p35p3\nPIN1 9906\nPIN2 7397\nPUK1 7623525\nPUK2 10433410"),

        Doc("Karta Kredytowa PKO Zbyszek", "31.01.2024",
            "Karta VISA", "karta kredytowa"),

        Doc("Karta Kredytowa PKO Jola", "30.04.2022",
            "Karta Kredytowa", ""),

        Doc("Paszport Jola", "1.07.2029",
            "Wydany 1.07.2019 przez Wojewodę Śląskiego", "nr paszportu ES 6275143"),

        Doc("Paszport Zbyszek", "10.06.2029",
            "Wydany 10.06.2019 przez Wojewodę Śląskiego", "Nr paszportu ES 8129824"),

        Doc("Karta Revolut", "31.07.2024",
            "Mastercard", "Karta walutowa"),

        Doc("Mama Rydułtowy", "28.02.2022",
            "Zapłacić 54 zł. pomiędzy 16.01 a 28.02 ", "Odszkodowanie 1 550 zł."),

        Doc("Mama Komórka", "6.04.2022",
            "tel. +48 692 394 293, 24 doładowania po 50 zł. do 16 dnia m-ca",
            "PIN 9885\nagnieszkaszurman71@gmail.com\nSzekzby12"),
    ]


print("Liczba dok = " + str(len(make_list_dok())))


def make_list_cyf():
    return [

        Cyf("GSU",
            "Karta rabatowa  102 107 202 254\nNr klienta  1153087\nSzekzby12@",
            "Hasło tel. 48911654\nPo 71.50 zł.do 10 dnia poprzedzającego m-ca ", 'drawable/ic_gsu.png'),

        Cyf("WP",
            "zszurman@wp.pl  Szekzby12  Szekzby12@  ",
            "WP pilot, Ipla, Spotify, Tauron, Allegro, Booking, Polar\nFB, Cubase, Vitay", 'drawable/ic_wp.png'),

        Cyf("GMAIL",
            "zszurman@gmail.com  Szekzby12", "Sygic", 'drawable/ic_gmail.png'),

        Cyf("Legitymacja Emeryta",
            "Nr 34/12/E/004006/16\nRybnik 25.07.2016 ZUS Oddział w Rybniku", "Nr świadczenia KGE/25/07/182682",
            'drawable/ic_zus.png'),

        Cyf("PKO",
            "32000079   SamwBarze12\n50724921    Mojastopa64",
            "2975  3390\nSzekzby12  Szekzby12@\n18 1020 2472 0000 6902 0107 7205", 'drawable/ic_pko.png'),

        Cyf("PZU",
            "Szekzby12@", "mojepzu.pl", 'drawable/ic_pzu.png'),

        Cyf("GitHub",
            "zszurman", "Szekzby12", 'drawable/ic_git.png'),

        Cyf("Sygic",
            "KOD 7VXR-P6RK-VPEH-65MP", "zszurman@gmail.com", 'drawable/ic_sygic.png'),

        Cyf("Netflix",
            "szumi.bs@gmail.com, fcbarcelona", "I, IV, VII, X - po 52 zł.", 'drawable/ic_net.png'),

        Cyf("Chomik",
            "zszurman@wp.pl", "zima1964", 'drawable/ic_chomik.png'),

        Cyf("Mama PZU",
            "raty do 28.02, 31.05, 31.08, 30.11, kwota 129.45 zł.",
            "rata obejmuje 3 m-ce (m-c wpłaty + 2 następne)\nsuma ubezpieczenia 6 100 zł.", 'drawable/ic_pzu.png'),

        Cyf("Mama Dane",
            "PESEL 360402 11841", "Karta 9563\nTel. 692 394 293\nPIN 9885  ", 'drawable/ic_agn.png'),

        Cyf("Cubase AI",
            "Cubase AI 8.0 activation Code\n0240 7CDA RPFO TVSM VBLD XR00 14D4 8C45\n",
            "Cubase AI 10.5 activation Code\n0240 7COA OZAG KJRS CNPO XK00 F142 8B32", 'drawable/ic_cub.png'),

        Cyf("PESEL",
            "Jola  641110 04689", "Zbyszek  640426 06934\nMama  360402 11841 ", 'drawable/ic_herb.png'),

        Cyf("T-Mobile",
            "Jola  698385284 ", "Zbyszek  604733938  882061921\nMama  692394293  ", 'drawable/ic_era.png'),

    ]


print("Liczba cyf = " + str(len(make_list_cyf())))


def make_list_bday():
    return [
        Bday("Agnieszka", "Szurman", 1936, 4, 2, "+48 692 394 293", "44-352 Czyżowice, Wodzisławska 10", "", "u",
             "drawable/ic_agn.png"),

        Bday("Wiktor", "Morończyk", 1939, 2, 19, "+48 694 227 067", "58-200 Dzierżoniów, Oś. Błękitne 10 G/7", "",
             "u",
             "drawable/ic_wik.png"),

        Bday("Jolanta", "Szurman", 1964, 11, 10, "+48 698 385 284", "44-352 Czyżowice, Wodzisławska 10",
             "jolszurman@wp.pl", "u", "drawable/ic_jol.png"),

        Bday("Zbigniew", "Szurman", 1964, 4, 26, "+48 604 733 938", "44-352 Czyżowice, Wodzisławska 10",
             "zszurman@wp.pl", "u", "drawable/ic_zby.png"),

        Bday("Patrycja", "Czerwińska", 1989, 2, 7, "+49 157 521 161 15", "74080 Heilbronn, Heckenstrasse 56",
             "czerwinska.patrycja@gmail.com", "u", "drawable/ic_pat.png"),

        Bday("Łukasz", "Czerwiński", 1989, 1, 31, "+49 157 758 799 59", "74080 Heilbronn, Heckenstrasse 56",
             "czerwinski.lukasz@gmail.com", "u", "drawable/ic_luk.png"),

        Bday("Hanna", "Czerwińska", 2013, 4, 17, "", "74080 Heilbronn, Heckenstrasse 56", "", "u",
             "drawable/ic_han.png"),

        Bday("Elena", "Czerwińska", 2018, 7, 23, "", "74080 Heilbronn, Heckenstrasse 56", "", "u",
             "drawable/ic_ele.png"),

        Bday("Izabela", "Szurman", 1990, 8, 18, "+48 505 340 391", "44-194 Knurów, Mieszka I 17B/2",
             "izabela.stach@onet.eu", "u", "drawable/ic_iza.png"),

        Bday("Błażej", "Szurman", 1990, 7, 29, "+48 517 507 343", "44-194 Knurów, Mieszka I 17B/2",
             "szumi.bs@gmail.com", "u", "drawable/ic_bla.png"),

        Bday("Zofia", "Szurman", 2014, 4, 28, "", "44-194 Knurów, Mieszka I 17B/2", "", "u", "drawable/ic_zos.png"),

        Bday("Florentyna", "Copiak", 1991, 11, 1, "+48 511 270 102", "44-121 Gliwice, Kozielska 63/3",
             "florentyna.szurman@gmail.com", "u", "drawable/ic_flo.png"),

        Bday("Krystian", "Copiak", 1988, 7, 24, "+48 509 974 131", "44-121 Gliwice, Kozielska 63/3",
             "krystiancopiak@gmail.com", "u", "drawable/ic_kry.png"),

        Bday("Antonina", "Jaskuła", 1994, 7, 11, "+48 724 104 003",
             "43-300 Bielsko-Biała, Jacka Malczewskiego 8/32",
             "antoninaszurman@gmail.com", "u", "drawable/ic_ant.png"),

        Bday("Szymon", "Jaskuła", 1994, 10, 1, "+48 510 109 217", "43-300 Bielsko-Biała, Jacka Malczewskiego 8/32",
             "", "u", "drawable/ic_szy.png"),

        Bday("Maria", "Dzierżęga", 1963, 3, 28, "+48 661 326 123", "32-060 Liszki, Ściejowice 174", "", "u",
             "drawable/ic_mar.png"),

        Bday("Krzysztof", "Dzierżęga", 1963, 4, 8, "+48 691 082 424", "32-060 Liszki, Ściejowice 174",
             "krzysztof.dzierzega@edu.pl", "u", "drawable/ic_krz.png"),
        Bday("Jan", "Dzierżęga", 1999, 10, 4, "+48 884 902 965", "32-060 Liszki, Ściejowice 174", "", "u",
             "drawable/ic_jan.png"),

        Bday("Iwona", "Morończyk", 1970, 5, 16, "+48 666 922 776", "32-005 Niepołomice, Daszyńskiego 2A", "", "u",
             "drawable/ic_iwo.png"),

        Bday("Adam", "Morończyk", 1969, 10, 13, "+48 784 057 962", "32-005 Niepołomice, Daszyńskiego 2A", "", "u",
             "drawable/ic_ada.png"),

        Bday("Julia", "Morończyk", 2009, 8, 10, "", "32-005 Niepołomice, Daszyńskiego 2A", "", "u",
             "drawable/ic_jul.png"),

        Bday("Marzena", "Morończyk", 1977, 7, 9, "+48 603 286 161", "43-512 Bestwina, Janowice, Łanowa 5", "", "u",
             "drawable/ic_mrz.png"),

        Bday("Aleksander", "Morończyk", 1976, 2, 18, "+48 695 984 509", "43-512 Bestwina, Janowice, Łanowa 5", "",
             "u",
             "drawable/ic_ale.png"),

        Bday("Wojciech", "Morończyk", 2008, 9, 7, "+48 781 339 222", "43-512 Bestwina, Janowice, Łanowa 5", "", "u",
             "drawable/ic_woj.png"),

        Bday("Oliwier", "Morończyk", 2010, 9, 22, "+48 730 392 072", "43-512 Bestwina, Janowice, Łanowa 5", "", "u",
             "drawable/ic_oli.png"),

        Bday("Jola & Zbyszek", "Szurman", 1988, 10, 1, "",
             "(ślub cywilny 3.09.19988 w Bestwinie)\nKościół św. Józefa Robotnika w Janowicach", "", "r",
             "drawable/ic_slub.png"),

        Bday("Pati & Łukasz", "Czerwińscy", 2012, 10, 28, "", "Kościół pw. Chrystusa Króla w Czyżowicach", "", "r",
             "drawable/ic_slub.png"),
        Bday("Iza & Błażej", "Szurman", 2013, 10, 12, "", "Kościół pw. Chrystusa Króla w Czyżowicach", "", "r",
             "drawable/ic_slub.png"),

        Bday("Flora & Krystian", "Copiak", 2018, 7, 21, "", "Kościół pw. Chrystusa Króla w Czyżowicach", "", "r",
             "drawable/ic_slub.png"),

        Bday("Tosia & Szymek", "Jaskuła", 2020, 4, 25, "", "Kościół pw. Św. Jana Nepomucena w Jaworzu", "", "r",
             "drawable/ic_slub.png"),

        Bday("Zdzisława", "Copiak", 1960, 12, 18, "+48 694 044 924", "29-100 Dąbie, Dąbie 48A", "", "u",
             "drawable/ic_zco.png"),

        Bday("Adam", "Copiak", 1956, 11, 8, "+48 692 982 930", "29-100 Dąbie, Dąbie 48A", "", "u",
             "drawable/ic_aco.png")
    ]


print("Liczba bday = " + str(len(make_list_bday())))


def make_list_kosz():
    return [
        Kosz("Kubeł", ["11.01.2021", "8.02.2021", "8.03.2021", "2.04.2021", "19.04.2021", "30.04.2021", "17.05.2021",
                       "31.05.2021", "14.06.2021", "28.06.2021", "12.07.2021", "26.07.2021", "9.08.2021", "23.08.2021",
                       "6.09.2021", "20.09.2021", "4.10.2021", "18.10.2021", "8.11.2021", "22.11.2021",
                       "6.12.2021"],
             "Opłata za śmieci\nmiesięcznie 3 osoby x 28.50 zł. = 85.50zł.\nkwartalnie 256.50 zł.\n"
             "do 31.III, 30.VI, 30.IX, 15.XII\nmożna płacić miesięcznie",
             'drawable/ic_kubel.png'),
        Kosz("Worki kolorowe", ["8.01.2021", "5.02.2021", "5.03.2021", "2.04.2021", "30.04.2021", "28.05.2021",
                                "25.06.2021", "23.07.2021", "20.08.2021", "17.09.2021", "15.10.2021", "12.11.2021",
                                "10.12.2021"],
             "szkło, metal, tworzywa sztuczne\nopakowania wielomateriałowe",
             'drawable/ic_worki.png'),
        Kosz("Worki brązowe", ["8.01.2021", "5.02.2021", "5.03.2021", "2.04.2021", "16.04.2021", "30.04.2021",
                               "14.05.2021", "28.05.2021", "11.06.2021", "25.06.2021", "9.07.2021",
                               "23.07.2021", "6.08.2021", "20.08.2021", "3.09.2021", "17.09.2021", "1.10.2021",
                               "15.10.2021", "29.10.2021", "12.11.2021", "26.11.2021", "10.12.2021"],
             "Maks. ilość worków brązowych\nod IV do XI po 3 worki bioodpadów\nod XII do III po 1 worku bioodpadów",
             'drawable/ic_bio.png'),
        Kosz("Popiół", ["25.01.2021", "22.02.2021", "22.03.2021", "19.04.2021", "11.10.2021", "8.11.2021", "6.12.2021"],
             "PSZOK dodatkowe śmieci\nrezerwować wizyty na aplikacji\nhttps://pszok.gorzyce.pl\n"
             "odpady remontowo - budowlane tylko w soboty\ntel. 32 451 30 56 (w.21)",
             'drawable/ic_popiol.png'),
        Kosz("Gabaryty", ["28.05.2022"], "", 'drawable/ic_gabaryt.png'),
        Kosz("Emerytura",
             ["25.12.2020", "25.01.2021", "25.02.2021", "25.03.2021", "23.04.2021", "25.05.2021", "25.06.2021",
              "23.07.2021", "25.08.2021", "24.09.2021", "25.10.2021", "25.11.2021", "23.12.2021"],
             "5 027.59 zł.\nSwiadczenie ZUS\n340000E 201025 00 KGE07182682",
             'drawable/ic_kasa.png'),
        Kosz("Prąd",
             ["5.12.2020", "5.01.2021", "5.02.2021", "5.03.2021", "5.04.2021", "5.05.2021", "5.06.2021",
              "5.07.2021", "5.08.2021", "5.09.2021", "5.10.2021", "5.11.2021", "5.12.2021"],
             "około 5 dnia miesiąca podać stan liczników", 'drawable/ic_prad.png'),
        Kosz("Spotkanie Barbórkowe", ["5.12.2020", "4.12.2021"], "", 'drawable/ic_czako.png'),
        Kosz("Mama PZU Życie", ["28.2.2021", "31.05.2021", "31.8.2021", "30.11.2021"],
             "129,45 zł. co 3 m-ce\nokres ubezpieczenia obejmuje m-c wpłaty i 2 następne", 'drawable/ic_pzu.png'),
        Kosz("Mama komórka",
             ["15.12.2020", "15.01.2021", "15.02.2021", "15.03.2021", "15.04.2021", "15.05.2021", "15.06.2021",
              "15.07.2021", "15.08.2021", "15.09.2021", "15.10.2021", "15.11.2021", "15.12.2021"],
             "doładowanie 50 zł.", 'drawable/ic_era.png')
    ]


print("Liczba kosz = " + str(len(make_list_kosz())))


def make_map(lat, lon, zoom):
    mapka = folium.Map(location=[lat, lon], zoom_start=zoom, control_scale=True)

    def marker_home(m, la, lng, popup, tooltip):
        folium.Marker(location=[la, lng], popup=popup, tooltip=tooltip, icon=folium.Icon(
            icon='glyphicon-home', color='pink', prefix='glyphicon')).add_to(m)

    def marker_user(m, la, lng, popup, tooltip):
        folium.Marker(location=[la, lng], popup=popup, tooltip=tooltip, icon=folium.Icon(
            icon='glyphicon-user', color='pink', prefix='glyphicon')).add_to(m)

    def marker_heart(m, la, lng, popup, tooltip):
        folium.Marker(location=[la, lng], popup=popup, tooltip=tooltip, icon=folium.Icon(
            icon='glyphicon-heart', color='pink', prefix='glyphicon')).add_to(m)

    marker_home(mapka, 49.986, 18.42051, '44-352 Czyżowice, Wodzisławska 10',
                'Agnieszka, Jolanta i Zbigniew Szurman')
    marker_heart(mapka, 49.13556, 9.18322, '74080 Heilbronn, Heckenstrasse 56',
                 'Elena, Hanna, Patrycja i Łukasz Czerwińscy')
    marker_heart(mapka, 50.23069, 18.66263, '44-194 Knurów, Mieszka I 17B/2',
                 'Zofia, Izabela i Błażej Szurman')
    marker_heart(mapka, 50.30197, 18.64435, '44-121 Gliwice, Kozielska 63/3',
                 'Florentyna i Krystian Copiak')
    marker_heart(mapka, 49.81506, 19.0283, '44-300 Bielsko-Biała, Jacka Malczewskiego 8/32',
                 'Antonina i Szymon Jaskuła')
    marker_user(mapka, 50.74028, 16.64504, '58-200 Dzierżoniów, Oś.Błękitne 10G/7', 'Wiktor Morończyk')
    marker_user(mapka, 50.00158, 19.77959, '32-060 Liszki, Ściejowice 174',
                'Jan, Maria i Krzysztof Dzierżęga')
    marker_user(mapka, 50.03111, 20.21154, '32-005 Niepołomice, Daszyńskiego 2A',
                ' Julia, Iwona i Adam Morończyk')
    marker_user(mapka, 49.88891, 19.10136, '43-512 Bestwina Janowice, Łanowa 5',
                ' Oliwier, Wojciech, Marzena i Aleksander Morończyk')

    fileHtml = "rodzinka.html"
    mapka.save(fileHtml)
    html_page = f"{fileHtml}"
    mapka.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)
