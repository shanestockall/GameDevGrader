import pandas as pd



def main():
    caesarCSV = open("./gradebook.csv")
    canvasCSV = open("./grades.csv")
    
    a = pd.read_csv(caesarCSV)
    b = pd.read_csv(canvasCSV)

    merged = a.merge(b, on='ID')
    merged.to_csv("upload.csv")
if __name__ == '__main__':
    main()
