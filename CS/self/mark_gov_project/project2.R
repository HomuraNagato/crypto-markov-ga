# Bond project compilation
install.packages("reshape")
install.packages("reshape2")
install.packages("tidyverse")
library("reshape")
library("reshape2")
library(tidyverse)
library(xlsx)

filenames = as.list(dir(pattern="*.csv"))
for(i in 1:length(filenames)) {
  data_i <-  lapply(filenames, read.csv, header=TRUE)
}

df <- do.call(cbind.data.frame, data)



df2 <- dcast(df,  LOCATION ~ Value)


# # Appendix of previous attempts
# # practice loop
# #list = c("defence", "education")
# #as.character(list)
# #for (i in 1:length(list)) {
# #  print(list[i])
# #  i+1
# #}
# 
# df_i <- df[, c("TIME", "LOCATION", "Value", "SUBJECT")]
# 
# # lets rename the column Value to its subject in a cool way
# # trial checking
# #class(df$SUBJECT[2])
# #class(name1)
# name1 <- as.character(df$SUBJECT[1])
# # name1
# # names(df) <- c("TIME", "LOCATION", name1, "SUBJECT")
# # names(df)
# rename(df, c(Value=name1))
# }
# 
# /##