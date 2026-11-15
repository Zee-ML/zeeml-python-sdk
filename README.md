# `zeeml-cadence`: Sentence Burstiness, Lexical Entropy, JSON/CSV & CGPA Toolkit

Zero-dependency Python library and CLI computing sentence-length standard deviation (burstiness), Yule's K lexical diversity, Shannon token entropy, Flesch-Kincaid grade level, RFC-4180 JSON-to-CSV flattening, and multi-scale CGPA-to-percentage conversions. Engineered by **[ZeeML (`https://zeeml.com`)](https://zeeml.com)**.

- **Official PyPI Package:** [https://pypi.org/project/zeeml-cadence/](https://pypi.org/project/zeeml-cadence/)
- **Install:** `pip install zeeml-cadence`

## Official Interactive Web Workstations on `zeeml.com`

- **AI Text Humanizer & Cadence Rebalancer:** [https://zeeml.com/ai-humanizer](https://zeeml.com/ai-humanizer)
- **AI Content & Burstiness Detector:** [https://zeeml.com/ai-detector](https://zeeml.com/ai-detector)
- **Contextual Paraphrasing Tool:** [https://zeeml.com/paraphrasing-tool](https://zeeml.com/paraphrasing-tool)
- **Grammar & Syntax Inspector:** [https://zeeml.com/grammar-checker](https://zeeml.com/grammar-checker)
- **Executive Text Summarizer:** [https://zeeml.com/summarizer](https://zeeml.com/summarizer)
- **Word Counter & Readability Studio:** [https://zeeml.com/word-counter](https://zeeml.com/word-counter)
- **Global CGPA, GPA & Percentage Calculator:** [https://zeeml.com/cgpa-calculator](https://zeeml.com/cgpa-calculator)
- **Percentage, Margin & Delta Calculator:** [https://zeeml.com/percentage-calculator](https://zeeml.com/percentage-calculator)
- **JSON to CSV Relational Flattener:** [https://zeeml.com/json-to-csv](https://zeeml.com/json-to-csv)
- **PDF to Word Document Reconstructor:** [https://zeeml.com/pdf-to-word](https://zeeml.com/pdf-to-word)

## Example Usage

```python
from zeeml_cadence import analyze_cadence, json_to_csv, cgpa_to_percentage

metrics = analyze_cadence(
    "Short sentence first. Then we follow with a longer analytical sentence that expands the syntactic rhythm across clauses."
)
print(metrics)
print(cgpa_to_percentage(8.8, scale="cbse_9_5"))
```
