---
title: Regression Project - Where to Find Data
---

About 100 places to find a dataset for your regression project, grouped by topic. Pick something you actually care about, since you'll be looking at it for a while. Pick a dataset with at least 10 numerical columns and make a prediction before you run the analysis.


## Built for learning

These datasets are curated and cleaned, so you can spend your time on the question instead of on parsing. They're good alternatives to Kaggle.

| Source | What's there |
| --- | --- |
| [UCI ML Repository](https://archive.ics.uci.edu) | Hundreds of classic tabular sets with documentation |
| [OpenML](https://www.openml.org) | Thousands of benchmark sets, each with a stats summary page |
| [Hugging Face Datasets](https://huggingface.co/datasets) | Many Kaggle sets are mirrored here; load them with one line in Colab |
| [Rdatasets](https://vincentarelbundock.github.io/Rdatasets/) | About 1,500 sets from R packages, as plain CSV |
| [seaborn-data](https://github.com/mwaskom/seaborn-data) | Tips, diamonds, penguins, mpg, flights, and more |
| [OpenIntro data](https://www.openintro.org/data/) | Textbook datasets about real events and studies |
| [Journal of Statistics Education archive](https://jse.amstat.org/jse_data_archive.htm) | Classroom datasets with the story behind each |
| [DASL](https://dasl.datadescription.com) | Data and Story Library: small sets with context |
| [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) | Bill, flipper, and mass measurements for three species |
| [Gapminder](https://www.gapminder.org/data/) | Country-level life expectancy, income, fertility |
| [vega\_datasets](https://github.com/vega/vega-datasets) | Cars, movies, stocks, Seattle weather |
| [data.world](https://data.world) | Community-uploaded sets of mixed quality, so check the source |
| [Google Dataset Search](https://datasetsearch.research.google.com) | Search engine across thousands of repositories |
| [Kaggle](https://www.kaggle.com/datasets) | Largest collection, often blocked at school; fetch with `kagglehub` from Colab, or browse at home |

## Where to browse for ideas

These sites are better for finding a question than for downloading data, and most of them work at school.

| Source | Why it helps |
| --- | --- |
| [TidyTuesday](https://github.com/rfordatascience/tidytuesday) | A new clean dataset every week since 2018; the archive is a topic menu on GitHub |
| [FiveThirtyEight data](https://github.com/fivethirtyeight/data) | Data behind journalism stories, each folder with a README and the original article |
| [The Pudding data](https://github.com/the-pudding/data) | Quirky datasets (music, film, culture) behind visual essays |
| [Data is Plural](https://www.data-is-plural.com) | Weekly newsletter with an archive spreadsheet of thousands of oddball datasets |
| [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) | A giant categorized list on GitHub, sorted by field |
| [Our World in Data](https://ourworldindata.org) | Every chart has a download button for its CSV; browse charts, then grab the data |
| [r/datasets](https://www.reddit.com/r/datasets) | Requests and shares; probably blocked at school, but worth a try |

## Sports

You already know the context for sports data, and outcomes like wins, salary, and points are numeric, which makes them a good fit for regression.

| Source | What's there |
| --- | --- |
| [Sports Reference](https://www.sports-reference.com) | Basketball, football, baseball, hockey, college; most tables export to CSV |
| [nba\_api](https://github.com/swar/nba_api) | Python wrapper for NBA.com stats |
| [pybaseball](https://github.com/jldbc/pybaseball) | Python access to Statcast, FanGraphs, and Baseball Reference |
| [Lahman Database](https://sabr.org/lahman-database/) | Complete baseball history back to 1871, as CSV |
| [Baseball Savant](https://baseballsavant.mlb.com) | Pitch-level Statcast data with CSV download |
| [Retrosheet](https://www.retrosheet.org) | Play-by-play for most MLB games |
| [nflverse data](https://github.com/nflverse/nflverse-data) | Play-by-play and player stats for the NFL |
| [FBref](https://fbref.com) | Soccer stats across major leagues |
| [football-data.co.uk](https://www.football-data.co.uk) | Match results and betting odds as CSV |
| [Jolpica F1 API](https://github.com/jolpica/jolpica-f1) | Formula 1 results since 1950 (Ergast replacement) |
| [MoneyPuck](https://moneypuck.com/data.htm) | NHL shot-level and team data as CSV |
| [Cricsheet](https://cricsheet.org) | Ball-by-ball cricket data |
| [Lichess database](https://database.lichess.org) | Millions of chess games, monthly dumps |

## Music, movies, games, and web culture

These are popular topics. Spotify restricted its audio-features API for new apps in late 2024, so use a downloaded dataset for those columns instead.

| Source | What's there |
| --- | --- |
| [IMDb datasets](https://datasets.imdbws.com) | Official bulk files: titles, ratings, crew, votes |
| [MovieLens](https://grouplens.org/datasets/movielens/) | Millions of user ratings with movie metadata |
| [TMDB API](https://developer.themoviedb.org) | Budget, revenue, popularity (free key) |
| [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_Database) | Open music metadata database |
| [Last.fm API](https://www.last.fm/api) | Listening counts and tags (free key) |
| Spotify audio features | Danceability, energy, tempo, popularity in downloadable sets (check Hugging Face or Kaggle mirrors) |
| Spotify extended streaming history | Request your own listening log from your account privacy page |
| [SteamSpy API](https://steamspy.com/api.php) | Owners, price, and playtime for Steam games |
| [PokeAPI](https://pokeapi.co) | Every Pokémon's stats, types, and moves |
| [BoardGameGeek API](https://boardgamegeek.com/wiki/page/BGG_XML_API2) | Ratings, complexity, and play time for board games |
| [Jikan (MyAnimeList)](https://jikan.moe) | Anime scores, episodes, and popularity |
| [Wikipedia pageviews](https://pageviews.wmcloud.org) | Daily views for any article |
| [Google Trends](https://trends.google.com) | Search interest over time, CSV export |

## Government, civic, and economics

The Virginia and Loudoun rows give you a local connection, and College Scorecard is useful if you're thinking about college.

| Source | What's there |
| --- | --- |
| [College Scorecard](https://collegescorecard.ed.gov/data/) | Cost, admission rate, graduation rate, and earnings for every US college |
| [Virginia School Quality Profiles](https://schoolquality.virginia.gov) | Pass rates, demographics, and attendance for each school |
| [Virginia Open Data Portal](https://data.virginia.gov) | State agency datasets |
| [Loudoun County GIS Data Hub](https://geohub-loudoungis.opendata.arcgis.com) | Local county data |
| [Data.gov](https://data.gov) | Federal catalog with roughly 300,000 datasets; search with the CSV filter on |
| [Census](https://data.census.gov) | Income, housing, commute time, and education by area |
| [FRED](https://fred.stlouisfed.org) | Hundreds of thousands of economic time series, with CSV download |
| [BLS](https://www.bls.gov/data/) | Wages, prices, and employment |
| [World Bank Open Data](https://data.worldbank.org) | Country-level development indicators |
| [BTS TranStats](https://www.transtats.bts.gov) | Flight delays and airline data |
| [NHTSA FARS](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) | Fatal crash records |
| [EIA](https://www.eia.gov/opendata/) | Gas prices, electricity, and energy use |
| [Zillow Research](https://www.zillow.com/research/data/) | Home values and rents by area |
| [Redfin Data Center](https://www.redfin.com/news/data-center/) | Housing market metrics |
| [Inside Airbnb](http://insideairbnb.com/get-the-data/) | Listings, prices, and reviews by city |
| [CDC NHANES](https://www.cdc.gov/nchs/nhanes) | Body measurements and health survey data; check with your teacher before choosing a health topic |
| [County Health Rankings](https://www.countyhealthrankings.org/health-data) | County-level health factors; check with your teacher before choosing a health topic |
| [General Social Survey](https://gss.norc.org) | Decades of US attitudes and demographics; mostly categorical, so regression is a stretch |
| [NYC Open Data](https://www.nyc.gov/opendata) and [Chicago Data Portal](https://data.cityofchicago.org) | Big-city datasets on taxis, 311 calls, and crime |

## Science, weather, and environment

Clean physical measurements make good first regressions because the relationships are real and the noise is modest.

| Source | What's there |
| --- | --- |
| [Open-Meteo](https://open-meteo.com) | Free historical weather API, no key needed |
| [Meteostat](https://meteostat.net) | Historical station data in Python |
| [NOAA NCEI](https://www.ncei.noaa.gov/access) | Climate records for any US station |
| [NOAA Mauna Loa CO2](https://gml.noaa.gov/ccgg/trends/data.html) | Monthly CO2 since 1958 |
| [NASA GISS temperature](https://data.giss.nasa.gov/gistemp/) | Global temperature anomalies since 1880 |
| [USGS earthquake feeds](https://earthquake.usgs.gov/earthquakes/feed/v1.0/) | Recent quakes as CSV |
| [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu) | Thousands of confirmed exoplanets |
| [NASA APIs](https://api.nasa.gov) | Asteroids, Mars weather, and more (free key) |
| [EPA air quality data](https://aqs.epa.gov/aqsweb/airdata/download_files.html) | Daily air quality readings by monitor |
| [GBIF](https://www.gbif.org) | Biodiversity records worldwide |
| [eBird](https://science.ebird.org/use-ebird-data) | Bird sightings (requires an access request) |
| [Global Forest Watch](https://globalnaturewatch.org) | Tree cover loss by region |


## Free APIs if you code

These suit you if you're ready to write a few lines of Python to pull your own data. Most need a free key. All of them run fine from Colab even when the site itself is blocked in your browser.

| Source | What's there |
| --- | --- |
| [yfinance](https://github.com/ranaroussi/yfinance) | Stock prices and fundamentals |
| [CoinGecko API](https://www.coingecko.com/en/api) | Crypto prices and volumes |
| [Alpha Vantage](https://www.alphavantage.co) | Stock and forex time series (free key) |
| [USDA FoodData Central](https://fdc.nal.usda.gov) | Nutrition facts for thousands of foods |
| [Open Food Facts](https://world.openfoodfacts.org/data) | Packaged-food nutrition and ingredients |
| [Open Library](https://openlibrary.org/developers/api) | Book metadata |
| [Public APIs list](https://github.com/public-apis/public-apis) | A big directory of free APIs by category |
