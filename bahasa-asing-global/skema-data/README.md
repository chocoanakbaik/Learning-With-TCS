# Skema Data Bahasa Global LWT

## Tujuan

Skema ini memisahkan tiga entitas yang sering tercampur:

- **Negara/wilayah:** lokasi geografis dan konteks administratif.
- **Bahasa:** sistem bahasa dengan identitas tersendiri.
- **Variasi:** aksen, dialek, register, slang, dan gaya komunikasi yang terkait dengan bahasa serta komunitas tertentu.

Satu negara dapat memiliki banyak bahasa. Satu bahasa juga dapat digunakan di banyak negara. Karena itu, data bahasa tidak boleh disimpan seolah-olah hanya dimiliki satu negara.

## Enam kelompok materi

| Urutan | Kunci data | Isi |
|---|---|---|
| 1 | `accent_and_pronunciation` | Aksen, logat, bunyi, intonasi, tekanan, ritme, contoh audio/fonetik bila tersedia |
| 2 | `speaking_style_and_pragmatics` | Sapaan, kesopanan, giliran bicara, gaya langsung/tidak langsung, konteks sosial |
| 3 | `standard_language` | Bentuk baku, tata bahasa, ejaan, kosakata formal, penggunaan resmi |
| 4 | `nonstandard_language_and_slang` | Bahasa percakapan, slang, singkatan, bahasa internet, variasi generasi |
| 5 | `profanity_and_vulgar_language` | Umpatan, kata kasar, makna, intensitas, sasaran, konteks, dan peringatan penggunaan |
| 6 | `regional_and_minority_languages` | Bahasa daerah, bahasa minoritas, bahasa adat, dialek, komunitas, dan wilayah |

## Format setiap entri

Entri kosakata/ungkapan sebaiknya memiliki bidang berikut:

- `id`: ID stabil dan unik.
- `term`: kata atau ungkapan asli.
- `normalized_form`: bentuk normalisasi bila diperlukan.
- `language_code`: kode bahasa ISO 639.
- `region`: negara, wilayah, atau komunitas tempat bentuk tersebut digunakan.
- `category`: salah satu dari enam kelompok materi.
- `meaning`: arti yang jelas dalam bahasa Indonesia.
- `literal_meaning`: arti harfiah bila berbeda dari makna pemakaian.
- `indonesian_equivalent`: padanan bahasa Indonesia, jika ada.
- `register`: formal, informal, slang, vulgar, archaic, atau lainnya.
- `intensity`: tingkat kekasaran/ketajaman bila relevan.
- `usage_context`: situasi penggunaan.
- `example_original`: contoh dalam bahasa asal.
- `example_indonesian`: contoh/padanan dalam bahasa Indonesia.
- `cultural_notes`: catatan budaya dan potensi salah tafsir.
- `sources`: sumber yang mendukung entri.
- `verification_status`: draft, reviewed, atau verified.

Tidak semua bidang harus terisi untuk setiap jenis data, tetapi arti, identitas bahasa, konteks, dan sumber wajib tersedia sebelum entri dinyatakan verified.

## Prinsip pemetaan ke bahasa Indonesia

LWT adalah guru bahasa Indonesia. Bahasa asal digunakan untuk menjelaskan materi, bukan menjadi tujuan kursus. Setiap unit belajar perlu mengarah pada kemampuan memahami atau menggunakan bahasa Indonesia.

Contoh arah pemetaan:

- Konsep sapaan dalam bahasa asal → sapaan bahasa Indonesia yang sesuai.
- Perbedaan register dalam bahasa asal → perbedaan baku dan nonbaku dalam bahasa Indonesia.
- Umpatan dalam bahasa asal → penjelasan padanan umpatan Indonesia beserta intensitas dan konteksnya.
- Aksen bahasa asal → panduan pelafalan bunyi bahasa Indonesia yang sering sulit bagi penutur tersebut.

## Pengendalian mutu

- Bedakan fakta, variasi regional, pendapat penutur, dan slang yang sedang tren.
- Jangan menyebut suatu ungkapan sebagai bahasa seluruh negara jika hanya dipakai komunitas tertentu.
- Umpatan harus dijelaskan secara edukatif, tidak disamarkan, tetapi juga tidak dilepaskan dari konteks.
- Sertakan sumber yang dapat ditelusuri dan tanggal pemeriksaan.
- Gunakan status `draft` sampai diperiksa; status `verified` memerlukan sumber yang memadai.
