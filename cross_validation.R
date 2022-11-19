set.seed(1996, sample.kind="Rounding")
n <- 1000
p <- 10000
x <- matrix(rnorm(n*p), n, p)
colnames(x) <- paste("x", 1:ncol(x), sep = "_")
library(purrr)
y <- rbinom(n, 1, 0.5) %>% factor()

x_subset <- x[ ,sample(p, 100)]
library(caret)
fit <- train(x_subset, y, method = "glm")
fit$results
install.packages("BiocManager")
BiocManager::install("genefilter")
library(genefilter)
tt <- colttests(x, y)
pvals <- tt$p.value
#
mat <- matrix(c(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6), ncol=4, nrow=4)
colnames(mat) <- c("C1","C2","C3","C4")
rownames(mat) <- c("R1", "R2","R3","R4")
which(mat==5, arr.ind = TRUE)
#
ind <- sum(pvals<0.01)
ind
ind_names <- rownames(tt[tt[,"p.value"]<0.01,])
x_subset <- x[,ind_names]
fit <- train(x_subset, y, method = "glm")
fit$results

fit <- train(x_subset, y, method = "knn", tuneGrid = data.frame(k = seq(101, 301, 25)))
ggplot(fit)
library(dslabs)
data("tissue_gene_expression")
fit <- train(tissue_gene_expression$x, tissue_gene_expression$y, method = "knn", tuneGrid = data.frame(k = seq(1, 7, 2)))
fit$results$k[which.max(fit$results$Accuracy)]

#bootstrap
set.seed(1995)
n <- 10^6
income <- 10^(rnorm(n, log10(45000), log10(3)))
qplot(log10(income), bins = 30, color = I("black"))
m <- median(income)
m
#44938.54
N <- 100
X <- sample(income, N)
median(X)
#> [1] 47432.95

library(gridExtra)
B <- 10^4
M <- replicate(B, {
  X <- sample(income, N)
  median(X)
})
p1 <- qplot(M, bins = 30, color = I("black"))
p2 <- qplot(sample = scale(M), xlab = "theoretical", ylab = "sample") + 
  geom_abline()
grid.arrange(p1, p2, ncol = 2)
median(X) + 1.96 * sd(X) / sqrt(N) * c(-1, 1)
#> [1] 4773.012 90092.885
quantile(M, c(0.025, 0.975))
#    2.5%    97.5% 
#34555.74 58599.42

B <- 10^4
M_star <- replicate(B, {
  X_star <- sample(X, N, replace = TRUE)
  median(X_star)
})
quantile(M_star, c(0.025, 0.975))
#    2.5%    97.5% 
# 30084.63 68565.84
#codehm{
n <- 10^6
income <- 10^(rnorm(n, log10(45000), log10(3)))
qplot(log10(income), bins = 30, color = I("black"))

m <- median(income)
m

set.seed(1995)
#use set.seed(1995, sample.kind="Rounding") instead if using R 3.6 or later
N <- 250
X <- sample(income, N)
M<- median(X)
M
library(gridExtra)
B <- 10^4
M <- replicate(B, {
  X <- sample(income, N)
  median(X)
})
p1 <- qplot(M, bins = 30, color = I("black"))
p2 <- qplot(sample = scale(M)) + geom_abline()
grid.arrange(p1, p2, ncol = 2)
mean(M)
sd(M)
B <- 10^4
M_star <- replicate(B, {
  X_star <- sample(X, N, replace = TRUE)
  median(X_star)
})

tibble(monte_carlo = sort(M), bootstrap = sort(M_star)) %>%
  qplot(monte_carlo, bootstrap, data = .) + 
  geom_abline()

quantile(M, c(0.05, 0.95))
quantile(M_star, c(0.05, 0.95))

median(X) + 1.96 * sd(X) / sqrt(N) * c(-1, 1)

mean(M) + 1.96 * sd(M) * c(-1,1)

mean(M_star) + 1.96 * sd(M_star) * c(-1, 1)
#}
#quiz
library(dslabs)
library(caret)
data(mnist_27)
set.seed(1995,sample.kind="Rounding")
indexes <- createResample(mnist_27$train$y, 10)
three_times = table(indexes$Resample01==3)
three_times = three_times + table(indexes$Resample05==3)
#11
y <- rnorm(100, 0, 1)
qnorm(0.75)
quantile(y, 0.75)

set.seed(1)
B <- 10^3
M_s <- replicate(B, {
  X_s <- rnorm(100, 0, 1)
  quantile(X_s, 0.75)
})
mean(M_s) #expected value
sd(M_s)

set.seed(1)
y <- rnorm(100, 0, 1)
set.seed(1)
indexes <- createResample(y, 10000)
for (i in c(1:10000)) {
  x[i] = quantile(y[indexes[[i]]], 0.75)
}
mean(x)
sd(x)
