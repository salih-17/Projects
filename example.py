import pandas as pd
from datetime import datetime
import random



def main():
    df= pd.DataFrame ({'TimeNow':datetime.now()} , index=[0])
    file_name = str(int(random.random()*12345)) + "_df.csv"
    df.to_csv(file_name,index = False)


if __name__ == '__main__':
  main()
