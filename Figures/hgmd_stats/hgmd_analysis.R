library(ggplot2)

getwd()
setwd("/home/raony/Dropbox/Doutorado/myphdthesis/qualificacao/Figures/hgmd_stats")
mydata = read.csv("hgmd_stats.csv")
?sort
year_stats = cbind(mydata[1], cumsum(mydata[3]))
names(year_stats)
table(year_stats)
year_stats[,2]

plot(year_stats)

hgmd_stats <- as.data.frame(year_stats)

names(hgmd_stats)[1] <- paste("years")
names(hgmd_stats)[2] <- paste("mutations")

lines(lowess(year_stats))
lines(year_stats)

# plot(cars)


#nice try
qplot(x = years, y=mutations, data = hgmd_stats, geom = c("point", "smooth"), span = 0.1) +
  geom_point() +  
  scale_x_continuous(breaks = seq(1977,2013,2))


qplot(x = years, y=mutations, data = hgmd_stats, geom = "point")

qplot(x = years, y=mutations, data = hgmd_stats, stat = "ecdf")

?apply

qplot(rnorm(1000), stat = "ecdf", geom = "step")
df <- data.frame(x = c(rnorm(100, 0, 3), rnorm(100, 0, 10)),
                 g = gl(2, 100))
ggplot(df, aes(x, colour = g)) + stat_ecdf()

ggplot(hgmd_stats, aes(years)) + stat_ecdf()
cumsum(c(1,2,3))
?qplot
qplot(c(1,2,3), stat = "ecdf", geom = "step")

(ii <- order(x <- c(1,1,3:1,1:4,3), y <- c(9,9:1), z <- c(2,1:9)))
## 6  5  2  1  7  4 10  8  3  9
rbind(x, y, z)[,ii] # shows the reordering (ties via 2nd & 3rd arg)
?order

order(hgmd_stats['mutations'])