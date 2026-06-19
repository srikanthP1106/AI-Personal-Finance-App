from reportlab.pdfgen import canvas


def generate_pdf_report():

    pdf = canvas.Canvas("finance_report.pdf")

    pdf.drawString(
        100,
        800,
        "AI Personal Finance Report"
    )

    pdf.drawString(
        100,
        770,
        "Generated Successfully"
    )

    pdf.save()

    return "finance_report.pdf"