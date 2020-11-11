from googletrans import Translator
text_input = (input("Masukan teks: "))
text_go = (input("Masukan arah terjemah: "))
terjemah = Translator()
done_translate = terjemah.translate(text_input,text_go)
print(done_translate.text)

#untuk daftar kode bahasa bisa kunjungi situs ini https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
