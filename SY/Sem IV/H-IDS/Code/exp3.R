dbinom(x = 10, size = 12, prob = 0.6) 
dbinom(x = 7, size = 20, prob = 0.5) 
dbinom(x = 7, size = 100, prob = 0.5) 

pbinom(4, size = 10, prob = 0.3)
pbinom(4, size = 50, prob = 0.3)
pbinom(2, size = 5, prob = 0.5, lower.tail = FALSE)
pbinom(4, size = 5, prob = 0.5, lower.tail = FALSE)

qbinom(0.8479, size = 10, prob = 0.3)
qbinom(0.5, size = 5, prob = 0.5)
qbinom(0.5, size = 100, prob = 0.5)
qbinom(0.1, size = 20, prob = 0.4)
qbinom(0.4, size = 30, prob = 0.25)

result <- rbinom(10, size = 100, prob = 0.3)
print(result)
result <- rbinom(10, size = 500, prob = 0.5)
print(result)

success <- 0:20
plot(success, dbinom(success, size = 20, prob = 0.3),
     type = 'h',
     main = 'Binomial Distribution (n = 20, p = 0.3)',
     ylab = 'Probability',
     xlab = '#Successes',
     lwd = 3)
success <- 0:50
plot(success, dbinom(success, size = 50, prob = 0.4),
       type = 'h',
       main = 'Binomial Distribution (n = 50, p = 0.4)',
       ylab = 'Probability',
       xlab = '#Successes',
       lwd = 3)


dpois(x = 8, lambda = 10)
dpois(x = 5, lambda = 100)

ppois(q = 8, lambda = 10)
ppois(q = 10, lambda = 100)

qpois(p = 0.9, lambda = 10)
qpois(p = 0.5, lambda = 19)

rpois(n = 15, lambda = 10)
rpois(n = 150, lambda = 1000)

lambda <- 6
success <- 0:20
plot(success, dpois(success, lambda),
     type = 'h',
     main = 'Poisson Distribution (lambda = 6)',
     ylab = 'Probability',
     xlab = '#Successes',
     lwd = 3)

dnorm(x = 0, mean = 0, sd = 1)
dnorm(x = 0)
dnorm(x = 10, mean = 20, sd = 5)
dnorm(x = 100, mean = 400, sd = 15)

x <- seq(-4, 4, length = 100)
y <- dnorm(x)
plot(x, y, type = "l", lwd = 2, axes = FALSE, xlab = "", ylab = "")
axis(1, at = -3:3, label = c("-3s", "-2s", "-1s", "mean", "1s", "2s", "3s"))

pnorm(74, mean = 70, sd = 2, lower.tail = FALSE)
pnorm(14, mean = 90, sd = 5, lower.tail = FALSE)
pnorm(22, mean = 30, sd = 5)
pnorm(220, mean = 300, sd = 50)
pnorm(14, mean = 13, sd = 2) - pnorm(10, mean = 13, sd = 2)
pnorm(22, mean = 30, sd = 5) - pnorm(14, mean = 90, sd = 5)

qnorm(0.99, mean = 1, sd = 1)
qnorm(0.99)
qnorm(0.95)
qnorm(0.01)

z <- rnorm(5, mean = 10, sd = 2)
z

narrowDistribution <- rnorm(1000, mean = 50, sd = 15)
wideDistribution <- rnorm(1000, mean = 50, sd = 25)
par(mfrow = c(1, 2))
hist(narrowDistribution, breaks = 50, xlim = c(-50, 150))
hist(wideDistribution, breaks = 50, xlim = c(-50, 150))


