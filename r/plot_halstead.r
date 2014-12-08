library(ggplot2)
setwd('G:/diploma_data')

## Plot Halstead metrics of the project
django <- read.csv('django_halstead.csv', sep = '\t')
django$date <- as.Date(django$date, "%Y-%m-%d")

summary(django)
colnames(django)

ggplot(aes(x = date, y = bugs), data = django) +
  geom_line(linetype = 6, color = 'red') +
  geom_point(shape = 3)

## Plot ciclomatic data
#
#1 - 5  A	low - simple block
#6 - 10	B	low - well structured and stable block
#11 - 20	C	moderate - slightly complex block
#21 - 30	D	more than moderate - more complex block
#31 - 40	E	high - complex block, alarming
#41+	F	very high - error-prone, unstable block

## Plotting D, E, F - как потенциально опасные.

django <- read.csv('cc_django.csv', sep = '\t')
django$date <- as.Date(django$date, "%Y-%m-%d")

head(django)

ggplot(aes(x = date), data = django) +
  geom_line(aes(y = E), color = 'gray') +
  geom_point(aes(y = E), shape = 4) +
  geom_line(aes(y = F), color = 'red') +
  geom_point(aes(y = F), shape = 5) +
  geom_line(aes(y = D), color = 'gray') +
  geom_point(aes(y = D), shape = 6) +
  geom_line(aes(y = D+E+F), color = 'black') +
  geom_point(aes(y = D+E+F), shape = 3) +
  xlab("Time") +
  ylab("Errors") +
  ggtitle("Errors in Django repo during time.")

