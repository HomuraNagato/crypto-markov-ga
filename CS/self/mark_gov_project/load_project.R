##Mark_gov_project
## Loading data
## December 30, 2016

library(tidyverse)
library(stringr)


setwd("C:/Users/homur/OneDrive/CS/self/mark_gov_project/")
d_def <- read_csv("defence.csv")
d_econ <- read_csv("economic_affairs.csv")
d_edu <- read_csv("education.csv")


d_arr <- list(d_econ)
d_names <- list("def")
x1 <- "def"

View(d_edu)
View(d_merge)

## Need to rename subject and value, and drop flag codes
d_merge <- d_def[,-8]
d_merge <- d_def %>% rename(as.character(paste(x1,"Subject")) = SUBJECT)
names(d_merge)
for( i in 1:length(d_arr)) {
	d_merge <- inner_join(d_merge, data.frame(d_arr[i]), by=c("LOCATION", "TIME", "INDICATOR", "MEASURE", "FREQUENCY"))
	#d_merge <- inner_join(d_merge, data.frame(d_arr[i]))
}
str(d_merge)