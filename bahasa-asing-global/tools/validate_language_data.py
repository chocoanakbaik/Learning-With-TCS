#!/usr/bin/env python3
"""Validate LWT country catalogs and language profiles using Python stdlib only."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
COUNTRY_ROOT = ROOT / "bahasa-asing-global" / "negara"
REQUIRED_CATEGORIES = {
    "accent_and_pronunciation",
    "speaking_style_and_pragmatics",
    "standard_language",
    "nonstandard_language_and_slang",
    "profanity_and_vulgar_language",
    "regional_and_minority_languages",
}
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
        self.entries = 0
        self.drafts = 0
        self.reviewed = 0
        self.verified = 0

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def load_json(path: Path, report: Report) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        report.error(f"{path.relative_to(ROOT)}: gagal membaca JSON: {exc}")
        return None


def check_entry(entry: Any, path: Path, category: str, seen_ids: set[str], report: Report) -> None:
    label = f"{path.relative_to(ROOT)} [{category}]"
    if not isinstance(entry, dict):
        report.error(f"{label}: entri harus berupa object.")
        return

    missing = REQUIRED_ENTRY_FIELDS - set(entry)
    if missing:
        report.error(f"{label}: field wajib hilang: {', '.join(sorted(missing))}.")

    entry_id = entry.get("id")
    if not isinstance(entry_id, str) or not entry_id.strip():
        report.error(f"{label}: id harus berupa string non-kosong.")
    elif entry_id in seen_ids:
        report.error(f"{label}: ID duplikat: {entry_id}.")
    else:
        seen_ids.add(entry_id)

    status = entry.get("verification_status")
    if status not in VALID_STATUSES:
        report.error(f"{label}: verification_status tidak valid: {status!r}.")
    else:
        counter = {"draft": "drafts", "reviewed": "reviewed", "verified": "verified"}[status]
        setattr(report, counter, getattr(report, counter) + 1)

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
        if field in entry and (not isinstance(entry[field], str) or not entry[field].strip()):
            report.error(f"{label}: {field} harus berupa string non-kosong.")

    report.entries += 1


def check_profile(path: Path, country_code: str, seen_ids: set[str], report: Report) -> None:
    profile = load_json(path, report)
    if profile is None:
        return
    report.profiles += 1

    if profile.get("record_type") != "language_profile":
        report.error(f"{path.relative_to(ROOT)}: record_type harus language_profile.")
    if profile.get("schema_version") != "1.1.0":
        report.error(f"{path.relative_to(ROOT)}: schema_version harus 1.1.0.")

    context = profile.get("country_context", {})
    if context.get("country_code") != country_code:
        report.error(f"{path.relative_to(ROOT)}: country_context tidak cocok dengan folder {country_code}.")

    categories = profile.get("categories")
    if not isinstance(categories, dict):
        report.error(f"{path.relative_to(ROOT)}: categories harus berupa object.")
        return

    missing = REQUIRED_CATEGORIES - set(categories)
    extra = set(categories) - REQUIRED_CATEGORIES
    if missing:
        report.error(f"{path.relative_to(ROOT)}: kategori hilang: {', '.join(sorted(missing))}.")
    if extra:
        report.warn(f"{path.relative_to(ROOT)}: kategori tambahan: {', '.join(sorted(extra))}.")

    for category in REQUIRED_CATEGORIES:
        section = categories.get(category)
        if not isinstance(section, dict):
            report.error(f"{path.relative_to(ROOT)} [{category}]: harus berupa object.")
            continue
        entries = section.get("entries")
        if not isinstance(entries, list):
            report.error(f"{path.relative_to(ROOT)} [{category}]: entries harus berupa array.")
            continue
        for entry in entries:
            check_entry(entry, path, category, seen_ids, report)

    profile_sources = profile.get("sources", [])
    if not isinstance(profile_sources, list):
        report.error(f"{path.relative_to(ROOT)}: sources tingkat profil harus berupa array.")
    else:
        for source in profile_sources:
            if not isinstance(source, dict) or not isinstance(source.get("url"), str) or not source["url"].startswith("https://"):
                report.error(f"{path.relative_to(ROOT)}: setiap sumber profil harus memiliki URL https://.")

    status = profile.get("verification", {}).get("status", "")
    if "not_native_validated" in status:
        report.warn(f"{path.relative_to(ROOT)}: profil belum divalidasi penutur asli/ahli.")


def main() -> int:
    report = Report()
    seen_ids: set[str] = set()

    if not COUNTRY_ROOT.is_dir():
        print(f"ERROR: direktori tidak ditemukan: {COUNTRY_ROOT}")
        return 2

    country_files = sorted(COUNTRY_ROOT.glob("*/country.json"))
    if not country_files:
        report.error("Tidak ditemukan country.json.")

    for country_file in country_files:
        country = load_json(country_file, report)
        if country is None:
            continue
        code = country.get("country", {}).get("iso_3166_1_alpha2")
        folder_code = country_file.parent.name
        if code != folder_code:
            report.error(f"{country_file.relative_to(ROOT)}: kode ISO negara tidak cocok dengan nama folder.")
        if country.get("record_type") != "country_profile":
            report.error(f"{country_file.relative_to(ROOT)}: record_type harus country_profile.")

        language_records = country.get("languages", [])
        if not isinstance(language_records, list):
            report.error(f"{country_file.relative_to(ROOT)}: languages harus berupa array.")
            language_records = []

        for language in language_records:
            if not isinstance(language, dict):
                report.error(f"{country_file.relative_to(ROOT)}: setiap record bahasa harus berupa object.")
                continue
            profile_path = language.get("profile_path")
            if profile_path:
                full_path = country_file.parent / profile_path
                if not full_path.is_file():
                    report.error(f"{country_file.relative_to(ROOT)}: profile_path tidak ditemukan: {profile_path}")
                else:
                    linked = load_json(full_path, report)
                    if linked is not None:
                        lang_code = linked.get("language", {}).get("iso_639_3")
                        if lang_code != language.get("iso_639_3"):
                            report.error(f"{full_path.relative_to(ROOT)}: ISO bahasa tidak cocok dengan katalog negara.")

        for profile_file in sorted((country_file.parent / "languages").glob("*/profile.json")):
            check_profile(profile_file, folder_code, seen_ids, report)

    print("LWT DATA VALIDATION")
    print(f"Country catalogs : {len(country_files)}")
    print(f"Language profiles: {report.profiles}")
    print(f"Learning entries : {report.entries}")
    print(f"Draft / reviewed / verified: {report.drafts} / {report.reviewed} / {report.verified}")
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
