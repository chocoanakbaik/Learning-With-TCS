# Fase 01 — Amerika Serikat, Jepang, dan Tiongkok

Fase 1 membangun katalog awal dan profil pembelajaran bahasa untuk tiga negara. Cakupan ini merupakan sampel terpilih, bukan inventaris lengkap bahasa di masing-masing negara.

## Ringkasan data terkini

Audit dihitung ulang dari seluruh berkas `profile.json` pada branch `main` tanggal 19 November 2026.

| Negara | Record katalog | Profil bahasa | Entri |
|---|---:|---:|---:|
| Amerika Serikat (US) | 12 | 10 | 228 |
| Jepang (JP) | 9 | 9 | 141 |
| Tiongkok (CN) | 14 | 14 | 130 |
| **Total** | **35** | **33** | **499** |

Dari 35 record katalog, 33 sudah memiliki profil individual. Dua record AS belum menjadi profil individual karena masih berupa label payung:
- Chinese language groups — referensi silang ke profil bahasa terkait dalam katalog Tiongkok; variasi komunitas diaspora AS belum diprofilkan secara terpisah.
- Arabic varieties — perlu dipecah berdasarkan varietas dan komunitas yang benar-benar teridentifikasi sebelum menentukan kode bahasa dan membuat profil.

### Status verifikasi entri

| Status | Jumlah |
|---|---:|
| Reviewed | 397 |
| Draft | 102 |
| Verified | 0 |
| **Total** | **499** |

`Reviewed` berarti entri telah diperiksa terhadap rujukan yang dicantumkan. Status ini bukan bukti bahwa entri sudah divalidasi oleh penutur asli atau ahli bahasa. Belum ada entri yang diberi status `verified`; jangan menyebut materi ini telah tervalidasi secara linguistik.

### Distribusi entri berdasarkan kategori

| Kategori | Entri |
|---|---:|
| Accent and pronunciation | 112 |
| Speaking style and pragmatics | 68 |
| Standard language | 120 |
| Nonstandard language and slang | 44 |
| Profanity and vulgar language | 37 |
| Regional and minority languages | 118 |
| **Total** | **499** |

## Profil bahasa yang tersedia

### Amerika Serikat — 10 profil, 228 entri

1. English — [eng](./negara/US/languages/eng/profile.json)
2. Spanish — [spa](./negara/US/languages/spa/profile.json)
3. Tagalog — [tgl](./negara/US/languages/tgl/profile.json)
4. Vietnamese — [vie](./negara/US/languages/vie/profile.json)
5. French — [fra](./negara/US/languages/fra/profile.json)
6. Korean — [kor](./negara/US/languages/kor/profile.json)
7. Russian — [rus](./negara/US/languages/rus/profile.json)
8. Navajo / Diné Bizaad — [nav](./negara/US/languages/nav/profile.json)
9. Central Alaskan Yup'ik — [esu](./negara/US/languages/esu/profile.json)
10. Western Apache — [apw](./negara/US/languages/apw/profile.json)

### Jepang — 9 profil, 141 entri

1. Japanese — [jpn](./negara/JP/languages/jpn/profile.json)
2. Ainu — [ain](./negara/JP/languages/ain/profile.json)
3. Southern Amami-Oshima — [ams](./negara/JP/languages/ams/profile.json)
4. Kunigami — [xug](./negara/JP/languages/xug/profile.json)
5. Okinawan (Shuri focus) — [ryu](./negara/JP/languages/ryu/profile.json)
6. Miyako — [mvi](./negara/JP/languages/mvi/profile.json)
7. Yaeyama — [rys](./negara/JP/languages/rys/profile.json)
8. Yonaguni / Dunan — [yoi](./negara/JP/languages/yoi/profile.json)
9. Hachijo — [Glottocode hach1239](./negara/JP/languages/hach1239/profile.json)

Hachijo menggunakan Glottocode `hach1239`. `iso_639_3` tetap `null` dan tag BCP 47 tidak diisi karena identifier tersebut belum terkonfirmasi. Glottocode adalah pengenal alternatif, bukan pengganti kode ISO.

### Tiongkok — 14 profil, 130 entri

1. Mandarin Putonghua — [cmn](./negara/CN/languages/cmn/profile.json)
2. Yue (Hong Kong Cantonese focus) — [yue](./negara/CN/languages/yue/profile.json)
3. Wu Chinese (Shanghai focus) — [wuu](./negara/CN/languages/wuu/profile.json)
4. Min Nan / Southern Min (Zhangzhou focus) — [nan](./negara/CN/languages/nan/profile.json)
5. Hakka (Meixian focus) — [hak](./negara/CN/languages/hak/profile.json)
6. Xiang — [hsn](./negara/CN/languages/hsn/profile.json)
7. Gan (Nanchang focus) — [gan](./negara/CN/languages/gan/profile.json)
8. Jin (Northern Shaanxi focus) — [cjy](./negara/CN/languages/cjy/profile.json)
9. Tibetan (Lhasa colloquial focus) — [bod](./negara/CN/languages/bod/profile.json)
10. Uyghur (Central Uyghur focus) — [uig](./negara/CN/languages/uig/profile.json)
11. Mongolian (Inner Mongolia focus) — [mon](./negara/CN/languages/mon/profile.json)
12. Zhuang (Standard Wuming focus) — [zha](./negara/CN/languages/zha/profile.json)
13. Korean (Yanbian / Chosŏnmal focus) — [kor](./negara/CN/languages/kor/profile.json)
14. Kazakh (Xinjiang focus) — [kaz](./negara/CN/languages/kaz/profile.json)

Setiap profil regional hanya mencakup fokus varietas yang dinyatakan. Contohnya, profil Min Nan berfokus pada Zhangzhou dan tidak mewakili seluruh kelompok Min; Yue berfokus pada Kanton Hong Kong; Wu berfokus pada Shanghai; Tibetan berfokus pada Lhasa; dan Mongolian berfokus pada Inner Mongolia.

## Struktur materi pembelajaran

Semua profil menggunakan enam kategori baku LWT:

1. Accent and pronunciation.
2. Speaking style and pragmatics.
3. Standard language.
4. Nonstandard language and slang.
5. Profanity and vulgar language.
6. Regional and minority languages.

Konten vulgar dicatat untuk tujuan pemahaman bahasa. Entri harus menjelaskan makna, intensitas, konteks, dan risiko sosialnya, bukan mendorong penghinaan atau pelecehan. Kategori tertentu dapat tetap kosong bila sumber tepercaya atau dokumentasi komunitas belum memadai.

## Validasi dan batasan mutu

Validator tersedia pada `bahasa-asing-global/tools/validate_language_data.py` dan menggunakan Python standard library. Jalankan dari root repository:

```bash
python bahasa-asing-global/tools/validate_language_data.py
```

Validator memeriksa struktur JSON, enam kategori, field wajib, keunikan ID entri secara global, duplikasi nama/kode dalam katalog negara, format ISO 3166-1/ISO 639-3/Glottocode/BCP 47, URL HTTPS, keamanan dan keberadaan `profile_path`, kecocokan identitas katalog/profil, serta profil yang yatim atau ditautkan berulang. Pemeriksaan URL hanya memvalidasi bentuk URL, bukan memastikan situs dapat diakses atau isi sumber benar-benar mendukung klaim. Hasil validator tetap merupakan pemeriksaan struktur dan konsistensi data; ia tidak membuktikan ketepatan linguistik, kewajaran contoh, atau penerimaan komunitas.

Aturan editorial:
- Gunakan ISO 3166-1 alpha-2 untuk kode negara.
- Gunakan ISO 639-3 bila kode bahasa terkonfirmasi.
- Gunakan BCP 47 hanya jika tag tepat dapat ditentukan.
- Pisahkan bahasa, dialek/aksen, register, dan wilayah.
- Jangan mengarang lema, contoh, klasifikasi, kode, atau rekaman audio.
- Tandai informasi yang belum cukup sumber sebagai `draft`.
- Hormati asal komunitas dan jangan menggeneralisasi satu varietas sebagai keseluruhan bahasa.
- Jangan memberi status `verified` tanpa proses verifikasi penutur asli/ahli yang terdokumentasi.

## Pekerjaan lanjutan Fase 1

Fase 1 **belum selesai**. Pekerjaan berikutnya, dalam urutan prioritas:

1. Memperbarui dan memperketat validator agar laporan audit mencakup ringkasan per negara, kategori, dan konsistensi identitas bahasa.
2. Meninjau 102 entri draft dan memperkuat dukungan sumber untuk entri reviewed.
3. Memecah dua label payung AS menjadi profil yang benar-benar teridentifikasi setelah bukti komunitas dan varietas tersedia.
4. Meninjau cakupan bahasa/varietas Jepang dan Tiongkok tanpa menyamakan kelompok besar dengan satu varietas lokal.
5. Menyiapkan proses tinjauan penutur asli/ahli, termasuk pencatatan nama peninjau, tanggal, lingkup, dan keputusan.
6. Menambahkan pelafalan/audio hanya dengan sumber dan lisensi yang jelas.

Fase 2 tidak dimulai sebelum kriteria penyelesaian Fase 1 ditinjau dan disepakati.

## Referensi utama tingkat negara

- [U.S. Census Bureau — Detailed Languages Spoken at Home, 2017–2021](https://www.census.gov/newsroom/press-releases/2025/2017-2021-acs-language-use-tables.html). Katalog AS hanya sampel dari cakupan data yang jauh lebih luas.
- [Agency for Cultural Affairs, Japan](https://www.bunka.go.jp/english/policy/japanese_language/policy/index.html) dan [NINJAL — Endangered Languages](https://www.ninjal.ac.jp/english/research/cr-project/project-4/endangered-languages/).
- [Ministry of Education of the People's Republic of China](https://www.moe.gov.cn/). Rujukan untuk kebijakan bahasa, bahasa umum nasional, dan lanskap bahasa di Tiongkok.

Tanggal audit dokumentasi: 2026-11-19.
