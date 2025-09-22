# Minimal Working Example: Data Cleaning in R

data <- data.frame(
  A = c(1, 2, NA, 4),
  B = c('x', NA, 'y', 'z')
)

# Drop rows with missing values
data_clean <- na.omit(data)
print(data_clean)
