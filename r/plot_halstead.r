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
  geom_line(aes(y = E, label='E'), color = 'gray', size=0.8) +
  geom_point(aes(y = E), shape = 4) +
  geom_line(aes(y = F), color = 'red', size=0.8) +
  geom_point(aes(y = F), shape = 5) +
  geom_line(aes(y = D, color='D'), color = 'gray', size = 0.8) +
  geom_point(aes(y = D), shape = 6) +
  geom_line(aes(y = D+E+F), color = 'black', size = 0.8) +
  geom_point(aes(y = D+E+F), shape = 3) +
  xlab("Дата") +
  ylab("Количество файлов") +
  ggtitle("Цикломатическая сложность в Django.") +
  theme_bw() +
  theme(legend.text=element_text(size=16)) +
  theme(axis.text=element_text(size=16),
        axis.title=element_text(size=16))

### Hole dataset cc
d <- read.csv('hole_cc.csv', sep = '\t')
head(d)
d$date <- as.Date(d$date, "%Y-%m-%d")

ggplot(aes(x = date, y = D + E + F), data = d) +
  geom_line(aes(color = proj_name), size = 0.8) +
  xlab("Дата") +
  ylab("Количество файлов") +
  ggtitle("Количество методов с высокой цикломатической сложностью") +
  theme_bw() +
  theme(legend.text=element_text(size=16)) +
  theme(axis.text=element_text(size=16),
        axis.title=element_text(size=16))
#geom_point(aes(color = proj_name, shape = proj_name)) +

### Hole dataset halst
d <- read.csv('hole_halstead.csv', sep = '\t')
d$date <- as.Date(d$date, "%Y-%m-%d")

ggplot(aes(x = date, y = bugs), data = d) +
  geom_line(aes(color = proj_name), size = 0.8) + 
  xlab("Дата") +
  ylab("Ошибки") +
  ggtitle("Количество ошибок по метрике Халстеда") +
  theme_bw() +
  theme(legend.text=element_text(size=16)) +
  theme(axis.text=element_text(size=16),
        axis.title=element_text(size=16))
  

########### Dinamic models
d <- read.csv('dynamic_models.csv', sep = '\t')
head(d)
ggplot(aes(x = tau), data = d) +
  geom_line(aes(y = real_error), color = 'black') +
  geom_line(aes(y = musa),  color = 'red') +
  geom_line(aes(y = musa_okumoto), , color = 'green') +
  geom_line(aes(y = jm), color = 'blue')

cor(d$real_falls, d$mttf)

d <- read.csv('jm_model.csv', sep = '\t')
head(d)
ggplot(aes(x = i), data = d) +
  geom_point(aes(y = real_falls), color = 'black', shape = 4) +
  geom_line(aes(y = mttf), color = 'red', linetype = 2) +
  xlab("Отказы") +
  ylab("Время до отказа") +
  theme_bw()


# Plot multiple JM
require(gridExtra)
d <- read.csv('jm_6.csv', sep = '\t')
p1 <- ggplot(aes(x = i), data = d) +
  geom_point(aes(y = real_falls), color = 'black', shape = 4) +
  geom_line(aes(y = mttf), color = 'red', linetype = 2) +
  xlab("Отказы") +
  ylab("Время до отказа") +
  theme_bw()

d <- read.csv('jm_journal_of_ca.csv', sep = '\t')
p2 <- ggplot(aes(x = i), data = d) +
  geom_point(aes(y = real_falls), color = 'black', shape = 4) +
  geom_line(aes(y = mttf), color = 'red', linetype = 2) +
  xlab("Отказы") +
  ylab("Время до отказа") +
  theme_bw()

d <- read.csv('jm_40.csv', sep = '\t')
p3 <- ggplot(aes(x = i), data = d) +
  geom_point(aes(y = real_falls), color = 'black', shape = 4) +
  geom_line(aes(y = mttf), color = 'red', linetype = 2) +
  xlab("Отказы") +
  ylab("Время до отказа") +
  theme_bw()


grid.arrange(p1, p2, p3, ncol=1)
