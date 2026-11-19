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

**Selesai untuk paket inti Fase 1:**
- Katalog negara US, JP, dan CN telah dibuat.
- Tiga bahasa utama memiliki profil terisi pada keenam kategori.
- Setiap entri memiliki ID, penjelasan Indonesia, hubungan ke pembelajaran bahasa Indonesia, konteks, contoh, sumber, dan status verifikasi.
- Status profil dan tautan dari katalog negara telah diselaraskan.
- Sumber yang tidak secara langsung mendukung lema dihapus atau diganti; rujukan pembanding dari Taiwan diberi batas geografis yang jelas.
- Validator Python standard library ditambahkan dan diperkuat untuk memeriksa JSON, kategori, field wajib, ID unik, status, tautan sumber, dan relasi katalog.
- Kode Hachijo tetap `null` karena belum dikonfirmasi; kode bahasa tidak ditebak.

## Ringkasan status entri

Audit data terakhir: **97 entri**, terdiri dari **63 reviewed**, **34 draft**, dan **0 verified**.

- `reviewed` berarti entri telah diperiksa terhadap rujukan yang dicantumkan; bukan berarti sudah divalidasi penutur asli.
- `draft` berarti sumber langsung, sebaran regional, atau konteks pemakaian belum cukup.
- `verified` belum diberikan karena belum ada proses validasi penutur asli/ahli yang terdokumentasi untuk entri-entri tersebut.

Katalog yang saat ini tercatat memuat **35 record bahasa/kelompok bahasa** di tiga negara. Tiga bahasa utama telah memiliki profil; **32 record lainnya masih menunggu profil individual**. Angka ini adalah hitungan record katalog saat ini, bukan klaim bahwa semua bahasa di ketiga negara sudah terdaftar.

Pemeriksaan struktur terakhir menemukan nol kesalahan JSON/struktur, nol ID kosong/duplikat, dan seluruh tiga profil inti terhubung ke kode bahasa yang sesuai.

**Masih terbuka sebelum seluruh inventaris tiga negara dapat disebut lengkap:**
- Profil individual bahasa lain yang tercantum dalam katalog negara, termasuk bahasa komunitas, Indigenous, regional, dan minoritas.
- Pemecahan label payung seperti Min menjadi subvarietas yang tepat.
- Penambahan rekaman pelafalan berlisensi dan transkripsi fonetik yang ditinjau.
- Pemeriksaan oleh penutur asli/ahli, khususnya entri berstatus `draft`.
- Penambahan kosakata dan contoh percakapan yang bersumber dari kamus/korpus, dengan wilayah dan tahun penggunaan.

Dengan demikian, **paket inti tiga bahasa selesai diisi**, tetapi fase tiga negara ini tidak diklaim sebagai inventaris linguistik nasional yang lengkap.

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
