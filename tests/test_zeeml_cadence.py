import unittest
from zeeml_cadence import analyze_cadence, json_to_csv, cgpa_to_percentage, percentage_margin_delta


class TestZeemlCadence(unittest.TestCase):
    def test_cadence_burstiness(self):
        res = analyze_cadence(
            "Short sentence first. Then we follow with a significantly longer analytical sentence that expands the syntactic rhythm across multiple clauses."
        )
        self.assertEqual(res["sentence_count"], 2)
        self.assertGreater(res["burstiness_cv"], 0.40)

    def test_json_to_csv(self):
        csv_txt = json_to_csv([{"id": 1, "meta": {"tag": "alpha,beta"}}])
        self.assertIn("meta.tag", csv_txt)
        self.assertIn('"alpha,beta"', csv_txt)

    def test_cgpa_and_margin(self):
        gpa = cgpa_to_percentage(9.0, "cbse_9_5")
        self.assertEqual(gpa["percentage"], 85.5)
        margin = percentage_margin_delta(60.0, 40.0)
        self.assertEqual(margin["selling_price"], 100.0)


if __name__ == "__main__":
    unittest.main()
