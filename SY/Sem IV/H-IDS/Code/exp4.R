rm(list = ls())

data()

my_data <- pressure
head(my_data, 9)
tail(my_data, 9)
mean(my_data$temperature)
median(my_data$temperature)

install.packages("modeest")
require(modeest)
mfv(my_data$temperature)
min(my_data$temperature)
max(my_data$temperature)
range(my_data$temperature)

quantile(my_data$temperature)
quantile(my_data$temperature, seq(0, 1, 0.25))
quantile(my_data$temperature, seq(0, 1, 0.1))
IQR(my_data$temperature)

var(my_data$temperature)
sd(my_data$temperature)
mad(my_data$temperature)

summary(my_data$temperature)
summary(my_data, digits = 2)

sapply(my_data[, -5], mean)
sapply(my_data[, -5], quantile)

install.packages("ggpubr")
library(ggpubr)

ggboxplot(my_data, y = "temperature", width = 0.5)
gghistogram(my_data, x = "temperature", bins = 9, add = "mean")
ggecdf(my_data, x = "temperature")
ggqqplot(my_data, x = "temperature")

install.packages("dplyr")
library(dplyr)

group_by(my_data, temperature) %>%
  summarise(
    count = n(),
    mean = mean(temperature, na.rm = TRUE),
    sd = sd(temperature, na.rm = TRUE)
  )

ggboxplot(my_data, x = "temperature", y = "pressure",
          color = "temperature",
          palatte = c("#2E8B57", "#FFC300", "#3399FF"))

ggstripchart(my_data, x = "temperature", y = "pressure",
          color = "temperature",
          palatte = c("#2E8B57", "#FFC300", "#3399FF"),
          add = "mean_sd")

df <- as.data.frame(HairEyeColor)
hair_eye <- df[rep(row.names(df), df$Freq), 1:4]
rownames(hair_eye) <- 1:nrow(hair_eye)
head(hair_eye)

Hair <- hair_eye$Hair
Eye <- hair_eye$Eye
table(Hair)
table(Eye)

library(ggpubr)
ggbarplot(df, x = "Hair", y = "Freq")

he <- table(Hair, Eye)
he

xtabs(~Hair + Eye + Sex, data = hair_eye)
ftable(Sex + Hair ~ Eye, data = hair_eye)

margin.table(he, 1)
margin.table(he, 2)

prop.table(he, 1)
round(prop.table(he, 1), 2) * 100
round(prop.table(he, 1), 4) * 100