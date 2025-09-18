library(readr)
library(dplyr)

df <- read_csv("data/example.csv", show_col_types = FALSE)
summary <- df %>% summarize(mean_value = mean(value, na.rm = TRUE), n = n())
write_csv(summary, "summary_r.csv")
cat("Wrote summary_r.csv\n")
