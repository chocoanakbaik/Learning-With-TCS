#!/usr/bin/env python3
"""Validate LWT country catalogs and language profiles using Python stdlib only."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
COUNTRY_ROOT = ROOT / "bahasa-asing-global" / "negara"
REQUIRED_CATEGORIES = (
    "accent_and_pronunciation",
    "speaking_style_and_pragmatics",
    "standard_language",
    "nonstandard_language_and_slang",
    "profanity_and_vulgar_language",
    "regional_and_minority_languages",
)
REQUIRED_ENTRY_FIELDS = {
    "id", "term", "explanation_id", "indonesian_learning_link", "region",
    "register", "usage_context", "example_source_language", "example_indonesian",
    "sources", "verification_status",
}
VALID_STATUSES = {"draft", "reviewed", "verified"}


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
        self.seen_ids: set[str] = set()
        self.linked_profiles: set[Path] = set()

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_json(path: Path, report: Report) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        report.error(f"{relative(path)}: gagal membaca JSON: {exc}")
        return None


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
    elif entry_id in report.seen_ids:
        report.error(f"{label}: ID duplikat global: {entry_id}.")
    else:
        report.seen_ids.add(entry_id)

    status = entry.get("verification_status")
    if not isinstance(status, str) or status not in VALID_STATUSES:
        report.error(f"{label}: verification_status tidak valid: {status!r}.")
    else:
        report.statuses[status] += 1

    sources = entry.get("sources")
    if not isinstance(sources, list):
        report.error(f"{label}: sources harus berupa array.")
    else:
        for source in sources:
            if not isinstance(source, str) or not source.startswith("https://"):
                report.error(f"{label}: setiap sumber harus berupa URL https://.")
        if status in {"reviewed", "verified"} and not sources:
            report.error(f"{label}: status {status} membutuhkan setidaknya satu sumber.")
        elif status == "draft" and not sources:
            report.warn(f"{label}: entri draft belum memiliki sumber langsung.")

    for field in (
        "term", "explanation_id", "indonesian_learning_link", "region", "register",
        "usage_context", "example_source_language", "example_indonesian",
    ):
        if field in entry and (
            not isinstance(entry[field], str) or not entry[field].strip()
        ):
            report.error(f"{label}: {field} harus berupa string non-kosong.")

    report.entries += 1
    report.category_counts[category] += 1


def check_profile(path: Path, country_code: str, report: Report) -> None:
    profile = load_json(path, report)
    if profile is None:
        return
    report.profiles += 1

    if not isinstance(profile, dict):
        report.error(f"{relative(path)}: profil harus berupa object.")
        return
    if profile.get("record_type") != "language_profile":
        report.error(f"{relative(path)}: record_type harus language_profile.")
    if profile.get("schema_version") != "1.1.0":
        report.error(f"{relative(path)}: schema_version harus 1.1.0.")

    context = profile.get("country_context")
    if not isinstance(context, dict):
        report.error(f"{relative(path)}: country_context harus berupa object.")
    elif context.get("country_code") != country_code:
        report.error(f"{relative(path)}: country_context tidak cocok dengan folder {country_code}.")

    categories = profile.get("categories")
    if not isinstance(categories, dict):
        report.error(f"{relative(path)}: categories harus berupa object.")
        return

    missing = set(REQUIRED_CATEGORIES) - set(categories)
    extra = set(categories) - set(REQUIRED_CATEGORIES)
    if missing:
        report.error(f"{relative(path)}: kategori hilang: {', '.join(sorted(missing))}.")
    if extra:
        report.warn(f"{relative(path)}: kategori tambahan: {', '.join(sorted(extra))}.")

    for category in REQUIRED_CATEGORIES:
        section = categories.get(category)
        if not isinstance(section, dict):
            report.error(f"{relative(path)} [{category}]: harus berupa object.")
            continue
        entries = section.get("entries")
        if not isinstance(entries, list):
            report.error(f"{relative(path)} [{category}]: entries harus berupa array.")
            continue
        for entry in entries:
            check_entry(entry, path, category, report)

    profile_sources = profile.get("sources", [])
    if not isinstance(profile_sources, list):
        report.error(f"{relative(path)}: sources tingkat profil harus berupa array.")
    else:
        for source in profile_sources:
            if (
                not isinstance(source, dict)
                or not isinstance(source.get("url"), str)
                or not source["url"].startswith("https://")
            ):
                report.error(f"{relative(path)}: setiap sumber profil harus memiliki URL https://.")

    verification = profile.get("verification", {})
    if not isinstance(verification, dict):
        report.error(f"{relative(path)}: verification harus berupa object.")
    elif "not_native_validated" in str(verification.get("status", "")):
        report.warn(f"{relative(path)}: profil belum divalidasi penutur asli/ahli.")


def main() -> int:
    report = Report()
    if not COUNTRY_ROOT.is_dir():
        print(f"ERROR: direktori tidak ditemukan: {COUNTRY_ROOT}")
        return 2

    country_files = sorted(COUNTRY_ROOT.glob("*/country.json"))
    if not country_files:
        report.error("Tidak ditemukan country.json.")

    for country_file in country_files:
        country = load_json(country_file, report)
        if not isinstance(country, dict):
            continue

        folder_code = country_file.parent.name
        country_data = country.get("country")
        if not isinstance(country_data, dict):
            report.error(f"{relative(country_file)}: country harus berupa object.")
            continue
        code = country_data.get("iso_3166_1_alpha2")
        if code != folder_code:
            report.error(f"{relative(country_file)}: kode ISO negara tidak cocok dengan nama folder.")
        if country.get("record_type") != "country_profile":
            report.error(f"{relative(country_file)}: record_type harus country_profile.")

        language_records = country.get("languages", [])
        if not isinstance(language_records, list):
            report.error(f"{relative(country_file)}: languages harus berupa array.")
            continue

        stats = report.country_counts.setdefault(folder_code, Counter())
        stats["catalog_records"] = len(language_records)
        for language in language_records:
            if not isinstance(language, dict):
                report.error(f"{relative(country_file)}: setiap record bahasa harus berupa object.")
                continue
            report.catalog_records += 1
            profile_path = language.get("profile_path")
            if not profile_path:
                stats["without_profile"] += 1
                continue

            full_path = (country_file.parent / profile_path).resolve()
            if not full_path.is_file():
                report.error(f"{relative(country_file)}: profile_path tidak ditemukan: {profile_path}")
                continue
            report.linked_profiles.add(full_path)
            linked = load_json(full_path, report)
            if not isinstance(linked, dict):
                continue
            language_data = linked.get("language")
            if not isinstance(language_data, dict):
                report.error(f"{relative(full_path)}: language harus berupa object.")
                continue
            if language_data.get("iso_639_3") != language.get("iso_639_3"):
                report.error(f"{relative(full_path)}: ISO bahasa tidak cocok dengan katalog negara.")
            stats["linked_profiles"] += 1

        profile_files = sorted((country_file.parent / "languages").glob("*/profile.json"))
        stats["profile_files"] = len(profile_files)
        for profile_file in profile_files:
            check_profile(profile_file, folder_code, report)
            if profile_file.resolve() not in report.linked_profiles:
                report.error(f"{relative(profile_file)}: profil tidak ditautkan oleh country.json.")

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
