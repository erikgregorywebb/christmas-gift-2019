library(tidyverse)

# import
url = 'https://raw.githubusercontent.com/erikgregorywebb/christmas-gift-2019/master/christopher-spotify.csv'
spot = read_csv(url)

# clean
spot = spot %>%
  select(-X1) %>%
  rename(playlist = `0`, artist = `1`, song = `2`)

# number of songs by playlist
spot %>% group_by(playlist) %>% count(sort = T)

# top songs
spot %>% group_by(song, artist) %>% count(sort = T)

# top artists
spot %>% group_by(artist) %>% count(sort = T)

# list: Mariah Carey, Taylor Swift, Lana Del Rey, Ariana Grande, Charli XCX