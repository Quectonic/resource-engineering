from bs4 import BeautifulSoup
import pandas as pd

class HtmlTableTransformer:
    
    """
        Table Processing Class
         -  Converting html '\<table\> ... \</table\>' into:
             - Text // string format
             - pandas dataframe
    """
    
    
    def __init__(self, table_html) -> None:
        try:
            self.table_html = BeautifulSoup(table_html, 'lxml')
        except:
            self.table_html = BeautifulSoup(table_html, 'html.parser')
            print(f'lxml unusable, switching to html.parser')
        self.rows = self.parse_table()
        self.text = self.toText()
        # <html><body><a></a></body></html>
        
    ## Expect the table to be in the format 
    ## <table> ... </table> --> no further processing is needed
    def parse_table(self):
        rows = []
        row_spans = {}
        for row_idx, row in enumerate(self.table_html.find_all('tr')):
            cells = []
            col_idx = 0

            for cell in row.find_all(['td', 'th']):
                # Handle any ongoing rowspans from previous rows
                while col_idx in row_spans and row_spans[col_idx]['count'] > 0:
                    cells.append(row_spans[col_idx]['value'])
                    row_spans[col_idx]['count'] -= 1
                    if row_spans[col_idx]['count'] == 0:
                        del row_spans[col_idx]
                    col_idx += 1

                # Extract text and handle rowspan and colspan
                cell_text = cell.get_text().replace('\n', '')
                rowspan = int(cell.get('rowspan', 1))
                colspan = int(cell.get('colspan', 1))

                # Place the current cell's value in the appropriate column(s)
                for _ in range(colspan):
                    cells.append(cell_text)
                    col_idx += 1

                # If the cell has a rowspan, mark it to be carried over to the subsequent rows
                if rowspan > 1:
                    for i in range(colspan):
                        row_spans[col_idx - colspan + i] = {'value': cell_text, 'count': rowspan - 1}

            # Handle any remaining rowspans after processing all cells in this row
            while col_idx in row_spans and row_spans[col_idx]['count'] > 0:
                cells.append(row_spans[col_idx]['value'])
                row_spans[col_idx]['count'] -= 1
                if row_spans[col_idx]['count'] == 0:
                    del row_spans[col_idx]
                col_idx += 1

            # Append the parsed row to the final result
            rows.append(cells)

        return rows

    def toText(self):
        processed_table = []
        for row in self.rows:
            processed_row = f'|| {" | ".join(row)} ||'
            processed_table.append(processed_row)
        processed_table = '\n'.join(processed_table)
        return processed_table
    
    def toDataframe(self):
        header_row = None
        for row in self.rows:
            if any(row):
                header_row = row
                break
        
        df = pd.DataFrame(self.rows, columns=header_row)
        return df
    
    def encodeText(self):
        
        ## To detect table: look for "<table> ||" beginning and "|| <table>" ending
        
        textTable = self.toText()
        return f"<table> {textTable} <table>"
    
class HTMLListTransformer:
    """
        List Processing Class
         -  Converting html '\<ul\> ... \</ul\>' into:
             - Text // string format
    """
    
    
    def __init__(self, ul_html) -> None:
        try:
            self.table_html = BeautifulSoup(ul_html, 'lxml')
        except:
            self.table_html = BeautifulSoup(ul_html, 'html.parser')
        self.list = self.parse_list()
        # <html><body><a></a></body></html>
        
    ## Expect the table to be in the format 
    ## <table> ... </table> --> no further processing is needed
    def parse_list(self):
        bulletpoints = self.ul_html.find_all('li')
        items = [item.get_text() for item in bulletpoints]
        
        ## PROBLEM: parsing links
        ##          Including link url etc. how could it be infused into JSON?

        return items

    def toText(self):
        processed_table = []
        for row in self.rows:
            processed_row = f'|| {" | ".join(row)} ||'
            processed_table.append(processed_row)
        processed_table = '\n'.join(processed_table)
        return processed_table
    
    def encodeText(self):
        
        ## To detect table: look for "<table> ||" beginning and "|| <table>" ending
        
        textTable = self.toText()
        return f"<table> {textTable} <table>"