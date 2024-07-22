library(readr)

file_path <- "data/directory-homeless-population-by-year.csv"

df <- read_csv(file_path)

print(head(df))

print(summary(df))

print(colnames(df))
