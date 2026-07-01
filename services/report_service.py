from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from reportlab.lib import colors


class ReportService:

    def generate_report(
        self,
        filename,
        claim_id,
        result,
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>ClaimVision AI Assessment Report</b>",
                styles["Title"],
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"<b>Claim ID:</b> {claim_id}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Estimated Cost:</b> ₹{result.total_cost:,.0f}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Fraud Score:</b> {result.fraud['fraud_score']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Risk Level:</b> {result.fraud['risk_level']}",
                styles["Normal"],
            )
        )

        story.append(Spacer(1, 20))

        data = [
            [
                "Damage ID",
                "Severity",
                "Area",
                "Width",
                "Height",
            ]
        ]

        for damage in result.damages:

            data.append(
                [
                    damage["damage_id"],
                    damage["severity"],
                    round(damage["area"], 2),
                    damage["width"],
                    damage["height"],
                ]
            )

        table = Table(data)

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ]
            )
        )

        story.append(table)

        doc.build(story)