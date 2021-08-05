# SPDX-FileCopyrightText: 2021 Tuomas Siipola
# SPDX-License-Identifier: MIT

import unittest
import unicodedata
import kyrlat

class TestRomanize(unittest.TestCase):
    def __init__(self, romanize, text, expected):
        super().__init__('test')
        self.romanize = romanize
        self.text = text
        self.expected = expected

    def test(self):
        self.assertEqual(self.romanize(self.text), self.expected)

def test_suite(romanize, test_cases):
    suite = unittest.TestSuite()
    for text, expected in test_cases:
        for form in ('NFC', 'NFKC', 'NFD', 'NFKD'):
            for quote in ('\u0027', '\u2019', '\u02bc'):
                t = text.replace('\u02bc', quote)
                suite.addTest(TestRomanize(romanize, unicodedata.normalize(form, t), expected))
                suite.addTest(TestRomanize(romanize, unicodedata.normalize(form, t.upper()), expected.upper()))
                suite.addTest(TestRomanize(romanize, unicodedata.normalize(form, 'látin ' + t + ' làtin'), 'látin ' + expected + ' làtin'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    # https://fi.wikipedia.org/wiki/Ven%C3%A4j%C3%A4n_translitterointi
    runner.run(test_suite(kyrlat.romanize_ru, [
        ('Анапа', 'Anapa'), ('Бабаево', 'Babajevo'),
        ('Всеволожск', 'Vsevoložsk'), ('Гагарин', 'Gagarin'),
        ('Дедовск', 'Dedovsk'), ('Дальнереченск', 'Dalneretšensk'),
        ('Егорьевск', 'Jegorjevsk'), ('Гаджиево', 'Gadžijevo'),
        ('Горбачёв', 'Gorbatšov'), ('Тимашёвск', 'Timašovsk'),
        ('Хрущёв', 'Hruštšov'), ('Королёв', 'Koroljov'),
        ('Железнодорожный', 'Železnodorožnyi'), ('Заозёрск', 'Zaozjorsk'),
        ('Ишим', 'Išim'), ('Краснотурьинск', 'Krasnoturjinsk'),
        ('Ясный', 'Jasnyi'), ('Валдайский район', 'Valdaiski raion'),
        ('Каспийск', 'Kaspijsk'), ('Йошкар-Ола', 'Joškar-Ola'),
        ('Чайковский', 'Tšaikovski'), ('Копейск', 'Kopeisk'),
        ('Лихославль', 'Lihoslavl'), ('Мурманск', 'Murmansk'),
        ('Ногинск', 'Noginsk'), ('Олонец', 'Olonets'), ('Почеп', 'Potšep'),
        ('Рязань', 'Rjazan'), ('Сестрорецк', 'Sestroretsk'),
        ('Тольятти', 'Toljatti'), ('Уссурийск', 'Ussurijsk'),
        ('Фатеж', 'Fatež'), ('Хабаровск', 'Habarovsk'),
        ('Цивильск', 'Tsivilsk'), ('Чита', 'Tšita'), ('Шушары', 'Šušary'),
        ('Щёлково', 'Štšolkovo'), ('субъект', 'subjekt'), ('Кызыл', 'Kyzyl'),
        ('Козьмодемьянск', 'Kozmodemjansk'), ('Энгельс', 'Engels'),
        ('Юрюзань', 'Jurjuzan'), ('Ярославль', 'Jaroslavl'),
        ('Дми́трий Нарки́сович Ма́мин-Сибиря́к', 'Dmitri Narkisovitš Mamin-Sibirjak'),
    ]))

    # https://fi.wikipedia.org/wiki/Ukrainan_translitterointi
    runner.run(test_suite(kyrlat.romanize_uk, [
        ('Алушта', 'Alušta'), ('Бобринець', 'Bobrynets'),
        ('Вишневе', 'Vyšneve'), ('Генічеськ', 'Henitšesk'),
        ('Ґалаґан', 'Galagan'), ('Дніпродзержинськ', 'Dniprodzeržynsk'),
        ('Енергодар', 'Enerhodar'), ('Єнакієве', 'Jenakijeve'),
        ('Житомир', 'Žytomyr'), ('Запоріжжя', 'Zaporižžja'),
        ('Винники', 'Vynnyky'), ('Іллічівськ', 'Illitšivsk'),
        ('Ізмаїл', 'Izmajil'), ('Їжакевич', 'Jižakevytš'),
        ('Красноармійськ', 'Krasnoarmijsk'), ('Гайсин', 'Haisyn'),
        ('Хмельницький', 'H\u02bcmelnytskyi'), ('Григорій', 'Hryhori'),
        ('Красноперекопськ', 'Krasnoperekopsk'),
        ('Лохвиця', 'Loh\u02bcvytsja'), ('Миколаїв', 'Mykolajiv'),
        ('Нетішин', 'Netišyn'), ('Острог', 'Ostroh'),
        ('Прип\u02bcять', 'Prypjat'), ('Рахів', 'Rah\u02bciv'),
        ('Севастополь', 'Sevastopol'), ('Тальне', 'Talne'), ('Умань', 'Uman'),
        ('Феодосія', 'Feodosija'), ('Христинівка', 'H\u02bcrystynivka'),
        ('Цюрупинськ', 'Tsjurupynsk'), ('Чугуїв', 'Tšuhujiv'),
        ('Шепетівка', 'Šepetivka'), ('Щастя', 'Štšastja'), ('Южне', 'Južne'),
        ('Ялта', 'Jalta'), ('Комсомольськ', 'Komsomolsk'),
        ('Куп\u02bcянськ', 'Kupjansk'),
        ('Миха́йло Пана́сович Сте́льмах', 'Myh\u02bcailo Panasovytš Stelmah\u02bc')
    ]))

    # https://fi.wikipedia.org/wiki/Valkoven%C3%A4j%C3%A4n_translitterointi
    runner.run(test_suite(kyrlat.romanize_be, [
        ('Ашмяны', 'Ašmjany'), ('Бабруйск', 'Babruisk'),
        ('Ваўкавыск', 'Vaukavysk'), ('Гомель', 'Homel'),
        ('Давыд-Гарадок', 'Davyd-Haradok'), ('Петрыкаў', 'Petrykau'),
        ('Ельск, Лоеў', 'Jelsk, Lojeu'), ('Міёры', 'Mijory'),
        ('Жодзіна', 'Žodzina'), ('Зарэчча', 'Zaretštša'),
        ('Івацэвічы', 'Ivatsevitšy'), ('Вілейка', 'Vileika'),
        ('Лаўрэнцій', 'Laurentsi'), ('Крупкі', 'Krupki'), ('Лепель', 'Lepel'),
        ('Магілёў', 'Mahiljou'), ('Нароўля', 'Naroulja'), ('Орша', 'Orša'),
        ('Пінск', 'Pinsk'), ('Рагачоў', 'Rahatšou'), ('Свіслач', 'Svislatš'),
        ('Татарка', 'Tatarka'), ('Узда', 'Uzda'), ('Быхаў', 'Byh\u02bcau'),
        ('Фаніпаль', 'Fanipal'), ('Хойнікі', 'H\u02bcoiniki'),
        ('Церахаўка', 'Tserah\u02bcauka'), ('Чачэрск', 'Tšatšersk'),
        ('Шаркаўшчына', 'Šarkauštšyna'),
        ('Мар\u02bcіна Горка', 'Marina Horka'), ('Докшыцы', 'Dokšytsy'),
        ('Лельчыцы', 'Leltšytsy'), ('Эмэрык', 'Emeryk'),
        ('Юрацішкі', 'Juratsiški'), ('Янавічы', 'Janavitšy'),
        ('Вінцэ́нт-Яку́б Ду́нін-Марцінке́віч', 'Vintsent-Jakub Dunin-Martsinkevitš'),
    ]))

    # https://fi.wikipedia.org/wiki/Bulgarian_translitterointi
    runner.run(test_suite(kyrlat.romanize_bg, [
        ('Асеновград', 'Asenovgrad'), ('Бобошево', 'Boboševo'),
        ('Велики Преслав', 'Veliki Preslav'), ('Габрово', 'Gabrovo'),
        ('Димитровград', 'Dimitrovgrad'), ('Елена', 'Elena'),
        ('Кнежа', 'Kneža'), ('Завет', 'Zavet'), ('Ихтиман', 'Ihtiman'),
        ('Стамболийски', 'Stambolijski'), ('Йордан', 'Jordan'),
        ('Ивайловград', 'Ivailovgrad'), ('Куклен', 'Kuklen'),
        ('Летница', 'Letnitsa'), ('Момчилград', 'Momtšilgrad'),
        ('Неделино', 'Nedelino'), ('Оряхово', 'Orjahovo'),
        ('Попово', 'Popovo'), ('Радомир', 'Radomir'), ('Силистра', 'Silistra'),
        ('Тръстеник', 'Trăstenik'), ('Сунгурларе', 'Sungurlare'),
        ('Алфатар', 'Alfatar'), ('Харманли', 'Harmanli'),
        ('Царево', 'Tsarevo'), ('Чепеларе', 'Tšepelare'), ('Шумен', 'Šumen'),
        ('Свищов', 'Svištov'), ('Гълъбово', 'Gălăbovo'), ('Пирьов', 'Pirjov'),
        ('Тюленово', 'Tjulenovo'), ('Ямбол', 'Jambol'), ('Лѣсново', 'Lesnovo'),
    ]))

    # https://fi.wikipedia.org/wiki/Makedonian_translitterointi
    runner.run(test_suite(kyrlat.romanize_mk, [
        ('Ацева', 'Aceva'), ('Битола', 'Bitola'), ('Валандово', 'Valandovo'),
        ('Гевгелија', 'Gevgelija'), ('Делчево', 'Delčevo'),
        ('Ѓорѓи', 'G\u02bcorg\u02bci'), ('Енчев', 'Enčev'),
        ('Жарноски', 'Žarnoski'), ('Захов', 'Zahov'), ('Ѕвезда', 'Dzvezda'),
        ('Илиевски', 'Ilievski'), ('Јоциќ', 'Jocik\u02bc'),
        ('Крчовски', 'Krčovski'), ('Лилјана', 'Liljana'), ('Љупчо', 'Ljupčo'),
        ('Михајло', 'Mihajlo'), ('Неготино', 'Negotino'), ('Охрид', 'Ohrid'),
        ('Прилеп', 'Prilep'), ('Радовиш', 'Radoviš'), ('Скопје', 'Skopje'),
        ('Тетово', 'Tetovo'), ('Ќушкоски', 'K\u02bcuškoski'),
        ('Урошевиќ', 'Uroševik\u02bc'), ('Фотев', 'Fotev'), ('Хаџи', 'Hadži'),
        ('Цветкоски', 'Cvetkoski'), ('Чачански', 'Čačanski'),
        ('Џаџев', 'Džadžev'), ('Шеќероски', 'Šek\u02bceroski'),
    ]))
