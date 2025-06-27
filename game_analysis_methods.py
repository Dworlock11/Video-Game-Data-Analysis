import pandas as pd

class DataFrame_Manipulator():
    def __init__ (self, df):
        self.df = df

    def top_bottom_n(self, col, extreme, n=5):
        '''
        Returns a DataFrame with the top or bottom of a specified column by the names.

        Parameters
        ----------
        col (string): the name of the column containing the desired information.
        extreme (string): should be "top" for the top values and "bottom" for the bottom values.
        n (int): the number of rows of the DataFrame returned.
        '''

        top_bottom_values = None
        indexed_df = self.df.set_index("Name")

        if extreme == "top":
            top_bottom_values = indexed_df.sort_values(col, ascending=False).head(n)
        elif extreme == "bottom":
            top_bottom_values = indexed_df.sort_values(col, ascending=True).head(n)
            
        return top_bottom_values
    
    def elements_per_group(self, col, n=5):
        '''
        Groups the DataFrame by a certain column and returns a DataFrame with the number of elements per group.

        Parameters
        ----------

        col (string): the name of the column containing the desired information.        
        n (int): the number of rows of the DataFrame returned.
        '''
        
        elements_counted = self.df.groupby(col)[col].count().sort_values(ascending=False).head(n)
        return elements_counted