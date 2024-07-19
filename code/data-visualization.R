library(readr)
library(dplyr)
library(ggplot2)

file_path <- "data/directory-homeless-population-by-year.csv"
data <- read_csv(file_path)

total_homeless_per_year <- data %>%
  group_by(Year) %>%
  summarize(Total_Homeless = sum(`Homeless Estimates`))

# This function plots the total homeless population over the years
ggplot(total_homeless_per_year, aes(x = Year, y = Total_Homeless)) +
  geom_line(color = "green", size = 1) +
  geom_point(color = "green", size = 2) +
  labs(title = "Total Homeless Population Over Four Years", x = "Year",
       y = "Total Homeless Estimates") +
  theme_minimal()

ggplot(data, aes(x = Year, y = `Homeless Estimates`, color = Area)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  labs(title = "Homeless Population Estimation by Area Over Four Years", 
    x = "Year",
       y = "Homeless Estimates") +
  theme_grey() +
  theme(legend.position = "bottom") +
  scale_color_brewer(palette = "Set1")

print(data, n = 32)