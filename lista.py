import klasa


def make_list():
    L = [
        klasa.Doc("Dowód Osobisty Zbyszek", "30.05.2027",
                  "Wydany 30.05.2017 przez Wójta Gminy Gorzyce", "Seria CEU 826 321, PESEL 640426 06934"),

        klasa.Doc("Dowód Osobisty Jola", "28.01.2026",
                  "Wydany 28.01.2016 przez Wójta Gminy Gorzyce", "Seria CBU 037 122, PESEL 641110 04689"),

        klasa.Doc("EKUZ Zbyszek", "1.03.2022",
                  "Nr identyfikacyjny karty: 8061 6000 1200 2149 7568 ",
                  "Nr identyfikacyjny instytucji: NFZ KATOWICE - WF12"),

        klasa.Doc("EKUZ Jola", "30.04.2020",
                  "karta nieważna", "Nr identyfikacyjny instytucji: NFZ KATOWICE - WF12"),

        klasa.Doc("Ferbi szczepienie", "5.11.2021",
                  "Zwierzakowo Lek. Wet. Beata Mazur", "tel. +48 607 476 314"),

        klasa.Doc("GSU Zbyszek", "31.08.2022",
                  "karta rabatowa  102 107 202 254, nr klienta  1153087, hasło: Szekzby12@",
                  "po 71.50 zł. m-c do 10 dnia m-ca"),

        klasa.Doc("Internet Luksus", "1.01.2021",
                  "65 zł./m-c, ID 137, PIN 561280", "hasło sxr6h2dt"),

        klasa.Doc("Dom PZU", "30.12.2020",
                  "Nr karty rabatowej 102 107 202 254", "466 zł./rok"),

        klasa.Doc("Mama Rydułtowy", "28.02.2021",
                  "Zapłacić pomiędzy 16.01 a 28.02 ", "Odszkodowanie 1 550 zł."),

        klasa.Doc("Karta PKO MC Zbyszek", "31.01.2021",
                  "mastercard", "konto Aurum"),

        klasa.Doc("Karta PKO VISA Jola", "31.01.2021",
                  "Karta VISA", "konto Aurum"),

        klasa.Doc("Baleno - przegląd gwarancyjny", "29.05.2021",
                  "33 197 km - maksymalny przebieg", "Suzuki Rybnik"),

        klasa.Doc("Baleno - badania techniczne", "30.05.2022",
                  "po 2 latach użytkowania", "100 zł."),

        klasa.Doc("Baleno - PZU", "30.05.2021",
                  "nr karty rabatowej 102 107 202 254", "1 614 zł."),

        klasa.Doc("Komórka Jola", "27.03.2022",
                  "tel. +48 698 385 284 ", "T-Mobile"),

        klasa.Doc("Komórka Zbyszek", "30.09.2021",
                  "tel. +48 604 733 938", "PIN1 5855, PIN2 7419, PUK1 14908437, PUK2 65294624"),

        klasa.Doc("Komórka Mama", "6.04.2022",
                  "tel. +48 692 394 293, 24 doładowania po 50 zł. do 16 dnia m-ca",
                  "PIN 9885, agnieszkaszurman71@gmail.com, Szekzby12"),

        klasa.Doc("Komórka Tosia", "30.06.2021",
                  "tel. +48 724 104 003, 42 doładowania po 30 zł.", "Plus"),

        klasa.Doc("Kredyt PKO", "26.03.2022",
                  "rata 1 613.38 zł.", "pobierana automatycznie 26 dnia m-ca"),

        klasa.Doc("Router", "16.04.2022",
                  "tel. 882 061 921, login admin, hasło admin",
                  "hasło do routera 2l5p35p3, PIN1 9906, PIN2 7397\nPUK1 7623525, PUK2 10433410"),

        klasa.Doc("Karta kredytowa PKO Zbyszek", "31.01.2024",
                  "karta VISA", "karta kredytowa"),

        klasa.Doc("Karta kredytowa PKO Jola", "28.01.2026",
                  "Wydany 28.01.2016 przez Wójta Gminy Gorzyce", "CBU 037 122"),

        klasa.Doc("Baleno - przegląd techniczny", "30.05.2027",
                  "Wydany 30.05.2017 przez Wójta Gminy Gorzyce", "CEU 826 321"),

        klasa.Doc("Paszport Jola", "1.07.2029",
                  "Wydany 1.07.2019 przez Wojewodę Śląskiego", "nr paszportu ES 6275143"),

        klasa.Doc("Paszport Zbyszek", "10.06.2029",
                  "Wydany 10.06.2019 przez Wojewodę Śląskiego", "Nr paszportu ES 8129824"),

        klasa.Doc("WP", "31.12.2100",
                  "zszurman@wp.pl", "WP pilot, Ipla, Spotify, Tauron, Allegro, Booking, Polar, FB, Cubase, Vitay"),

        klasa.Doc("GMAIL", "31.12.2100",
                  "zszurman@gmail.com ", "Sygic"),

        klasa.Doc("Karta Revolut", "31.07.2024",
                  "mastercard", "karta walutowa"),

        klasa.Doc("Legitymacja Emeryta - Rencisty", "31.12.2100",
                  "Nr 34/12/E/004006/16, Rybnik 25.07.2016 ZUS Oddział w Rybniku", "Nr świadczenia KGE/25/07/182682"),

        klasa.Doc("Mama dane", "31.12.2100",
                  "PESEL 360402 11841", "Karta 9563"),

        klasa.Doc("PKO", "31.12.2100",
                  "32000079   50724921  (18 1020 2472 0000 6902 0107 7205)",
                  "SamwBarze12  Mojastopa64  2975  3390  Szekzby12  Szekzby12@"),

        klasa.Doc("PZU", "31.12.2100",
                  "Szekzby12@", "mojepzu.pl"),

        klasa.Doc("GitHub", "31.12.2100",
                  "zszurman", "Szekzby12"),

        klasa.Doc("Sygic", "31.12.2100",
                  "KOD 7VXR-P6RK-VPEH-65MP", "zszurman@gmail.com"),

        klasa.Doc("Netflix", "31.12.2100",
                  "szumi.bs@gmail.com, fcbarcelona", "I, IV, VII, X - po 52 zł."),

        klasa.Doc("Chomik", "31.12.2100",
                  "zszurman@wp.pl", "zima1964"),
    ]
    return L
