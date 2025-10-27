from fpdf import FPDF

import pandas as pd


pdf = FPDF(orientation="P",unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=row['Topic'], border=0, ln=1, align='L')    
  
    # to show lines in the page   // my solution
    # x = 27
    # while x <= 277:        
    #     pdf.line(10, x, 200, x)
    #     x +=10
        
    # to show lines in the page // course teacher solution 
    for y in range(27, 298, 10):
         pdf.line(10, y, 200, y)
    pdf.line(10, 28, 200, 28)
    
    # set the footers
    pdf.ln(240)
    pdf.set_font(family='Times',style='I', size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=24, txt=row['Topic'], ln=1, align='R')

    
    for i in range(row['Pages']-1):
        pdf.add_page()
        
        # to show lines in the page   
        # x = 7
        # while x <= 277:        
        #     pdf.line(10, x, 200, x)
        #     x +=10

        # to show lines in the page // course teacher solution 
        for y in range(10, 298, 10):
            pdf.line(10, y, 200, y)

        # set the footers
        pdf.ln(270)
        pdf.set_font(family='Times',style='I', size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=24, txt=row['Topic'], ln=1, align='R')


pdf.output('output.pdf')