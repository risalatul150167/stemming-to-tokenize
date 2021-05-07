from nltk.tokenize import sent_tokenize, word_tokenize

kalimat = "saya bangga jadi warga nahdlatul ulama"

for kata in word_tokenize(kalimat):
    print (kata)

jumlah = kalimat.split()
hitung = len(jumlah)

print("jumlah kata : ", hitung)
