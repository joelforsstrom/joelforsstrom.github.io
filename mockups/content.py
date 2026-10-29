"""Shared content for the mockups, in Swedish (sv) and Finnish (fi).

In the real site this becomes Jekyll data files that Sveltia CMS edits.
"""

EMAIL = "joel.forsstrom@gmail.com"
PHONE = "+358 40 745 6054"
PHONE_HREF = "+358407456054"

UI = {
    "sv": {
        "lang_name": "Svenska",
        "voice": "tenor",
        "nav": {"index": "Hem", "bio": "Biografi", "media": "Media", "cv": "CV"},
        "titles": {"index": "Joel Forsström – tenor", "bio": "Biografi", "media": "Media", "cv": "CV"},
        "news": "Aktuellt",
        "read_bio": "Läs hela biografin",
        "see_cv": "Se CV",
        "featured": "Lyssna",
        "all_media": "Fler videor och bilder",
        "videos": "Video",
        "photos": "Bilder",
        "contact": "Kontakt och förfrågningar",
        "contact_lead": "Joel anlitas gärna för opera, konserter, kyrkomusik och högtidliga tillställningar.",
        "download_cv": "Ladda ner CV (PDF)",
        "print_cv": "Skriv ut",
        "play": "Spela upp",
        "cv_intro": "Roller, engagemang och utbildning.",
        "director": "Regi",
        "conductor": "Dirigent",
        "cv_headers": {"roles": "Roller", "chorus": "Operakorist", "concert": "Solist i konsert och kyrka",
                        "education": "Utbildning", "teachers": "Pedagoger", "masterclasses": "Masterclasser"},
        "cols": {"year": "År", "role": "Roll", "work": "Verk", "venue": "Scen / övrigt", "voice": "Stämma", "house": "Operahus"},
        "photo_credit_note": "Fotografer anges i den slutliga versionen.",
    },
    "fi": {
        "lang_name": "Suomi",
        "voice": "tenori",
        "nav": {"index": "Etusivu", "bio": "Biografia", "media": "Media", "cv": "CV"},
        "titles": {"index": "Joel Forsström – tenori", "bio": "Biografia", "media": "Media", "cv": "Ansioluettelo"},
        "news": "Ajankohtaista",
        "read_bio": "Lue koko biografia",
        "see_cv": "Katso ansioluettelo",
        "featured": "Kuuntele",
        "all_media": "Lisää videoita ja kuvia",
        "videos": "Videot",
        "photos": "Kuvat",
        "contact": "Yhteydenotot ja tiedustelut",
        "contact_lead": "Joel esiintyy mielellään oopperassa, konserteissa, kirkkomusiikkitilaisuuksissa ja juhlissa.",
        "download_cv": "Lataa ansioluettelo (PDF)",
        "print_cv": "Tulosta",
        "play": "Toista",
        "cv_intro": "Roolit, kiinnitykset ja koulutus.",
        "director": "Ohjaus",
        "conductor": "Kapellimestari",
        "cv_headers": {"roles": "Roolit", "chorus": "Oopperakuorolainen", "concert": "Konsertti- ja kirkkosolisti",
                        "education": "Koulutus", "teachers": "Laulupedagogit", "masterclasses": "Mestarikurssit"},
        "cols": {"year": "Vuosi", "role": "Rooli", "work": "Teos", "venue": "Esityspaikka / muuta", "voice": "Ääniala", "house": "Oopperatalo"},
        "photo_credit_note": "Kuvaajat merkitään lopulliseen versioon.",
    },
}

LEAD = {
    "sv": "Finlandssvensk lyrisk tenor, känd för sin klangfulla röst, sin varma scenpersonlighet och sin starka sceniska närvaro.",
    "fi": "Suomenruotsalainen lyyrinen tenori, joka tunnetaan sointuvasta äänestään, lämpimästä esiintyjäpersoonastaan ja vahvasta näyttämöpresenssistään.",
}

BIO = {
    "sv": [
        "Joel Forsström är en finlandssvensk lyrisk tenor utbildad i Stockholm, bland annat vid Stockholm Operastudio. Han är känd för sin klangfulla röst, sin varma scenpersonlighet och sin starka sceniska närvaro.",
        "Efter studier för sångpedagogen Mattias Danielsson debuterade Joel som solist vid Finlands Nationalopera och Nyslotts operafestival under säsongen 2016/2017. Sedan dess har han medverkat i en rad opera- och musikalproduktioner i Finland och Sverige.",
        "Bland hans operaroller märks Tamino i Mozarts <em>Trollflöjten</em>, Nemorino i Donizettis <em>Kärleksdrycken</em>, prins Ramiro i Rossinis <em>Askungen</em> och Monostatos i <em>Trollflöjten</em>. På Finlands Nationalopera har han bland annat framträtt som Förste kommissarien i Poulencs <em>Karmelitsystrarna</em> och Andre nasaréen i Strauss <em>Salome</em>. Sommaren 2025 gestaltade han Monostatos i en kritikerrosad uppsättning av <em>Trollflöjten</em> på Ålands Operafestival, en produktion som återkom 2026.",
        "Joel har även medverkat i musikalproduktioner, bland annat <em>Chess</em> på Svenska Teatern i Helsingfors, och framträtt som solist i sakrala verk såsom Mozarts <em>Requiem</em>, Bachs <em>Matteuspassionen</em> och Saint-Saëns <em>Juloratorium</em>.",
        "Sedan hösten 2022 har Joel varit anställd vid Finlands Nationalopera. För närvarande är han tjänstledig och gästar bland annat Kungliga Operan i Köpenhamn och Malmö Opera. Hösten 2026 medverkade han som en av gangstrarna i Malmö Operas Europapremiär av Paul Moravecs <em>The Shining</em>, i regi av Keith Warner.",
        "Utöver sina sceniska engagemang anlitas Joel gärna för konserter, kyrkomusik och andra högtidliga tillställningar.",
    ],
    "fi": [
        "Joel Forsström on suomenruotsalainen lyyrinen tenori, joka on saanut laulajan koulutuksensa Tukholmassa muun muassa Stockholm Operastudiossa. Hänet tunnetaan sointuvasta äänestään, lämpimästä esiintyjäpersoonastaan ja vahvasta näyttämöpresenssistään.",
        "Opiskeltuaan laulua Mattias Danielssonin johdolla Joel debytoi solistina Suomen Kansallisoopperassa ja Savonlinnan Oopperajuhlilla kaudella 2016–2017. Sittemmin hän on esiintynyt useissa ooppera- ja musikaalituotannoissa Suomessa ja Ruotsissa.",
        "Hänen oopperarooleihinsa kuuluvat muun muassa Tamino Mozartin <em>Taikahuilussa</em>, Nemorino Donizettin <em>Lemmenjuomassa</em>, prinssi Ramiro Rossinin <em>Tuhkimossa</em> sekä Monostatos <em>Taikahuilussa</em>. Suomen Kansallisoopperassa hän on esiintynyt muun muassa ensimmäisen komissaarin roolissa Poulencin <em>Karmeliittasisarissa</em> ja toisen nasarealaisen roolissa Straussin <em>Salomessa</em>. Kesällä 2025 Joel esitti Monostatosta Ålands Operafestivalin kriitikoiden ylistämässä <em>Taikahuilu</em>-tuotannossa, joka palasi ohjelmistoon kesällä 2026.",
        "Joel on esiintynyt myös musikaaleissa, muun muassa <em>Chessissä</em> Helsingin Svenska Teaternissa. Lisäksi hän on toiminut solistina useissa kirkkomusiikkiteoksissa, kuten Mozartin <em>Requiemissa</em>, Bachin <em>Matteus-passiossa</em> ja Saint-Saënsin <em>Jouluoratoriossa</em>.",
        "Syksystä 2022 lähtien Joel on työskennellyt Suomen Kansallisoopperassa. Tällä hetkellä hän on virkavapaalla ja vierailee muun muassa Kööpenhaminan Kuninkaallisessa oopperassa ja Malmö Operassa. Syksyllä 2026 hän esiintyi yhtenä gangstereista Malmö Operan Paul Moravecin <em>The Shining</em> -oopperan Euroopan kantaesityksessä. Tuotannon ohjasi Keith Warner.",
        "Näyttämötehtäviensä lisäksi Joel esiintyy mielellään konserteissa, kirkkomusiikkitilaisuuksissa ja muissa juhlatilaisuuksissa.",
    ],
}

NEWS = [
    {"when": {"sv": "Hösten 2026", "fi": "Syksy 2026"},
     "title": {"sv": "The Shining – Malmö Opera", "fi": "The Shining – Malmö Opera"},
     "text": {"sv": "Europapremiären av Paul Moravecs opera, i regi av Keith Warner. Dirigent Patrik Ringborg.",
              "fi": "Paul Moravecin oopperan Euroopan kantaesitys, ohjaus Keith Warner, kapellimestari Patrik Ringborg."}},
    {"when": {"sv": "Somrarna 2025 och 2026", "fi": "Kesät 2025 ja 2026"},
     "title": {"sv": "Monostatos – Trollflöjten", "fi": "Monostatos – Taikahuilu"},
     "text": {"sv": "Ålands Operafestival. Kritikerrosad uppsättning i regi av Dan Karlström.",
              "fi": "Ålands Operafestival. Kriitikoiden ylistämä tuotanto, ohjaus Dan Karlström."}},
    {"when": {"sv": "Säsongen 2025/2026", "fi": "Kausi 2025/2026"},
     "title": {"sv": "Gäst i Köpenhamn och Malmö", "fi": "Vierailuja Kööpenhaminassa ja Malmössä"},
     "text": {"sv": "Det Kongelige Teater och Malmö Opera.",
              "fi": "Det Kongelige Teater ja Malmö Opera."}},
]

# id, title per language, featured flag
VIDEOS = [
    {"id": "nYvQSebytp8",
     "title": {"sv": "Una furtiva lagrima", "fi": "Una furtiva lagrima"},
     "sub": {"sv": "Nemorino, Kärleksdrycken (Donizetti)", "fi": "Nemorino, Lemmenjuoma (Donizetti)"}},
    {"id": "QvZrJAwomSg",
     "title": {"sv": "Tamino", "fi": "Tamino"},
     "sub": {"sv": "Trollflöjten (Mozart)", "fi": "Taikahuilu (Mozart)"}},
    {"id": "8dFgRcGA3tA",
     "title": {"sv": "O helga natt", "fi": "O helga natt"},
     "sub": {"sv": "Adolphe Adam. Henrik Wikström, piano. Finlands Luciakröning 2022.",
             "fi": "Adolphe Adam. Henrik Wikström, piano. Suomen Lucian kruunajaiset 2022."}},
    {"id": "R8RB0M-hF70",
     "title": {"sv": "Macduffs aria", "fi": "Macduffin aaria"},
     "sub": {"sv": "Macbeth (Verdi)", "fi": "Macbeth (Verdi)"}},
    {"id": "WQAxPE6s50k",
     "title": {"sv": "”Enemmän”", "fi": "”Enemmän”"},
     "sub": {"sv": "Jaakko Solas aria, Taipaleenjoki (Kuusisto)", "fi": "Jaakko Solan aaria, Taipaleenjoki-ooppera (Kuusisto)"}},
]

# Photo captions are educated guesses from the CV; Joel should confirm them.
PHOTOS = {
    "portratt-2021": {"w": 800, "h": 1200,
        "alt": {"sv": "Porträtt av Joel Forsström i höstlöv", "fi": "Muotokuva Joel Forsströmistä syksyisessä puistossa"},
        "cap": {"sv": "Porträtt", "fi": "Muotokuva"}},
    "tamino-aria": {"w": 2048, "h": 1365,
        "alt": {"sv": "Joel som Tamino sjunger med utsträckta armar", "fi": "Joel Taminona laulaa kädet levällään"},
        "cap": {"sv": "Tamino, Trollflöjten", "fi": "Tamino, Taikahuilu"}},
    "tamino-flojt": {"w": 952, "h": 960,
        "alt": {"sv": "Joel som Tamino med trollflöjten i händerna", "fi": "Joel Taminona taikahuilu käsissään"},
        "cap": {"sv": "Tamino, Trollflöjten", "fi": "Tamino, Taikahuilu"}},
    "monostatos-aland": {"w": 2048, "h": 1365,
        "alt": {"sv": "Joel som Monostatos på knä framför kören på en utomhusscen", "fi": "Joel Monostatoksena polvillaan kuoron edessä ulkonäyttämöllä"},
        "cap": {"sv": "Monostatos, Trollflöjten, Ålands Operafestival", "fi": "Monostatos, Taikahuilu, Ålands Operafestival"}},
    "karmelitsystrarna": {"w": 2048, "h": 1365,
        "alt": {"sv": "Joel i svart rock knäböjer bredvid en nunna på en mörk scen", "fi": "Joel mustassa takissa polvillaan nunnan vieressä pimeällä näyttämöllä"},
        "cap": {"sv": "Förste kommissarien, Karmelitsystrarna, Finlands Nationalopera", "fi": "Ensimmäinen komissaari, Karmeliittasisaret, Suomen Kansallisooppera"}},
    "nemorino-3": {"w": 2000, "h": 1400,
        "alt": {"sv": "Joel sjunger mot svart bakgrund", "fi": "Joel laulaa mustaa taustaa vasten"},
        "cap": {"sv": "Nemorino, Kärleksdrycken, Dala-Floda Operafest", "fi": "Nemorino, Lemmenjuoma, Dala-Floda Operafest"}},
    "nemorino-1": {"w": 1598, "h": 2000,
        "alt": {"sv": "Joel i hängselbyxor med en kvinna i röda glasögon lutad mot ryggen", "fi": "Joel haalareissa, punasankainen nainen nojaa hänen selkäänsä"},
        "cap": {"sv": "Nemorino, Kärleksdrycken", "fi": "Nemorino, Lemmenjuoma"}},
    "nemorino-2": {"w": 1572, "h": 2000,
        "alt": {"sv": "Joel ler förväntansfullt med en flaska i handen", "fi": "Joel hymyilee odottavasti pullo kädessään"},
        "cap": {"sv": "Nemorino, Kärleksdrycken", "fi": "Nemorino, Lemmenjuoma"}},
    "peruk": {"w": 2035, "h": 2048,
        "alt": {"sv": "Joel i 1700-talsperuk och kostym", "fi": "Joel 1700-luvun peruukissa ja puvussa"},
        "cap": {"sv": "I kostym och peruk", "fi": "Puvussa ja peruukissa"}},
}

GALLERY = ["tamino-aria", "monostatos-aland", "karmelitsystrarna", "tamino-flojt",
           "nemorino-3", "nemorino-1", "nemorino-2", "peruk", "portratt-2021"]


def L(sv, fi):
    return {"sv": sv, "fi": fi}


# Roles. Year, role, work, composer, venue, director, conductor.
ROLES = [
    ("2026", L("Maffiaguy 3", "Maffiaguy 3"), L("The Shining", "The Shining"), "P. Moravec",
     L("Malmö Opera", "Malmön ooppera"), "Keith Warner", "Patrik Ringborg"),
    ("2025–2026", L("Monostatos", "Monostatos"), L("Trollflöjten", "Taikahuilu"), "W. A. Mozart",
     L("Ålands Operafestival", "Ålands Operafestival"), "Dan Karlström", "Alberto Hold-Garrido"),
    ("2024", L("Andre nasaréen", "Toinen nasaretilainen"), L("Salome", "Salome"), "R. Strauss",
     L("Finlands Nationalopera", "Suomen Kansallisooppera"), "Christof Loy", "Hannu Lintu"),
    ("2024", L("Förste kommissarien", "Ensimmäinen komissaari"), L("Karmelitsystrarna", "Karmeliittasisaret"), "F. Poulenc",
     L("Finlands Nationalopera", "Suomen Kansallisooppera"), "Olivier Py", "Hannu Lintu"),
    ("2023", L("Nemorino", "Nemorino"), L("Kärleksdrycken", "Lemmenjuoma"), "G. Donizetti",
     L("Dala-Floda Operafest", "Dala-Floda Operafest"), "Christina Ros", "Miguel Ramos"),
    ("2022", L("Tamino", "Tamino"), L("Trollflöjten", "Taikahuilu"), "W. A. Mozart",
     L("Skånska Operan", "Skånska Operan"), "Ola Hörling", "Maria Ingemarsson Berg"),
    ("2021", L("Gherardo", "Gherardo"), L("Gianni Schicchi", "Gianni Schicchi"), "G. Puccini",
     L("Musicum, Kungliga Akademiska Kapellet", "Musicum, Kungliga Akademiska Kapellet"), "Ulric Qvale", "Stefan Karpe"),
    ("2021", L("Jaakko Sola", "Jaakko Sola"), L("Taipaleenjoki", "Taipaleenjoki-ooppera"), "I. Kuusisto",
     L("OperArt, turné i Finland", "OperArt, Suomen-kiertue"), "Juulia Tapola", "Mikk Murdvee"),
    ("2021", L("A-Rab och Glad Hand", "A-Rab & Glad Hand"), L("West Side Story", "West Side Story"), "L. Bernstein",
     L("Savoyteatern, Helsingfors", "Savoy-teatteri, Helsinki"), "Tuomas Parkkinen", "Jonas Rannila"),
    ("2021", L("Tenorsolist", "Tenorisolisti"), L("Operaquiz", "Operaquiz"), "",
     L("Skånska Operan", "Skånska Operan"), "Ola Hörling", ""),
    ("2020", L("Ramiro", "Ramiro"), L("Askungen", "Tuhkimo"), "G. Rossini",
     L("Lemi musikfestspel", "Lemin musiikkijuhlat"), "Anselmi Hirvonen", ""),
    ("2019", L("Jude 3", "3. juutalainen"), L("Salome", "Salome"), "R. Strauss",
     L("Åbo filharmoniska orkester", "Turun filharmoninen orkesteri"), "", "Leif Segerstam"),
    ("2019", L("Don José", "Don José"), L("Carmen", "Carmen"), "G. Bizet",
     L("Lovisa operaförening", "Loviisan oopperayhdistys"), "Päivi Storgårds", "Tomas Takolander"),
    ("2018", L("Amerikanska konsuln / ensemble", "Amerikkalainen konsuli / ensemble"), L("Chess", "Chess"), "B. Andersson / B. Ulvaeus",
     L("Svenska Teatern, Helsingfors", "Svenska Teatern, Helsinki"), "Maria Sid", "Kristian Nyman"),
    ("2018", L("Araldo, Conte di Lerma", "Araldo, Conte di Lerma"), L("Don Carlo", "Don Carlo"), "G. Verdi",
     L("OperaBox / Helden Productions", "OperaBox / Helden Productions"), "Ville Saukkonen", "Jonas Rannila"),
    ("2017", L("Tenorsolist i solokvartetten", "Tenorisolisti solistikvartetissa"), L("Enleveringen ur seraljen", "Ryöstö seraljista"), "W. A. Mozart",
     L("Nyslotts operafestival", "Savonlinnan Oopperajuhlat"), "Katariina Lahti", "Christoph Altstaedt"),
    ("2017", L("Micaëla (”Mikael”)", "Micaëla (”Mikael”)"), L("Carmen", "Carmen"), "G. Bizet",
     L("Dala-Floda Operafest", "Dala-Floda Operafest"), "Lotta Lindqvist", "Alexander Nordwall"),
    ("2016", L("Mengone", "Mengone"), L("Apotekaren (Lo speziale)", "Apteekkari (Lo speziale)"), "J. Haydn",
     L("Savoyteatern, Helsingfors", "Savoy-teatteri, Helsinki"), "Ville Saukkonen", "Tatu Erkkilä"),
    ("2016", L("En av poliserna / ensemble", "Poliisi / ensemble"), L("Lady Macbeth från Mtsensk", "Mtsenskin Lady Macbeth"), "D. Sjostakovitj",
     L("Finlands Nationalopera", "Suomen Kansallisooppera"), "Ole Anders Tandberg", "Oleg Caetani"),
]

CHORUS = [
    ("2025–2026", L("Det Kongelige Teater, Köpenhamn", "Det Kongelige Teater, Kööpenhamina")),
    ("2025–2027", L("Malmö Opera", "Malmön ooppera")),
    ("2022–", L("Finlands Nationalopera", "Suomen Kansallisooppera")),
    ("2021", L("Kungliga Operan, Stockholm", "Kungliga Operan, Tukholma")),
    ("2019–2020", L("Göteborgsoperan", "Göteborgin ooppera")),
    ("2016–2018, 2021", L("Finlands Nationalopera", "Suomen Kansallisooppera")),
    ("2017", L("Folkoperan, Stockholm", "Folkoperan, Tukholma")),
    ("2013–2018", L("Nyslotts operafestival", "Savonlinnan Oopperajuhlat")),
]

CONCERTS = [
    ("2024", L("Juloratorium", "Jouluoratorio"), "C. Saint-Saëns", L("Lovisa kyrka", "Loviisan kirkko"), "Tomas Takolander"),
    ("2022", L("O helga natt, tenorsolist", "O helga natt, tenorisolisti"), "A. Adam",
     L("Finlands Luciakröning, direktsänd i Yle", "Suomen Lucian kruunajaiset, suora lähetys Ylellä"), ""),
    ("2019", L("Matteuspassionen", "Matteus-passio"), "J. S. Bach", L("Haapavesi och Haapajärvi kyrkor", "Haapaveden ja Haapajärven kirkot"), "Timo Hannula"),
    ("2017", L("Juloratorium", "Jouluoratorio"), "C. Saint-Saëns", L("Mariakyrkan, Sigtuna", "Marian kirkko, Sigtuna"), "Mathias Kjellgren"),
    ("2016", L("Requiem", "Requiem"), "W. A. Mozart", L("Mejlans kyrka, Helsingfors", "Meilahden kirkko, Helsinki"), "Pete Vuorio"),
]

EDUCATION = [
    ("2014–2015", L("Klassisk sång", "Klassinen laulu"), "Birkagårdens folkhögskola"),
    ("2011–2013", L("Operasångare", "Oopperalaulaja"), "Operastudio Stockholm"),
    ("2010–2011", L("Klassisk sång", "Klassinen laulu"), "Kulturama"),
]

TEACHERS = "Mattias Danielsson, Franco Pomponi, Ron La Fond, Dale Fundling"

MASTERCLASSES = [
    ("2025", "Arwel T. Morgan", L("Skåne", "Skåne")),
    ("2020", "Karita Mattila", L("Helsingfors", "Helsinki")),
    ("2019", "Mikko Franck & Rilla Kyykkä", L("Kangasniemi", "Kangasniemi")),
    ("2019", "Karita Mattila", L("Birgit Nilsson-museet", "Birgit Nilsson -museo")),
]
