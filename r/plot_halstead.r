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
  xlab("Дата") +
  ylab("Количество файлов") +
  ggtitle("Цикломатическая сложность в Django.") +
  theme_bw()

### Hole dataset cc
d <- read.csv('hole_cc.csv', sep = '\t')
head(d)
d$date <- as.Date(d$date, "%Y-%m-%d")

ggplot(aes(x = date, y = D + E + F), data = d) +
  geom_line(aes(color = proj_name, linetype = proj_name), size = 1) +
  geom_point(aes(color = proj_name, shape = proj_name)) +
  xlab("Дата") +
  ylab("Количество файлов") +
  ggtitle("Количество методов с высокой цикломатической сложностью") +
  theme_bw()

### Hole dataset halst
d <- read.csv('hole_halstead.csv', sep = '\t')
d$date <- as.Date(d$date, "%Y-%m-%d")

ggplot(aes(x = date, y = bugs), data = d) +
  geom_line(aes(color = proj_name, linetype = proj_name), size = 0.8) +
  geom_point(aes(color = proj_name, shape = proj_name)) +
  xlab("Дата") +
  ylab("Ошибки") +
  ggtitle("Количество ошибок по метрике Холстеда") +
  theme_bw()
  



########### Dinamic models
d <- read.csv('dynamic_models.csv', sep = '\t')
head(d)
ggplot(aes(x = tau), data = d) +
  geom_line(aes(y = real_error), color = 'black') +
  geom_line(aes(y = musa),  color = 'red') +
  geom_line(aes(y = musa_okumoto), , color = 'green') +
  geom_line(aes(y = jm), color = 'blue')


d <- read.csv('jm_model.csv', sep = '\t')
head(d)
ggplot(aes(x = i), data = d) +
  geom_line(aes(y = real_falls, color = ), color = 'black') +
  geom_line(aes(y = mttf), color = 'red', linetype = 2) +
  xlab("Отказы") +
  ylab("Время до отказа") +
  theme_bw() +
  scale_shape_discrete(name  ="Payer",
                       breaks=c("Female", "Male"),
                       labels=c("Woman", "Man"))

