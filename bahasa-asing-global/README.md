# Bahasa Asing Global

Direktori ini menjadi fondasi basis pengetahuan bahasa global untuk **Learn with TCS (LWT)**.

## Misi LWT

LWT membantu penutur dari berbagai negara mempelajari **bahasa Indonesia**. Arah pembelajaran bersifat satu arah:

**Bahasa asal/pengantar pengguna → Bahasa Indonesia**

LWT bukan penerjemah dua arah dan bukan kursus untuk mengajarkan bahasa asing kepada penutur bahasa Indonesia.

## Cakupan data per negara dan komunitas bahasa

Setiap negara dapat memiliki satu atau lebih bahasa, variasi regional, serta komunitas penutur lintas negara. Karena itu, negara dipakai sebagai titik navigasi, bukan dianggap sama dengan satu bahasa.

Setiap profil negara/komunitas bahasa disusun dengan urutan kategori berikut:

1. **Logat dan aksen** — variasi pelafalan, tekanan, intonasi, ritme, dan ciri bunyi. Catat wilayah/komunitasnya; jangan menggeneralisasi seluruh penduduk negara.
2. **Cara bicara** — tingkat kesopanan, sapaan, kebiasaan percakapan, ekspresi, konteks sosial, dan gaya komunikasi.
3. **Bahasa baku** — bahasa standar/formal yang digunakan dalam pendidikan, dokumen, media resmi, atau konteks profesional.
4. **Bahasa nonbaku** — percakapan sehari-hari, slang, singkatan, variasi anak muda, istilah internet, dan ungkapan lokal.
5. **Bahasa umpatan dan kata kasar** — arti literal, tingkat kekasaran, sasaran/nuansa, konteks, risiko menyinggung, serta padanan penjelasan dalam bahasa Indonesia. Materi ini bersifat edukatif dan kontekstual, bukan ajakan menyerang orang.
6. **Bahasa daerah dan minoritas** — bahasa lokal, bahasa adat/indigenous, bahasa komunitas, dialek, wilayah penggunaan, dan status dokumentasinya.

## Hubungan dengan materi bahasa Indonesia

Tujuan akhir setiap materi adalah membantu pengguna memahami bahasa Indonesia. Setiap entri pembelajaran idealnya menghubungkan:

- istilah atau konsep dari bahasa asal pengguna;
- bentuk bahasa Indonesia yang relevan;
- arti dan nuansa;
- contoh kalimat bahasa Indonesia;
- konteks pemakaian;
- tingkat formalitas/kekasaran;
- catatan budaya dan wilayah;
- sumber rujukan dan status verifikasi.

Materi bahasa Indonesia yang diajarkan tetap dibagi menjadi:
- **Baku:** bentuk standar dan penggunaan formal.
- **Nonbaku:** percakapan, slang, singkatan, dan ungkapan sehari-hari.
- **Umpatan/kata kasar:** pemahaman arti, nuansa, dan konteks secara terbuka serta bertanggung jawab.
- **Bahasa daerah Indonesia:** bahasa dan variasi lokal di seluruh wilayah Indonesia.

## Struktur direktori

```text
bahasa-asing-global/
├── README.md
├── FASE-01-README.md
├── template-negara/
│   ├── README.md
│   └── profil-negara.template.json
├── skema-data/
│   └── README.md
├── tools/
│   └── validate_language_data.py
└── negara/
    ├── README.md
    ├── US/
    │   ├── country.json
    │   └── languages/<kode-bahasa>/profile.json
    ├── JP/
    │   ├── country.json
    │   └── languages/<kode-bahasa>/profile.json
    └── CN/
        ├── country.json
        └── languages/<kode-bahasa>/profile.json
```

Profil negara baru dibuat di dalam `negara/` menggunakan kode negara ISO 3166-1 alpha-2, misalnya `US/`, `JP/`, atau `BR/`. Di dalamnya, pisahkan profil negara dari profil bahasa/komunitas agar bahasa yang digunakan lintas negara tidak diduplikasi secara keliru.

## Standar identifikasi

- Gunakan **ISO 3166-1 alpha-2** untuk identitas negara.
- Gunakan **ISO 639-3** jika identitas bahasa terkonfirmasi.
- Gunakan tag bahasa/region BCP 47 jika perlu menandai variasi bahasa berdasarkan wilayah, misalnya `en-US`.
- Jika kode ISO 639-3 belum terkonfirmasi, jangan mengarang kode. Glottocode dapat dicatat sebagai pengenal tambahan yang berbeda dari ISO.
- Dialek atau aksen tidak otomatis dianggap bahasa terpisah. Catat sebagai variasi dari bahasa terkait kecuali ada dasar linguistik yang dapat dipertanggungjawabkan.

Rujukan:
- [ISO 639:2023](https://www.iso.org/standard/74575.html)
- [ISO 639 Language Code](https://www.iso.org/iso-639-language-code)
- [Library of Congress: ISO 639 FAQ](https://www.loc.gov/standards/iso639-2/faq.html)

## Aturan mutu dan editorial

1. Jangan mengarang kosakata, aksen, atau aturan bahasa.
2. Jangan menyamakan bahasa nasional, bahasa resmi, bahasa mayoritas, dan bahasa daerah.
3. Sertakan sumber, wilayah, komunitas, tanggal pemeriksaan, dan tingkat keyakinan pada data faktual.
4. Berikan contoh yang alami dan jelaskan konteks sosialnya.
5. Kata kasar tidak dihapus hanya karena kasar; jelaskan makna, intensitas, dan risiko pemakaiannya.
6. Tandai data yang belum diverifikasi sebagai `draft`, bukan fakta final.
7. Hormati penutur dan komunitas bahasa; hindari stereotip nasional atau etnis.
8. Perubahan skema harus menjaga kompatibilitas data lama.

## Status Fase 1

Audit ulang seluruh 33 profil pada branch `main` tanggal **19 November 2026** menghasilkan:

| Negara | Record katalog | Profil | Entri |
|---|---:|---:|---:|
| Amerika Serikat | 12 | 10 | 228 |
| Jepang | 9 | 9 | 141 |
| Tiongkok | 14 | 14 | 130 |
| **Total** | **35** | **33** | **499** |

Status entri: **397 reviewed, 102 draft, 0 verified**. Distribusi kategori: 112 accent/pronunciation, 68 speaking style/pragmatics, 120 standard language, 44 nonstandard/slang, 37 profanity/vulgar language, dan 118 regional/minority languages.

Dua record AS masih berupa label payung Chinese language groups dan Arabic varieties, bukan profil bahasa individual. Hachijo sudah memiliki profil menggunakan Glottocode `hach1239`, sementara `iso_639_3` tetap `null` karena tidak ada kode ISO 639-3 yang terkonfirmasi.

[Dokumentasi rinci Fase 1](./FASE-01-README.md) memuat daftar profil, batas cakupan varietas, distribusi entri, dan pekerjaan yang masih terbuka.

## Validasi

- [Validator data](./tools/validate_language_data.py) — pemeriksaan JSON, kategori, field entri, status, sumber, ID unik, dan hubungan katalog/profil.
- Jalankan dari root repository: `python bahasa-asing-global/tools/validate_language_data.py`.

Pemeriksaan otomatis hanya menguji struktur dan konsistensi data. Pemeriksaan itu tidak membuktikan ketepatan linguistik, kewajaran contoh, atau penerimaan komunitas. Belum ada entri berstatus `verified` karena proses validasi penutur asli/ahli belum terdokumentasi.

Cakupan katalog ini masih terpilih dan bukan inventaris lengkap seluruh bahasa, dialek, atau kosakata di ketiga negara. Peninjauan penutur asli/ahli, penambahan rekaman berlisensi, dan pengembangan bahasa komunitas lainnya tetap diperlukan.
