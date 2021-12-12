# Command Line Suite for DAL

_Assumes user is in the python environment. See setup.md_

## Usage:

` DB_URL=neo4j://localhost DB_PASSWORD=<your password> python3 <function>.py [args]`

## Example:

`DB_URL=neo4j://localhost DB_PASSWORD=<your password> python3 insert_move.py Titanic`

## Formatting for args:

- For space(s) in a single arg, wrap in single quotes
  - i.e. `... remove_movie.py Saving' 'Private' 'Ryan`
- For multiple args, seperate with space(s)
  - i.e. `... update_movie_vote_average.py Saving' 'Private' 'Ryan 8.9`

## Available Functions:

### Insert/Create a Movie

#### Creation function

`... insert_movie.py [budget] [movieId] [original_language] [popularity] [release_date] [runtime] [title] [vote_average]`

<br>

### Query id by movie title

#### User readable search function

` ... get_id_by_title.py [title]`

<br>

### Query movie title by id

#### Get-one-entity-by-ID function

`... get_title_by_id.py [movieId]`

<br>

### Remove Movie by id

#### Delete function

`... remove_movie.py [movieId]`

<br>

### Query average rating by id

`... get_average_rating.py [movieId]`

<br>

### Update movie runtime by id

#### Update function

`... update_movie_runtime.py [movieId] [runtime]`

<br>

### Update movie budget by id

#### Update function

`... update_movie_budget.py [movieId] [budget]`

<br>

### Update movie popularity by id

#### Update function

`... update_movie_popularity.py [movieId] [popularity]`

<br>

### Update movie release date by id

#### Update function

`... update_movie_release_date.py [movieId] [releaseDate]`

<br>

### Update movie original lanaguage by id

#### Update function

`... update_movie_original_language.py [movieId] [originalLanguage]`

<br>

### Update movie title by id

#### Update function

`... update_movie_title.py [movieId] [movieTitle]`

<br>

### Update movie vote average by id

#### Update function

`... update_movie_vote_average.py [movieId] [voteAverage]`

<br>

### Lists all movies based on performer cast id

`... get_actor_performances.py [castID]`

<br>

### Lists all movies based on keyword

`... get_movies_with_keyword.py [keyword]`

<br>

### Lists all movies where both cast id acted together

`... acted_together.py [castID] [castID]`

<br>

### Lists all actors and movies given a role

#### Complex Query

`... get_movies_and_actors_with_role.py [role]`

<br>

### Lists all movies and directors given a keyword

#### Complex Query

`... get_movies_and_directors_with_keyword.py [keyword]`

<br>

### Lists an actors role and attributed in specified movies

#### Transaction

`... link_actor_with_two_movies.py [castID] [first_movieId] [first_role] [second_movieId] [second_role]`
