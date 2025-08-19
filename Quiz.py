# simple quiz
pertanyaan = ("Kapan kita melaksanakan upacara bendera rutin?",
              "Siapa hewan tercepat di dunia?",
              "Mengapa kita perlu mengenyam pendidikan formal?",
              "Kenapa kita mempunyai sifat pemalas?",
              "Agama mana yang benar?"
                                                           )

pilihan = (("A. Senin", "B. Selasa", "C. Jumat", "D. Rabu"),
           ("A. Cheetah", "B. Alap2 kawah", "C. Elang emas", "D. Kelelawar ekor brasil"),
           ("A. Untuk pengetahuan dan keterampilan", "B. Untuk memperoleh koneksi", "C. Persiapan dunia kerja", "D. Semua jawaban benar"),
           ("A. Pengaruh teknologi", "B. Kebiasaan buruk", "C. Tidak punya motivasi", "D. Zona nyaman"),
           ("A. Krister", "B. Budha","C. Islam","D. Sesuai kepercayaan masing2"))

jawaban = ("A", "A", "C","D","D")
tebakan = []
score = 0
soal_no = 0

for tanya in pertanyaan:
    print("----------------------------")
    print(tanya)
    for pilih in pilihan[soal_no]:
        print(pilih)

    tebak = input("Masukan jawaban: (A, B, C, D): ").upper()
    tebakan.append(tebak)
    if tebak == jawaban[soal_no]:
        score += 1
    else:
        print("Jawaban Salah!")
        print(f"{jawaban[soal_no]} adalah jawaban yang benar")

    soal_no += 1

print("------Hasil Akhir-------")
print("jawaban: ", end="")
for jawab in jawaban:
    print(jawab, end="")
print()

print("------Hasil Akhir-------")
print("tebakan: ", end="")
for tebak in tebakan:
    print(tebak, end="")
print()

score = int(score/len(pertanyaan) * 100)
print(f"Scoremu: {score}")