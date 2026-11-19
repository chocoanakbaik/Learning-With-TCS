# Fase 01 — Amerika Serikat, Jepang, dan Tiongkok

Fase ini mengembangkan basis pengetahuan untuk tiga negara. Paket inti untuk bahasa utama telah diisi pada enam kategori pembelajaran LWT.

## Navigasi negara dan profil bahasa

| Kode | Negara | Profil bahasa yang tersedia |
|---|---|---|
| US | Amerika Serikat | English, Spanish, Tagalog, Vietnamese, French, Korean, Russian, Navajo (Diné Bizaad), Central Alaskan Yup'ik, Western Apache |
| JP | Jepang | Japanese |
| CN | Tiongkok | Mandarin Putonghua |

Tautan katalog negara:
- [Amerika Serikat](./negara/US/country.json)
- [Jepang](./negara/JP/country.json)
- [Tiongkok](./negara/CN/country.json)

Profil bahasa inti dan komunitas:
- [English — US](./negara/US/languages/eng/profile.json)
- [Spanish — US](./negara/US/languages/spa/profile.json)
- [Tagalog — US Filipino communities](./negara/US/languages/tgl/profile.json)
- [Vietnamese — US communities](./negara/US/languages/vie/profile.json)
- [French — US heritage communities](./negara/US/languages/fra/profile.json)
- [Korean — US communities](./negara/US/languages/kor/profile.json)
- [Russian — US communities](./negara/US/languages/rus/profile.json)
- [Navajo / Diné Bizaad](./negara/US/languages/nav/profile.json)
- [Central Alaskan Yup'ik](./negara/US/languages/esu/profile.json)
- [Western Apache](./negara/US/languages/apw/profile.json)
- [Japanese — JP](./negara/JP/languages/jpn/profile.json)
- [Mandarin Putonghua — CN](./negara/CN/languages/cmn/profile.json)

## Cakupan materi

Setiap profil bahasa memakai enam kategori: logat/aksen, pragmatik/cara bicara, bahasa baku, slang/nonbaku, umpatan/kata vulgar, dan bahasa regional/minoritas. Beberapa profil Indigenous sengaja membiarkan kategori slang atau umpatan kosong sampai sumber serta tinjauan komunitas tersedia.

| Profil bahasa | Entri awal |
|---|---:|
| English (US) | 32 |
| Spanish (US) | 17 |
| Tagalog (US) | 18 |
| Vietnamese (US) | 18 |
| French (US) | 18 |
| Korean (US) | 16 |
| Russian (US) | 18 |
| Navajo / Diné Bizaad | 12 |
| Central Alaskan Yup'ik | 12 |
| Western Apache | 10 |
| Japanese (JP) | 32 |
| Mandarin Putonghua (CN) | 33 |
| **Total** | **236** |

Audit entri terakhir: **165 reviewed, 71 draft, dan 0 verified**. Status reviewed berarti entri sudah diperiksa terhadap rujukan yang dicantumkan, bukan validasi menyeluruh oleh penutur asli.

## Status pekerjaan

**Pekerjaan yang telah dilakukan:**
- Katalog untuk tiga negara telah dibuat dan diperbarui.
- Sepuluh profil bahasa/komunitas telah dibuat untuk Amerika Serikat.
- Profil Japanese dan Mandarin Putonghua tetap tersedia untuk Jepang dan Tiongkok.
- Semua 12 profil memiliki enam kategori pembelajaran LWT.
- Katalog negara mengarah ke profil individual yang tersedia.
- Referensi yang tidak langsung mendukung suatu lema dihapus atau ditandai draft.
- Validator Python standard library tersedia untuk memeriksa JSON, kategori, field wajib, ID unik, status, sumber, dan hubungan katalog/profil.
- Hachijo tetap tanpa kode ISO 639-3 sampai identifier-nya diverifikasi.

## Ringkasan audit

Audit terbaru terhadap berkas GitHub menemukan:
- **3 katalog negara**
- **12 profil bahasa**
- **236 entri pembelajaran**
- **165 reviewed, 71 draft, 0 verified**
- **236 ID unik**
- **233 tautan sumber per entri** dan 70 tautan sumber tingkat profil
- **0 kesalahan struktur, 0 kesalahan hubungan katalog/profil, dan 0 ID duplikat**

Status reviewed berarti entri telah diperiksa terhadap rujukan yang dicantumkan. Itu bukan klaim validasi penutur asli. Status verified belum diberikan karena proses validasi penutur asli/ahli belum terdokumentasi.

Katalog berisi **35 record bahasa/kelompok bahasa**. Sebanyak 12 sudah memiliki profil. **23 record masih belum memiliki profil individual**: dua label payung di katalog US yang perlu dipecah, delapan record di Jepang, dan tiga belas record di Tiongkok. Angka tersebut adalah hitungan katalog saat ini, bukan klaim inventaris nasional lengkap.

## Pekerjaan yang masih terbuka

- Memecah Chinese language groups dan Arabic varieties di katalog US menjadi bahasa/varietas yang teridentifikasi dengan benar.
- Menambahkan profil Ainu dan bahasa/varietas Ryukyuan di Jepang; memverifikasi kode Hachijo terlebih dahulu.
- Menambahkan profil bahasa Yue, Wu, Min secara lebih rinci, Hakka, Xiang, Gan, Jin, serta bahasa minoritas terpilih di Tiongkok.
- Menambahkan rekaman pelafalan berlisensi, transkripsi fonetik, dan contoh percakapan dari penutur.
- Memeriksa materi draft dan memperoleh validasi penutur asli/ahli.
- Menambah kosakata slang dan umpatan hanya jika tersedia sumber leksikografi/korpus dan konteks komunitas yang tepat.

Dengan demikian, Fase 1 sudah memiliki **paket data awal yang terstruktur dan dapat divalidasi**, tetapi belum boleh dinyatakan selesai secara linguistik. Sisa profil, inventaris regional, audio, dan tinjauan komunitas masih diperlukan.

## Catatan sumber dan batas penggunaan

- U.S. Census Bureau mendokumentasikan lebih dari 500 bahasa dan kelompok bahasa dalam tabel bahasa 2017–2021. Katalog US di LWT hanya sampel awal.
- NINJAL menyediakan korpus bahasa tulis, lisan, dialek, dan sumber dokumentasi bahasa terancam di Jepang.
- Hukum dan materi uji Putonghua Kementerian Pendidikan RRT menjadi rujukan standar Mandarin.
- Rujukan kamus Mandarin dari Kementerian Pendidikan Taiwan pada beberapa entri umpatan hanya menjadi pembanding leksikografi; rujukan itu **tidak** dianggap bukti final penggunaan di Tiongkok daratan.
- Slang bersifat temporal. Daftar kata populer resmi harus menyertakan tahun penerbitan.
- Umpatan dicatat untuk pemahaman makna dan risiko sosial. Tidak ada instruksi untuk menggunakannya dalam serangan terhadap orang.

## Validasi lokal

Jalankan dari root repositori:

```bash
python bahasa-asing-global/tools/validate_language_data.py
```

Validator menggunakan Python standard library dan tidak membutuhkan paket pihak ketiga. Error membuat proses keluar dengan kode non-zero; entri draft dan bahasa yang belum memiliki profil dilaporkan sebagai peringatan.
