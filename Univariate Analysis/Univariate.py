class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtype!='O'):
                #print("quan")
                quan.append(columnName)
            else:
                #print("qual")
                qual.append(columnName)
        return quan,qual