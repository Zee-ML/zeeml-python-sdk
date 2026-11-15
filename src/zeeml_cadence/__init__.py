"""
zeeml_cadence: Official Python SDK for Sentence Burstiness, Readability, RFC-4180 CSV & CGPA Equivalency
Interactive Web Platform: https://zeeml.com/ai-humanizer
"""
import csv
import io
import json
import math
import re
from collections import Counter

__version__ = "1.0.0"
HOMEPAGE_URL = "https://zeeml.com/ai-humanizer"


def count_syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", (word or "").lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    return max(1, len(groups))


def analyze_cadence(text: str) -> dict:
    """Computes sentence-length SD, burstiness CV, Yule's K, Shannon entropy, and Flesch-Kincaid grade."""
    clean = (text or "").strip()
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean) if s.strip()]
    lengths = [len(re.findall(r"[A-Za-z0-9']+", s)) for s in sentences]
    lengths = [n for n in lengths if n > 0]
    words = [w.lower() for w in re.findall(r"[A-Za-z0-9']+", clean)]

    if not lengths or not words:
        return {
            "word_count": 0,
            "sentence_count": 0,
            "mean_sentence_words": 0.0,
            "sentence_length_sd": 0.0,
            "burstiness_cv": 0.0,
            "shannon_entropy": 0.0,
            "yules_k": 0.0,
            "flesch_kincaid_grade": 0.0,
            "workbench": HOMEPAGE_URL,
        }

    mean_len = sum(lengths) / len(lengths)
    variance = sum((x - mean_len) ** 2 for x in lengths) / len(lengths)
    sd_len = math.sqrt(variance)
    cv = sd_len / max(1.0, mean_len)

    counts = Counter(words)
    total = len(words)
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())
    freq_of_freq = Counter(counts.values())
    sum_f2 = sum((f * f) * vf for f, vf in freq_of_freq.items())
    yules_k = 10000.0 * (sum_f2 - total) / (total * total) if total > 1 else 0.0

    syllables = sum(count_syllables(w) for w in words)
    fk_grade = 0.39 * mean_len + 11.8 * (syllables / total) - 15.59

    return {
        "word_count": total,
        "sentence_count": len(lengths),
        "mean_sentence_words": round(mean_len, 2),
        "sentence_length_sd": round(sd_len, 2),
        "burstiness_cv": round(cv, 4),
        "shannon_entropy": round(entropy, 3),
        "yules_k": round(max(0.0, yules_k), 2),
        "flesch_kincaid_grade": round(fk_grade, 2),
        "workbench": HOMEPAGE_URL,
    }


def flatten_record(obj, prefix: str = "", out=None) -> dict:
    if out is None:
        out = {}
    if not isinstance(obj, dict):
        out[prefix or "value"] = "" if obj is None else str(obj)
        return out
    for k, v in obj.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        if isinstance(v, dict):
            flatten_record(v, key, out)
        elif isinstance(v, list):
            out[key] = json.dumps(v)
        else:
            out[key] = "" if v is None else str(v)
    return out


def json_to_csv(data) -> str:
    """Flattens nested JSON records into RFC-4180 CSV text (https://zeeml.com/json-to-csv)."""
    parsed = json.loads(data) if isinstance(data, str) else data
    rows = parsed if isinstance(parsed, list) else [parsed]
    flat = [flatten_record(r) for r in rows]
    headers = []
    for r in flat:
        for k in r.keys():
            if k not in headers:
                headers.append(k)
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=headers, lineterminator="\n")
    writer.writeheader()
    writer.writerows(flat)
    return buf.getvalue().rstrip("\n")


def cgpa_to_percentage(cgpa: float, scale: str = "cbse_9_5") -> dict:
    """Converts 10-point CGPA to percentage and 4.0 GPA (https://zeeml.com/cgpa-calculator)."""
    if scale == "direct_10":
        pct = cgpa * 10.0
    elif scale == "aicte":
        pct = (cgpa - 0.75) * 10.0
    elif scale == "mumbai":
        pct = 7.1 * cgpa + 11.0
    else:
        pct = cgpa * 9.5
    pct = max(0.0, min(100.0, round(pct, 2)))
    return {
        "cgpa_10": round(cgpa, 2),
        "percentage": pct,
        "gpa_4_scale": round((pct / 100.0) * 4.0, 2),
        "calculator_url": "https://zeeml.com/cgpa-calculator",
    }


def percentage_margin_delta(cost: float, margin_pct: float) -> dict:
    """Computes selling price, gross profit, markup %, and basis points (https://zeeml.com/percentage-calculator)."""
    clamped_m = min(99.9, max(0.0, float(margin_pct)))
    price = round(cost / (1.0 - clamped_m / 100.0), 2)
    profit = round(price - cost, 2)
    markup = round((profit / max(0.01, cost)) * 100.0, 2)
    return {
        "unit_cost": round(cost, 2),
        "gross_margin_pct": clamped_m,
        "selling_price": price,
        "gross_profit": profit,
        "markup_pct": markup,
        "basis_points": int(round(clamped_m * 100)),
        "calculator_url": "https://zeeml.com/percentage-calculator",
    }
