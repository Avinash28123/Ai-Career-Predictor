from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AI Career Predictor - Report', 0, 1, 'C')

def create_pdf(report_data, out_path='career_report.pdf'):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    for k, v in report_data.items():
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 8, str(k), 0, 1)
        pdf.set_font('Arial', '', 11)
        if isinstance(v, dict):
            for kk, vv in v.items():
                pdf.multi_cell(0, 7, f"{kk}: {vv}")
        else:
            pdf.multi_cell(0, 7, str(v))
        pdf.ln(3)
    pdf.output(out_path)
    return out_path
