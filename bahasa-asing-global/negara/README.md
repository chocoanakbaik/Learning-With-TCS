# Profil Bahasa Berdasarkan Negara

Setiap negara memiliki direktori sendiri menggunakan kode ISO 3166-1 alpha-2, misalnya:

```text
negara/
├── US/
│   ├── country.json
│   └── languages/
│       ├── en/
│       │   └── profile.json
│       └── es/
│           └── profile.json
├── JP/
│   ├── country.json
│   └── languages/
│       └── ja/
│           └── profile.json
└── ID/
    ├── country.json
    └── languages/
        ├── id/
        │   └── profile.json
        ├── jav/
        │   └── profile.json
        └── sun/
            └── profile.json
```

Contoh di atas hanya menunjukkan pola direktori, bukan klaim daftar lengkap bahasa di negara tersebut.

## Aturan

1. Gunakan kode negara ISO 3166-1 alpha-2 sebagai nama direktori.
2. Gunakan kode bahasa ISO 639 sebagai identitas bahasa.
3. Simpan variasi regional sebagai subprofil/entri variasi dari bahasa terkait.
4. Jika bahasa yang sama digunakan di beberapa negara, tautkan ke identitas bahasa yang sama dan simpan variasi negara/wilayah secara terpisah.
5. Jangan menganggap semua bahasa lokal sebagai dialek dari bahasa nasional.
6. Buat direktori negara hanya saat ada profil atau materi yang dapat dipertanggungjawabkan; hindari direktori kosong massal.
7. Semua data harus mengikuti enam kelompok materi pada direktori induk dan menyertakan sumber serta status verifikasi.

Lihat `../README.md`, `../template-negara/README.md`, dan `../skema-data/README.md` sebelum menambahkan profil.
