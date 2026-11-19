#!/usr/bin/env python3
"""Validate LWT country catalogs and language profiles using Python stdlib only."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
COUNTRY_ROOT = ROOT / "bahasa-asing-global" / "negara"
SCHEMA_VERSION = "1.1.0"

REQUIRED_CATEGORIES = (
    "accent_and_pronunciation",
    "speaking_style_and_pragmatics",
    "standard_language",
    "nonstandard_language_and_slang",
    "profanity_and_vulgar_language",
    "regional_and_minority_languages",
)
REQUIRED_ENTRY_FIELDS = {
    "id",
    "term",
    "explanation_id",
    "indonesian_learning_link",
    "region",
    "register",
    "usage_context",
    "example_source_language",
    "example_indonesian",
    "sources",
    "verification_status",
}
VALID_STATUSES = {"draft", "reviewed", "verified"}
ISO_639_3_RE = re.compile(r"^[a-z]{3}$")
ISO_3166_1_ALPHA2_RE = re.compile(r"^[A-Z]{2}$")
ISO_3166_1_ALPHA3_RE = re.compile(r"^[A-Z]{3}$")
GLOTTOCODE_RE = re.compile(r"^[a-z]{4}[0-9]{4}$")
BCP47_RE = re.compile(r"^[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.profiles = 0
        self.catalog_records = 0
        self.entries = 0
        self.statuses: Counter[str] = Counter()
        self.category_counts: Counter[str] = Counter()
        self.country_counts: dict[str, Counter[str]] = {}
        self.seen_entry_ids: set[str] = set()
        self.profile_link_counts: Counter[Path] = Counter()

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path, report: Report) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(f"{relative(path)}: gagal membaca JSON: {exc}")
        return None


def valid_https_url(value: Any) -> bool:
    if not isinstance(value, str) or not value or value != value.strip():
        return False
    if any(character.isspace() for character in value):
        return False
    try:
        parsed = urlsplit(value)
        # Accessing .port also rejects malformed/out-of-range port values.
        _ = parsed.port
        return (
            parsed.scheme.lower() == "https"
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
        )
    except ValueError:
        return False


def check_source_objects(
    sources: Any, label: str, report: Report
) -> None:
    if not isinstance(sources, list):
        report.error(f"{label}: sources harus berupa array.")
        return
    for index, source in enumerate(sources, start=1):
        source_label = f"{label} [sumber {index}]"
        if not isinstance(source, dict):
            report.error(f"{source_label}: sumber harus berupa object.")
            continue
        if not valid_https_url(source.get("url")):
            report.error(f"{source_label}: url harus berupa URL HTTPS yang valid.")
        title = source.get("title")
        if not isinstance(title, str) or not title.strip():
            report.error(f"{source_label}: title harus berupa string non-kosong.")


def check_entry(
    entry: Any, path: Path, category: str, report: Report
) -> None:
    label = f"{relative(path)} [{category}]"
    if not isinstance(entry, dict):
        report.error(f"{label}: entri harus berupa object.")
        return

    missing = REQUIRED_ENTRY_FIELDS - set(entry)
    if missing:
        report.error(f"{label}: field wajib hilang: {', '.join(sorted(missing))}.")

    entry_id = entry.get("id")
    if not isinstance(entry_id, str) or not entry_id.strip():
        report.error(f"{label}: id harus berupa string non-kosong.")
    elif entry_id != entry_id.strip():
        report.error(f"{label}: id tidak boleh memiliki spasi di awal/akhir.")
    elif entry_id in report.seen_entry_ids:
        report.error(f"{label}: ID duplikat global: {entry_id}.")
    else:
        report.seen_entry_ids.add(entry_id)

    status = entry.get("verification_status")
    if not isinstance(status, str) or status not in VALID_STATUSES:
        report.error(f"{label}: verification_status tidak valid: {status!r}.")
    else:
        report.statuses[status] += 1

    sources = entry.get("sources")
    if not isinstance(sources, list):
        report.error(f"{label}: sources harus berupa array.")
    else:
        for index, source in enumerate(sources, start=1):
            if not valid_https_url(source):
                report.error(
                    f"{label} [sumber {index}]: setiap sumber harus berupa URL HTTPS yang valid."
                )
        if status in {"reviewed", "verified"} and not sources:
            report.error(
                f"{label}: status {status} membutuhkan setidaknya satu sumber."
            )
        elif status == "draft" and not sources:
            report.warn(f"{label}: entri draft belum memiliki sumber langsung.")

    for field in (
        "term",
        "explanation_id",
        "indonesian_learning_link",
        "region",
        "register",
        "usage_context",
        "example_source_language",
        "example_indonesian",
    ):
        if field in entry and (
            not isinstance(entry[field], str) or not entry[field].strip()
        ):
            report.error(f"{label}: {field} harus berupa string non-kosong.")

    report.entries += 1
    report.category_counts[category] += 1


def check_language_identity(
    language: Any, label: str, report: Report
) -> tuple[str | None, str | None]:
    if not isinstance(language, dict):
        report.error(f"{label}: language harus berupa object.")
        return None, None

    name = language.get("name")
    if not isinstance(name, str) or not name.strip():
        report.error(f"{label}: language.name harus berupa string non-kosong.")

    iso_code = language.get("iso_639_3")
    if iso_code is not None and (
        not isinstance(iso_code, str) or not ISO_639_3_RE.fullmatch(iso_code)
    ):
        report.error(f"{label}: iso_639_3 harus berupa kode ISO 639-3 tiga huruf atau null.")

    glottocode = language.get("glottocode")
    if glottocode is not None and (
        not isinstance(glottocode, str) or not GLOTTOCODE_RE.fullmatch(glottocode)
    ):
        report.error(f"{label}: glottocode tidak memiliki format Glottolog yang diharapkan.")

    if iso_code is None and glottocode is None:
        report.error(f"{label}: profil harus memiliki ISO 639-3 atau Glottocode.")

    tags = language.get("bcp47_tags", [])
    if not isinstance(tags, list):
        report.error(f"{label}: bcp47_tags harus berupa array.")
    else:
        seen_tags: set[str] = set()
        for tag in tags:
            if not isinstance(tag, str) or not BCP47_RE.fullmatch(tag):
                report.error(f"{label}: tag BCP 47 tidak valid secara format: {tag!r}.")
            elif tag.lower() in seen_tags:
                report.error(f"{label}: tag BCP 47 duplikat: {tag}.")
            else:
                seen_tags.add(tag.lower())

    return iso_code, glottocode


def check_profile(path: Path, country_code: str, report: Report) -> None:
    profile = load_json(path, report)
    if profile is None:
        return
    report.profiles += 1
    label = relative(path)

    if not isinstance(profile, dict):
        report.error(f"{label}: profil harus berupa object.")
        return
    if profile.get("record_type") != "language_profile":
        report.error(f"{label}: record_type harus language_profile.")
    if profile.get("schema_version") != SCHEMA_VERSION:
        report.error(f"{label}: schema_version harus {SCHEMA_VERSION}.")

    check_language_identity(profile.get("language"), label, report)

    context = profile.get("country_context")
    if not isinstance(context, dict):
        report.error(f"{label}: country_context harus berupa object.")
    elif context.get("country_code") != country_code:
        report.error(
            f"{label}: country_context tidak cocok dengan folder {country_code}."
        )

    categories = profile.get("categories")
    if not isinstance(categories, dict):
        report.error(f"{label}: categories harus berupa object.")
        return

    missing = set(REQUIRED_CATEGORIES) - set(categories)
    extra = set(categories) - set(REQUIRED_CATEGORIES)
    if missing:
        report.error(f"{label}: kategori hilang: {', '.join(sorted(missing))}.")
    if extra:
        report.warn(f"{label}: kategori tambahan: {', '.join(sorted(extra))}.")

    for category in REQUIRED_CATEGORIES:
        section = categories.get(category)
        if not isinstance(section, dict):
            report.error(f"{label} [{category}]: harus berupa object.")
            continue
        category_status = section.get("status")
        if not isinstance(category_status, str) or not category_status.strip():
            report.error(f"{label} [{category}]: status kategori wajib diisi.")
        entries = section.get("entries")
        if not isinstance(entries, list):
            report.error(f"{label} [{category}]: entries harus berupa array.")
            continue
        for entry in entries:
            check_entry(entry, path, category, report)

    check_source_objects(profile.get("sources"), label, report)

    verification = profile.get("verification")
    if not isinstance(verification, dict):
        report.error(f"{label}: verification harus berupa object.")
    elif not isinstance(verification.get("status"), str) or not verification["status"].strip():
        report.error(f"{label}: verification.status harus berupa string non-kosong.")
    elif "not_native_validated" in verification["status"]:
        report.warn(f"{label}: profil belum divalidasi penutur asli/ahli.")



def resolve_profile_path(
    raw_path: Any, country_dir: Path, country_file: Path, report: Report
) -> Path | None:
    label = relative(country_file)
    if not isinstance(raw_path, str) or not raw_path.strip():
        report.error(f"{label}: profile_path harus berupa path relatif non-kosong.")
        return None
    if "\\" in raw_path:
        report.error(f"{label}: profile_path harus memakai pemisah '/' POSIX.")
        return None

    parts = Path(raw_path).parts
    if (
        Path(raw_path).is_absolute()
        or len(parts) != 3
        or parts[0] != "languages"
        or parts[2] != "profile.json"
        or any(part in {"", ".", ".."} for part in parts)
    ):
        report.error(
            f"{label}: profile_path harus berbentuk languages/<kode>/profile.json dan tidak boleh keluar dari direktori negara."
        )
        return None

    full_path = (country_dir / raw_path).resolve()
    try:
        full_path.relative_to(country_dir.resolve())
    except ValueError:
        report.error(f"{label}: profile_path keluar dari direktori negara.")
        return None
    if not full_path.is_file():
        report.error(f"{label}: profile_path tidak ditemukan: {raw_path}")
        return None
    return full_path


def check_country_catalog(
    country_file: Path, report: Report
) -> None:
    country = load_json(country_file, report)
    if not isinstance(country, dict):
        if country is not None:
            report.error(f"{relative(country_file)}: katalog negara harus berupa object.")
        return

    country_dir = country_file.parent
    folder_code = country_dir.name
    stats = report.country_counts.setdefault(folder_code, Counter())

    if country.get("schema_version") != SCHEMA_VERSION:
        report.error(
            f"{relative(country_file)}: schema_version harus {SCHEMA_VERSION}."
        )
    if country.get("record_type") != "country_profile":
        report.error(f"{relative(country_file)}: record_type harus country_profile.")

    country_data = country.get("country")
    if not isinstance(country_data, dict):
        report.error(f"{relative(country_file)}: country harus berupa object.")
        return

    alpha2 = country_data.get("iso_3166_1_alpha2")
    alpha3 = country_data.get("iso_3166_1_alpha3")
    if not ISO_3166_1_ALPHA2_RE.fullmatch(alpha2 or ""):
        report.error(f"{relative(country_file)}: kode ISO 3166-1 alpha-2 tidak valid.")
    if alpha2 != folder_code:
        report.error(
            f"{relative(country_file)}: kode ISO negara tidak cocok dengan nama folder."
        )
    if not ISO_3166_1_ALPHA3_RE.fullmatch(alpha3 or ""):
        report.error(f"{relative(country_file)}: kode ISO 3166-1 alpha-3 tidak valid.")
    for field in ("name_en", "name_local"):
        if not isinstance(country_data.get(field), str) or not country_data[field].strip():
            report.error(
                f"{relative(country_file)}: country.{field} harus berupa string non-kosong."
            )

    check_source_objects(country.get("sources"), relative(country_file), report)

    language_records = country.get("languages")
    if not isinstance(language_records, list):
        report.error(f"{relative(country_file)}: languages harus berupa array.")
        return

    stats["catalog_records"] = len(language_records)
    seen_names: set[str] = set()
    seen_iso_codes: set[str] = set()
    seen_glottocodes: set[str] = set()
    language_dir = country_dir / "languages"
    profile_files = (
        sorted(language_dir.rglob("profile.json")) if language_dir.is_dir() else []
    )
    stats["profile_files"] = len(profile_files)

    for language in language_records:
        if not isinstance(language, dict):
            report.error(
                f"{relative(country_file)}: setiap record bahasa harus berupa object."
            )
            continue

        report.catalog_records += 1
        name = language.get("name")
        if not isinstance(name, str) or not name.strip():
            report.error(
                f"{relative(country_file)}: setiap record bahasa harus memiliki name."
            )
        else:
            normalized_name = name.strip().casefold()
            if normalized_name in seen_names:
                report.error(
                    f"{relative(country_file)}: nama bahasa duplikat dalam katalog: {name}."
                )
            seen_names.add(normalized_name)

        iso_code = language.get("iso_639_3")
        if iso_code is not None and (
            not isinstance(iso_code, str) or not ISO_639_3_RE.fullmatch(iso_code)
        ):
            report.error(
                f"{relative(country_file)}: kode ISO 639-3 tidak valid pada {name!r}."
            )
        elif isinstance(iso_code, str):
            if iso_code in seen_iso_codes:
                report.error(
                    f"{relative(country_file)}: kode ISO 639-3 duplikat: {iso_code}."
                )
            seen_iso_codes.add(iso_code)

        glottocode = language.get("glottocode")
        if glottocode is not None:
            if (
                not isinstance(glottocode, str)
                or not GLOTTOCODE_RE.fullmatch(glottocode)
            ):
                report.error(
                    f"{relative(country_file)}: Glottocode tidak valid pada {name!r}."
                )
            elif glottocode in seen_glottocodes:
                report.error(
                    f"{relative(country_file)}: Glottocode duplikat: {glottocode}."
                )
            else:
                seen_glottocodes.add(glottocode)

        if "profile_path" not in language or language["profile_path"] is None:
            stats["without_profile"] += 1
            status = language.get("profile_status")
            if status not in {"cross_reference_only", "split_required"}:
                report.warn(
                    f"{relative(country_file)}: {name!r} belum memiliki profile_path; periksa alasan/statusnya."
                )
            continue

        profile_path = resolve_profile_path(
            language.get("profile_path"), country_dir, country_file, report
        )
        if profile_path is None:
            continue

        report.profile_link_counts[profile_path] += 1
        if iso_code is None and glottocode is None:
            report.error(
                f"{relative(country_file)}: {name!r} memiliki profil tetapi tidak memiliki ISO 639-3 maupun Glottocode."
            )

        linked_profile = load_json(profile_path, report)
        if not isinstance(linked_profile, dict):
            continue
        linked_language = linked_profile.get("language")
        if not isinstance(linked_language, dict):
            report.error(f"{relative(profile_path)}: language harus berupa object.")
            continue

        linked_iso = linked_language.get("iso_639_3")
        linked_glottocode = linked_language.get("glottocode")
        if linked_iso != iso_code:
            report.error(
                f"{relative(profile_path)}: ISO bahasa ({linked_iso!r}) tidak cocok dengan katalog ({iso_code!r})."
            )
        if glottocode is not None and linked_glottocode != glottocode:
            report.error(
                f"{relative(profile_path)}: Glottocode ({linked_glottocode!r}) tidak cocok dengan katalog ({glottocode!r})."
            )
        elif glottocode is None and linked_glottocode is not None and iso_code is None:
            report.error(
                f"{relative(profile_path)}: Glottocode profil tidak tercatat pada katalog."
            )

        stats["linked_profiles"] += 1

    for profile_file in profile_files:
        check_profile(profile_file, folder_code, report)
        link_count = report.profile_link_counts[profile_file.resolve()]
        if link_count == 0:
            report.error(
                f"{relative(profile_file)}: profil tidak ditautkan oleh country.json."
            )
        elif link_count > 1:
            report.error(
                f"{relative(profile_file)}: profil ditautkan {link_count} kali dalam katalog yang sama."
            )


def main() -> int:
    report = Report()
    if not COUNTRY_ROOT.is_dir():
        print(f"ERROR: direktori tidak ditemukan: {COUNTRY_ROOT}")
        return 2

    country_files = sorted(COUNTRY_ROOT.glob("*/country.json"))
    if not country_files:
        report.error("Tidak ditemukan country.json.")

    for country_file in country_files:
        folder_code = country_file.parent.name
        if not ISO_3166_1_ALPHA2_RE.fullmatch(folder_code):
            report.error(
                f"{relative(country_file)}: nama folder negara harus ISO alpha-2 huruf kapital."
            )
        check_country_catalog(country_file, report)

    print("LWT DATA VALIDATION")
    print(f"Country catalogs : {len(country_files)}")
    print(f"Catalog records  : {report.catalog_records}")
    print(f"Language profiles: {report.profiles}")
    print(f"Learning entries : {report.entries}")
    print(
        "Draft / reviewed / verified: "
        f"{report.statuses['draft']} / {report.statuses['reviewed']} / {report.statuses['verified']}"
    )
    print("Per-country coverage:")
    for code, stats in sorted(report.country_counts.items()):
        print(
            f"  {code}: {stats['catalog_records']} catalog records, "
            f"{stats['profile_files']} profiles, "
            f"{stats['linked_profiles']} linked, "
            f"{stats['without_profile']} without individual profile"
        )
    print("Category totals:")
    for category in REQUIRED_CATEGORIES:
        print(f"  {category}: {report.category_counts[category]}")

    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")

    if report.errors:
        print(f"FAILED: {len(report.errors)} error(s), {len(report.warnings)} warning(s).")
        return 1
    print(f"PASSED: 0 error(s), {len(report.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
