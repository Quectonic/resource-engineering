from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
from abc import ABC, abstractmethod

class Transformer(ABC):
    @abstractmethod
    def parse(self) -> list:
        pass
    
    @abstractmethod
    def toText(self) -> str:
        pass
    
    # @abstractmethod
    # def toDataFrame(self) -> DataFrame:
    #     pass
    

class HtmlTableTransformer(Transformer):
    
    """
        Table Processing Class
         -  Converting html '\<table\> ... \</table\>' into:
             - Text // string format
             - pandas dataframe
             
        2 Ways of instantiation:
         -  Instantiate by table_list (processed table html, formatted as list object)
             - Account for subcontent inside cells (e.g. links, medias) using ElementDict
         -  Instantiate by table_html (raw html)
             - Purely concatenated text inside cells
    """
    
    
    def __init__(self, *, table_list = None, table_html = None) -> None:
        if table_html:
            try:
                self.table_html = BeautifulSoup(table_html, 'lxml')
            except:
                self.table_html = BeautifulSoup(table_html, 'html.parser')
                print(f'lxml unusable, switching to html.parser')
            
            self.table_list = self.parse()
            self.table_ED_list = self.parse_with_elementdict()
        elif table_list:
            self.table_list = table_list
            self.table_ED_list = None
        else:
            raise ValueError('No table resource was referred to.')
        self.text = self.toText()
        # <html><body><a></a></body></html>
        
    def parse(self):
        
        """
        Extract everything in textual format
        """
        
        try:
            table_list = []
            row_spans = {}
            for row_idx, row in enumerate(self.table_html.find_all('tr')):
                cells = []
                col_idx = 0

                for cell in row.find_all(['td', 'th']):
                    # Handle any ongoing rowspans from previous table_list
                    ## checking if the column requires prior stacking
                    ## checking if the row requires left side stacking
                    while col_idx in row_spans and row_spans[col_idx]['count'] > 0:
                        cells.append(row_spans[col_idx]['value'])
                        row_spans[col_idx]['count'] -= 1
                        if row_spans[col_idx]['count'] == 0:
                            del row_spans[col_idx]
                        col_idx += 1


                    # Extract text
                    cell_text = cell.get_text().replace('\n', '')
                    # Handle rowspan & colspan
                    rowspan = int(cell.get('rowspan', 1))
                    colspan = int(cell.get('colspan', 1))

                    # Place the current cell's value in the appropriate column(s)
                    for _ in range(colspan):
                        cells.append(cell_text)
                        col_idx += 1

                    # If the cell has a rowspan, mark it to be carried over to the subsequent table_list
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
                table_list.append(cells)

            return table_list
        except Exception as e:
            raise ValueError(f'table parsing error: {e}')
    
    def parse_with_elementdict(self):
        
        """
        Extract everything in ElementDict format
        """
        
        ## TODO: 
        # the result is empty, need to check the implementation
        
        from mdkengineering.utils.Parse import transform_tag_to_ElementDict

        # print(f"input html: {type(self.table_html)}...\n")
        table_list = [] # The "row" field value
        row_spans = {}
        try:
            for row_idx, row in enumerate(self.table_html.find_all(('tr'))): ## html to be replaced by self.tablehtml
                
                cells = []
                col_idx = 0
                
                for cell_idx, cell in enumerate(row.find_all(['th', 'td'])):

                    # print(f"found th / tr: {cell_idx}")
                    
                    while col_idx in row_spans and row_spans[col_idx]['count'] > 0:
                        
                        ## Considering how many cells the row should skip for the next value

                        # print(f"appending row_spans[col_idx]['value']: {row_spans[col_idx]['value']}\n")
                        
                        cells.append(row_spans[col_idx]['value'])
                        row_spans[col_idx]['count'] -= 1
                        if row_spans[col_idx]['count'] == 0:
                            del row_spans[col_idx]
                        col_idx += 1
                        
                        
                    cell_content = []
                    
                    for item in cell.contents:
                        cell_content.append(transform_tag_to_ElementDict(item))
                    
                    
                    rowspan = int(cell.get('rowspan', 1))
                    colspan = int(cell.get('colspan', 1))
                    
                    
                    for _ in range(colspan):
                        cells.append(cell_content) ## APPEND CURRENT CELL CONTENT!!!
                        col_idx += 1
                    
                    if rowspan > 1:
                        for i in range(colspan):
                            row_spans[col_idx - colspan + i] = {'value': cell_content, 'count': rowspan - 1}
                            
                while col_idx in row_spans and row_spans[col_idx]['count'] > 0:
                    cells.append(row_spans[col_idx]['value'])
                    row_spans[col_idx]['count'] -= 1
                    if row_spans[col_idx]['count'] == 0:
                        del row_spans[col_idx]
                    col_idx += 1
                    
                table_list.append(cells)
                
            return table_list
        except Exception as e:
            raise ValueError(f'table parsing error: {e}')
            
                
        

    def toText(self):
        processed_table = []
        for row in self.table_list:
            row_list = []
            for cell in row:
                row_list.append(HtmlTableTransformer.concatenate_cell_content(cell))
            processed_row = f'|| {" | ".join(row_list)} ||'
            processed_table.append(processed_row)
        processed_table = '\n'.join(processed_table)
        return processed_table
    
    @staticmethod
    def concatenate_cell_content(content):
        """
        Recursively flatten item inside a cell
        
        Parameter(s)
        ------------
        content: list || nested list
             -  content should be a cell list
        Return(s)
        ------------
        str: concatenated string from the list of content inside
             cell
        """
        concatenated_cell_content = ""
        
        
        for subcontent in content:
            if isinstance(subcontent, list):
                concatenated_cell_content += HtmlTableTransformer.concatenate_cell_content(subcontent)
            else:
                concatenated_cell_content += subcontent
                
        return concatenated_cell_content
    
    # def toDataFrame(self):
    #     if self.table_html:
    #         header_row = None
    #         for row in self.table_list:
    #             if any(row):
    #                 header_row = row
    #                 break
            
    #         df = pd.DataFrame(self.table_list, columns=header_row)
    #         return df
    #     else:
    #         ## FUTURE
    #         ## a different algorithm that concatenates the list of content inside each cell
    #         return
    
    # def encodeText(self):
        
    #     ## To detect table: look for "<table> ||" beginning and "|| <table>" ending
        
    #     textTable = self.toText()
    #     return f"<table> {textTable} <table>"
    
    
class HTMLListTransformer(Transformer):
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
    def parse(self):
        bulletpoints = self.ul_html.find_all('li')
        items = [item.get_text() for item in bulletpoints]
        
        ## PROBLEM: parsing links
        ##          Including link url etc. how could it be infused into JSON?

        return items

    def toText(self):
        processed_table = []
        for row in self.table_list:
            processed_row = f'|| {" | ".join(row)} ||'
            processed_table.append(processed_row)
        processed_table = '\n'.join(processed_table)
        return processed_table
    
    def encodeText(self):
        
        ## To detect table: look for "<table> ||" beginning and "|| <table>" ending
        
        textTable = self.toText()
        return f"<table> {textTable} <table>"