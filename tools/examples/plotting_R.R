# Minimal Working Example: Plotting in R

data <- data.frame(x = c(1, 2, 3), y = c(2, 4, 1))

plot(data$x, data$y, type = 'b', xlab = 'x', ylab = 'y', main = 'Simple Plot')
