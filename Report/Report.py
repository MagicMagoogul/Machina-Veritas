# Author: Riley Owen
# Date: 10/30/2025
# Description:
# This module generates a summary report of the analysis results.
# Rates the EHR based on a percentage:
# 0-25% EHR = CRITICAL
# 26-50% EHR = HIGH
# 51-75% EHR = MODERATE
# 76-100% EHR = LOW

from datetime import datetime

class ReportGenerator:
    def __init__(self, image_analyzer, text_analyzer, network_analyzer):
        """
        Initialize with instances of other analysis classes.
        Each analyzer should have a `get_score()` and `get_summary()` method.
        """
        self.image_analyzer = image_analyzer
        self.text_analyzer = text_analyzer
        self.network_analyzer = network_analyzer

    def calculate_overall_ehr(self):
        """Calculate the average EHR score from all three analyzers."""
        scores = [
            self.image_analyzer.get_score(),
            self.text_analyzer.get_score(),
            self.network_analyzer.get_score()
        ]
        overall = sum(scores) / len(scores)
        return round(overall, 2)

    def rate_ehr(self, score):
        """Return a human-readable rating based on EHR percentage."""
        if score <= 25:
            return "CRITICAL"
        elif score <= 50:
            return "HIGH"
        elif score <= 75:
            return "MODERATE"
        else:
            return "LOW"

    def generate_report(self, filename="ehr_report.txt"):
        """Generate a detailed text report summarizing the findings."""
        overall_score = self.calculate_overall_ehr()
        rating = self.rate_ehr(overall_score)

        report_lines = [
            f"Employee Humanity Rating (EHR) Summary Report",
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "-" * 50,
            f"Image Analysis Score: {self.image_analyzer.get_score()}%",
            f"Text Analysis Score:  {self.text_analyzer.get_score()}%",
            f"Network Analysis Score:{self.network_analyzer.get_score()}%",
            "-" * 50,
            f"Overall EHR Score:     {overall_score}%",
            f"Overall Rating:        {rating}",
            "-" * 50,
            "DETAILED SUMMARIES:",
            "",
            "[IMAGE ANALYSIS]",
            self.image_analyzer.get_summary(),
            "",
            "[TEXT ANALYSIS]",
            self.text_analyzer.get_summary(),
            "",
            "[NETWORK ANALYSIS]",
            self.network_analyzer.get_summary(),
            "",
            "END OF REPORT"
        ]

        with open(filename, "w") as file:
            file.write("\n".join(report_lines))

        print(f"[+] Report successfully generated: {filename}")


# Example usage (remove or modify as needed)
if __name__ == "__main__":
    class DummyAnalyzer:
        def __init__(self, score, summary):
            self.score = score
            self.summary = summary

        def get_score(self):
            return self.score

        def get_summary(self):
            return self.summary

    # Example test data
    image = DummyAnalyzer(45, "Facial features show synthetic inconsistencies.")
    text = DummyAnalyzer(65, "Writing style partially AI-generated.")
    network = DummyAnalyzer(80, "Online footprint consistent with human behavior.")

    generator = ReportGenerator(image, text, network)
    generator.generate_report("ehr_summary_report.txt")
