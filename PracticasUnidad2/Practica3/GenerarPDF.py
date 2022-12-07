import csv
from fpdf import FPDF


class PDF(FPDF):
   

    def colored_table(self, headings, rows, col_widths=(42, 39, 35, 42)):
        # Colors, line width and bold font:
        self.set_fill_color(255, 100, 0)
        self.set_text_color(255)
        self.set_draw_color(255, 0, 0)
        self.set_line_width(0.3)
        self.set_font(style="B")
        for col_width, heading in zip(col_widths, headings):
            self.cell(col_width, 7, heading, border=1, align="C", fill=True)
        self.ln()
        # Color and font restoration:
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font()
        fill = False
        for row in rows:
            self.cell(col_widths[0], 6, row[0], border="LR", align="L", fill=fill)
            self.cell(col_widths[1], 6, row[1], border="LR", align="L", fill=fill)
            self.cell(col_widths[2], 6, row[2], border="LR", align="R", fill=fill)
            self.cell(col_widths[3], 6, row[3], border="LR", align="R", fill=fill)
            self.ln()
            fill = not fill
        self.cell(sum(col_widths), 0, "", "T")


def load_data_from_csv(csv_filepath):
    headings, rows = [], []
    with open(csv_filepath, encoding="utf8") as csv_file:
        for row in csv.reader(csv_file, delimiter=","):
            if not headings:  # extracting column names from first row:
                headings = row
            else:
                rows.append(row)
    return headings, rows


col_names, data = load_data_from_csv("countries.txt")
pdf = PDF()
pdf.set_font("helvetica", size=14)
pdf.add_page()
pdf.basic_table(col_names, data)
pdf.add_page()
pdf.improved_table(col_names, data)
pdf.add_page()
pdf.colored_table(col_names, data)
pdf.output("tuto5.pdf")