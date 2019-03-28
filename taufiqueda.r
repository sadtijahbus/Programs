library(ggplot2)
library(ade4)
library(factoextra)
library(readr)
dec<- read_csv("/home/vk/taufique1.csv")
data(dec)
head(dec[, 1:6])
dec.active <- dec[2:12, 2:12]
head(dec.active[, 1:6])
dudi.pca(dec.active, center = TRUE,  scale = TRUE,scannf = TRUE, nf = 12)
5
res.pca <- dudi.pca(dec.active, scannf = FALSE, nf = 5)
summary(res.pca)
eig.val <- get_eigenvalue(res.pca)
head(eig.val)
screeplot(res.pca, main ="Screeplot - Eigenvalues")
barplot(eig.val[, 2], names.arg=1:nrow(eig.val), 
        main = "Variances",
        xlab = "Principal Components",
        ylab = "Percentage of variances",
        col ="steelblue")
# Add connected line segments to the plot
lines(x = 1:nrow(eig.val), eig.val[, 2], 
      type="b", pch=19, col = "red")
fviz_screeplot(res.pca, ncp=10)
head(res.pca$co)
s.corcircle(df, label = row.names(df), grid = TRUE,
            box = FALSE)
# Graph of variables
s.corcircle(res.pca$co)
# Default plot
fviz_pca_var(res.pca)
# Change color and theme
fviz_pca_var(res.pca, col.var="steelblue")+
  theme_minimal()
# relative contributions of columns
var.cos2 <- abs(inertia$col.rel/100)
head(var.cos2)
fviz_pca_var(res.pca, col.var="contrib") +
  scale_color_gradient2(low="white", mid="blue",high="red", midpoint=50)
  + theme_minimal()
fviz_pca_var(res.pca, col.var="contrib",col.circle = "blue") + scale_color_gradient2(low="red",mid = "orange", high="blue", midpoint=7.5) 
  + theme_minimal()
fviz_pca_ind(res.pca, col.ind="cos2") +
  scale_color_gradient2(low="white", mid="blue", high="red", midpoint=0.50) 
  + theme_minimal()
fviz_pca_biplot(res.pca$, col.var="contrib",col.circle = "blue",col.ind="cos2") + 
  scale_color_gradient2(low="red",mid = "orange", high="blue", midpoint=6) 
  + theme_minimal()
