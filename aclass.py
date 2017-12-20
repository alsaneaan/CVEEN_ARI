class clean_df(object):
    
    '''
    This class will take a dataframe and clean it (as in remove all NA values)
    The class representation (__repr__) will return:
    - the dataframe's shape
    - list of column names
    
    '''
    def __init__(self, df):
        self.__df = df
        self._clean()
    @property
    def df(self):
        return self.__df
    def _clean(self):
        return self.__df.dropna(how = 'any', inplace=True)
    
    def __str__(self):
        return "column headers: %s"%(self.__df.columns.tolist())  

    def __repr__(self):
        return "The dataframe after cleaning has a of shape of (rows, columns): %s and %s"%( self.__df.shape,self.__str__())
    
class stats_data (clean_df):
    
    '''
    This class will calculate that average and total of a specified column given
    
    Class format will be:
    stats_data('column_name',dataframe)
    
    if the column name is not found in the dataframe, a key error will be raised
    
    The class representation will produce:
    - the average 
    - the total 
    
    '''
    
    #import the dataframe as a self in the instructor
    def __init__(self, cl, *args ):
        self.__cl = cl
        super(stats_data, self).__init__(*args)
        
        
    
    @property
    def cl(self):
        return self.__cl
    @cl.setter
    def cl(self, c):
        if c in self.df.columns:
            self.__cl = c
        
    def avg (self):
        return self.df[self.cl].mean()
        #return avg_feed
   
    def total (self):
        return self.df[self.cl].sum()
    
    
   # def __str__(self):
   #     return "avg: %4.4f; sum: %4.4f"%(self.avg_feed(), self.sum_feed())
                
    def __repr__(self):
        return "The average value of %s: %4.2f and the total is: %4.2f"%(self.cl, self.avg(), self.total())
    
    
        
    
     