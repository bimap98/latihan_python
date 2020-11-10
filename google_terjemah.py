from googletrans import Translator

translator = Translator()
translations = translator.translate(input("Masukan teks: "), input("Masukan kode bahasa tujuan: "))  
# print(translations)
print(translations.pronunciation)
print(translations.text)

#untuk daftar kode bahasa bisa kunjungi situs ini https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


