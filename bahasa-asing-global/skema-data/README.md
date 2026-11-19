# Skema Data Bahasa Global LWT

## Tujuan dan hubungan entitas

Skema memisahkan tiga jenis entitas:

- **Negara/wilayah:** konteks geografis dan administratif.
- **Bahasa:** sistem bahasa dengan identitas tersendiri.
- **Variasi:** aksen, dialek, register, slang, dan gaya komunikasi yang terkait dengan bahasa serta komunitas tertentu.

Satu negara dapat memiliki banyak bahasa. Satu bahasa dapat digunakan di banyak negara. Negara adalah titik navigasi, bukan pemilik eksklusif bahasa.

## Enam kategori wajib

| Urutan | Kunci | Isi |
|---|---|---|
| 1 | `accent_and_pronunciation` | Aksen, logat, bunyi, intonasi, tekanan, ritme, dan audio/fonetik bila tersedia. |
| 2 | `speaking_style_and_pragmatics` | Sapaan, kesopanan, giliran bicara, gaya langsung/tidak langsung, dan konteks sosial. |
| 3 | `standard_language` | Bentuk baku, tata bahasa, ejaan, kosakata formal, dan penggunaan resmi. |
| 4 | `nonstandard_language_and_slang` | Percakapan, slang, singkatan, bahasa internet, dan variasi generasi. |
| 5 | `profanity_and_vulgar_language` | Umpatan, kata kasar, makna, intensitas, sasaran, konteks, dan risiko penggunaan. |
| 6 | `regional_and_minority_languages` | Bahasa daerah/minoritas/Indigenous, dialek, komunitas, wilayah, dan rujukan profil terpisah. |

## Format entri profil bahasa

Berkas profil menggunakan `schema_version: 1.1.0`. Setiap kategori berisi `status`, `entries`, dan catatan cakupan bila diperlukan.

Setiap entri memakai bidang berikut:

- `id`: ID stabil dan unik di seluruh repositori.
- `term`: lema, ungkapan, atau fenomena bahasa.
- `reading`: pelafalan/transliterasi jika relevan.
- `explanation_id`: penjelasan dalam bahasa Indonesia.
- `indonesian_learning_link`: cara konsep tersebut membantu pengguna belajar bahasa Indonesia.
- `region`: negara, wilayah, atau komunitas tempat bentuk/fenomena digunakan.
- `register`: baku, informal, slang, vulgar, regional, atau label kontekstual lain.
- `usage_context`: situasi atau fungsi pemakaian.
- `example_source_language`: contoh atau representasi dalam bahasa asal.
- `example_indonesian`: contoh/padanan yang mengarah pada pembelajaran bahasa Indonesia.
- `sources`: satu atau lebih URL rujukan ketika tersedia.
- `verification_status`: `draft`, `reviewed`, atau `verified`.
- `note`: batasan, variasi, atau catatan editorial jika ada.

Untuk fenomena fonologi, `term` dapat berupa nama fenomena dan `example_source_language` berisi kata/bentuk bunyi. Jangan memaksakan terjemahan literal jika yang diajarkan adalah pola bunyi atau pragmatik.

## Status verifikasi

- **draft:** catatan awal; bukti, distribusi, atau konteks belum cukup.
- **reviewed:** telah diperiksa terhadap rujukan yang dicantumkan, tetapi belum tentu divalidasi penutur asli.
- **verified:** sumber kuat dan pemeriksaan ahli/penutur asli telah terdokumentasi. Status ini tidak boleh diberikan otomatis hanya karena entri memiliki tautan.

Status profil `content_seeded_reviewed_not_native_validated` berarti materi awal telah disusun dan ditautkan, tetapi belum mendapat validasi ahli/penutur asli secara menyeluruh.

## Prinsip pemetaan ke bahasa Indonesia

LWT adalah guru bahasa Indonesia. Bahasa asal digunakan sebagai jembatan, bukan menjadi tujuan kursus.

- Konsep sapaan dalam bahasa asal → sapaan bahasa Indonesia yang sesuai.
- Perbedaan register → pilihan bahasa Indonesia baku/nonbaku.
- Umpatan → penjelasan padanan Indonesia dengan intensitas, target, dan konteks.
- Aksen bahasa asal → panduan pelafalan bunyi bahasa Indonesia yang berpotensi sulit bagi penutur tersebut.
- Contoh terjemahan harus alami, tidak sekadar menyalin struktur bahasa asal.

## Pengendalian mutu

- Jangan mengarang kosakata, aksen, kode bahasa, atau aturan.
- Jangan menyebut variasi satu komunitas sebagai kebiasaan seluruh negara.
- Bedakan bahasa, keluarga bahasa, dialek, aksen, dan register.
- Cantumkan tanggal pemeriksaan dan sumber yang dapat ditelusuri.
- Tandai tren slang dengan tahun dan komunitas pemakai jika diketahui.
- Umpatan tetap dijelaskan secara terbuka, tetapi jangan dilepaskan dari konteks atau risiko sosial.
- Validasi manual sebelum status `verified`.
