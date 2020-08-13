#!/usr/bin/env Rscript
main <- function() {
    df <-read.csv("./2330.csv", header=T, sep=",")
    date = readline( prompt="Enter date: ")
    if (length(df[df['Date'] == date]) != 0){
        print(df[df['Date'] == date][5])
    }else{
        print('沒有該日期資料')
    }
}
main()


