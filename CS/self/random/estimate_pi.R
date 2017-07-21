## Estimate pi
## December 30, 2016

library(tidyverse)
library(stringr)


setwd("C:/Users/homur/OneDrive/CS/self/random/")

N = 1000
pi = 0

for (i in 1:N) {
	x_i = runif(n=1, min=-1, max=1)
	y_i = runif(n=1, min=-1, max=1)

	if(x_i**2 + y_i**2 <= 1) {
		pi = pi + 1
		plot(x_i, y_i, xlim=c(-1,1), ylim=c(-1,1))
		par(new=TRUE)
	}
}
par(new=FALSE)
4*pi/N