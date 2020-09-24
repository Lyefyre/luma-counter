from django.db import models

class CounterNumber(models.Model):
    species = [
        ("Oree", "Oree"),
        ("Zaobian", "Zaobian"),
        ("Platypet", "Platypet"),
        ("Platox", "Platox"),
        ("Platimous", "Platimous"),
        ("Swali", "Swali"),
        ("Loali", "Loali"),
        ("Tateru", "Tateru"),
        ("Paharo", "Paharo"),
        ("Paharac", "Paharac"),
        ("Granpah", "Granpah"),
        ("Ampling", "Ampling"),
        ("Amphatyr", "Amphatyr"),
        ("Bunbun", "Mudrid"),
        ("Hidody", "Hidody"),
        ("Taifu", "Taifu"),
        ("Fomu", "Fomu"),
        ("Wiplump", "Wiplump"),
        ("Skail", "Skail"),
        ("Skunch", "Skunch"),
        ("Goty", "Goty"),
        ("Mouflank", "Mouflank"),
        ("Rhoulder", "Rhoulder"),
        ("Houchic", "Houchic"),
        ("Tental", "Tental"),
        ("Nagaise", "Nagaise"),
        ("Orphyll", "Orphyll"),
        ("Nidrasil", "Nidrasil"),
        ("Banapi", "Capyre"),
        ("Lapinite", "Lapinite"),
        ("Azuroc", "Azuroc"),
        ("Zenoreth", "Zenoreth"),
        ("Bigu", "Bigu"),
        ("Babawa", "Babawa"),
        ("Kaku", "Kaku"),
        ("Saku", "Saku"),
        ("Valash", "Valash"),
        ("Barnshe", "Barnshe"),
        ("Gyalis", "Gyalis"),
        ("Occlura", "Occlura"),
        ("Myx", "Myx"),
        ("Raiber", "Raiber"),
        ("Raize", "Raize"),
        ("Raican", "Raican"),
        ("Pewki", "Pewki"),
        ("Piraniant", "Piraniant"),
        ("Osuchi", "Osuchi"),
        ("Osukan", "Osukan"),
        ("Osukai", "Osukai"),
        ("Saipat", "Saipat"),
        ("Pycko", "Pycko"),
        ("Drakash", "Drakash"),
        ("Crystle", "Crystle"),
        ("Sherald", "Sherald"),
        ("Tortenite", "Tortenite"),
        ("Hocus", "Hocus"),
        ("Pocus", "Pocus"),
        ("Sparzy", "Sparzy"),
        ("Mushi", "Mushi"),
        ("Mushook", "Mushook"),
        ("Magmis", "Magmis"),
        ("Mastione", "Mastione"),
        ("Umishi", "Umishi"),
        ("Ukama", "Ukama"),
        ("Raignet", "Raignet"),
        ("Smazee", "Smazee"),
        ("Baboong", "Baboong"),
        ("Seismunch", "Seismunch"),
        ("Zizare", "Zizare"),
        ("Kuri", "Kuri"),
        ("Kauren", "Kauren"),
        ("Spriole", "Spriole"),
        ("Deendre", "Deendre"),
        ("Cerneaf", "Cerneaf"),
        ("Toxolotl", "Toxolotl"),
        ("Noxolotl", "Noxolotl"),
        ("Blooze", "Blooze"),
        ("Goolder", "Goolder"),
        ("Zephyruff", "Zephyruff"),
        ("Volarend", "Volarend"),
        ("Grumvel", "Grumvel"),
        ("Grumper", "Grumper"),
        ("Ganki", "Ganki"),
        ("Gazuma", "Gazuma"),
        ("Oceara", "Oceara"),
        ("Yowlar", "Yowlar"),
        ("Droply", "Droply"),
        ("Garyo", "Garyo"),
        ("Shuine", "Shuine"),
        ("Nessla", "Nessla"),
        ("Valiar", "Valiar"),
        ("Kalazu", "Kalazu"),
        ("Kalabyss", "Kalabyss"),
        ("Adoroboros", "Adoroboros"),
        ("Tuwai", "Tuwai"),
        ("Tukai", "Tukai"),
        ("Tuvine", "Tuvine"),
        ("Turoc", "Turoc"),
        ("Kinu", "Kinu"),
        ("Vulvir", "Vulvir"),
        ("Vulor", "Vulor"),
        ("Vulcrane", "Vulcrane"),
        ("Pigepic", "Pigepic"),
        ("Akranox", "Akranox"),
        ("Vulffy", "Vulffy"),
        ("Anahir", "Anahir")
    ]
    species = models.CharField(choices=species, max_length=200, unique=True, default="")
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.species