# Fase 01 — Amerika Serikat, Jepang, dan Tiongkok

Fase ini mengembangkan basis pengetahuan untuk tiga negara. Paket inti untuk bahasa utama telah diisi pada enam kategori pembelajaran LWT.

## Navigasi negara dan profil inti

| Kode | Negara | Bahasa utama | Katalog |
|---|---|---|---|
| US | Amerika Serikat | English (eng) | [country.json](./negara/US/country.json) |
| JP | Jepang | Japanese (jpn) | [country.json](./negara/JP/country.json) |
| CN | Tiongkok | Mandarin Putonghua (cmn) | [country.json](./negara/CN/country.json) |

Profil bahasa:

- [English — Amerika Serikat](./negara/US/languages/eng/profile.json)
- [Japanese — Jepang](./negara/JP/languages/jpn/profile.json)
- [Mandarin Putonghua — Tiongkok daratan](./negara/CN/languages/cmn/profile.json)

## Cakupan paket inti

Setiap profil utama memiliki enam kategori: logat/aksen, pragmatik/cara bicara, bahasa baku, slang/nonbaku, umpatan/kata vulgar, dan bahasa regional/minoritas.

| Profil | Entri awal | Catatan |
|---|---:|---|
| English (US) | 32 | Beberapa entri aksen regional masih draft; referensi flapping dan cot-caught telah diperkuat dengan riset akademik. |
| Japanese (JP) | 32 | Rujukan Japan Foundation, NINJAL, NDL, dan kamus; slang tertentu sudah memiliki rujukan langsung, lainnya masih draft. |
| Mandarin Putonghua (CN) | 33 | Standar fonologi/tulisan ditopang sumber pemerintah RRT; beberapa pragmatik dan umpatan tetap draft. |
| **Total** | **97** | Benih materi terstruktur, bukan inventaris lengkap kosakata semua penutur. |

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
