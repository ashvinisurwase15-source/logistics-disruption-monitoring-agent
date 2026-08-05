from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_pdf(report):
    os.makedirs("generated_reports", exist_ok=True)

    filename = f"generated_reports/report_{report.generated_at.replace(':', '-').replace(' ', '_')}.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 750, "EV Battery Supply Chain Report")

    c.setFont("Helvetica", 12)

    y = 710

    c.drawString(50, y, f"Generated At: {report.generated_at}")
    y -= 25

    c.drawString(50, y, f"Total News: {report.total_news}")
    y -= 25

    c.drawString(50, y, f"High Risk Events: {report.high_risk_events}")
    y -= 25

    c.drawString(50, y, "Suppliers Impacted:")
    y -= 20

    if report.suppliers_impacted:
        for supplier in report.suppliers_impacted:
            c.drawString(70, y, f"- {supplier}")
            y -= 20
    else:
        c.drawString(70, y, "None")
        y -= 20

    y -= 10
    c.drawString(50, y, "Summary:")
    y -= 20

    text = c.beginText(50, y)
    text.textLines(report.summary)
    c.drawText(text)

    c.save()

    return filename