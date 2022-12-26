class StateAvgTuitionRow:
    def __init__(self, column1, column2, column3, column4, column5, 
    column6, column7, column8, column9, column10, column11, column12):
        # set columns values in a list
        self.columns = [
            column1, column2, column3, column4, column5, 
    column6, column7, column8, column9, column10, column11, column12
        ]

    ## make the objects indexable    
    def __getitem__(self, key):
        return self.columns[key]
