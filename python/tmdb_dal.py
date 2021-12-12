import os
from neo4j import GraphDatabase
from datetime import date

# This is for convenience since the `neo4j` user is known to be created by default.
# We do still let an environment variable override it if needed.
db_user = os.environ['DB_USER'] if os.environ.get('DB_USER') else 'neo4j'

# The Neo4j documentation calls this object `driver` but the name `db` is used here
# to provide an analogy across various DAL examples.
db = GraphDatabase.driver(os.environ['DB_URL'], auth=(
    db_user, os.environ['DB_PASSWORD']))


def insert_movie(budget, movieId, original_language, popularity, release_date, runtime, title, vote_average):
    '''
    insert_movie: creates a Movie object in neo4j, given the following parameters:
    parameters: budget(int), movieId(int), original_language(str), popularity(float), release_date(Date), runtime(int), title(str), vote_average(float)
    returns: newly created Movie object
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 add_movie.py 100000 12321 en 10.0 2021-12-14 120 Greatest' 'Movie' 'Ever 10.0
    '''
    with db.session() as session:
        result = session.run(
            """
            CREATE (insertedMovie:Movie { budget: $budget, movieId: $movieId, original_language: $original_language, popularity: $popularity, release_date: $release_date, runtime:$runtime, title: $title, vote_average: $vote_average})
            RETURN insertedMovie
            """,
            budget=int(budget),
            movieId=str(movieId),
            title=str(title),
            release_date=date.fromisoformat(release_date),
            original_language=str(original_language),
            popularity=float(popularity),
            vote_average=float(vote_average),
            runtime=int(runtime)
        )

        # This returns the full node so we have its identity and labels.
        return result.single().get('insertedMovie')


def get_title_by_id(movieId):
    '''
    get_title_by_id: given a movieId, returns the title of the Movie object possessing that id
    parameters: movieId(int)
    returns: title of movieId if found, else None
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_title.py 24
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie {movieId: $movieId})
            RETURN m.title
            """,
            movieId=str(movieId),
        )
        query = result.single()
        return query.get('m.title') if query else None

# USER READABLE SEARCH FUNCTION


def get_id_by_title(title):
    '''
    get_id_by_title: given a title, returns all movie titles containing phrase
    parameters: title(str)
    returns: list of matching Movie objects 
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_id_by_title.py Home
    '''

    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie)
            WHERE toLower(m.title) CONTAINS toLower($title)
            RETURN m
            ORDER BY m.title
            """,
            title=str(title)
        )
        return result.data()


def remove_movie(movieId):
    '''
    remove_movie: given a movieId, removes the matching Movie in our database.
    parameters: movieId(int)
    returns: None; argument validation check handled by does_id_exist
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 remove_movie.py 24492
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH (removedMovie:Movie { movieId: $movieId})
            DETACH DELETE removedMovie
            """,
            movieId=str(movieId)
        )


def get_average_rating(movieId):
    '''
    get_average_rating: Given a movieId, returns the average rating of that movie
    parameters: movieId(int)
    returns: average rating of the matching Movie
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_rating.py 24492
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie {movieId: $movieId})
            RETURN m.vote_average
            """,
            movieId=str(movieId),
        )
        query = result.single()
        return query.get('m.vote_average') if query else None


def update_movie_runtime(movieId, runtime):
    '''
    update_movie_runtime: updates runtime for Movie object matching movieId
    parameters: movieId(int), runtime(int)
    returns: modified matching MovieId object
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_runtime.py 24492 1234
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.runtime = $runtime
            RETURN m
            """,
            movieId=str(movieId),
            runtime=int(runtime)
        )
        return result.single()


def update_movie_budget(movieId, budget):
    '''
    update_movie_budget: updates the budget field of a given movieId
    parameters: movieId(int), budget(int)
    returns: updated Movie object
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_budget.py 24492, 165000000
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.budget = $budget
            RETURN m
            """,
            movieId=str(movieId),
            budget=int(budget)
        )
        return result.single()


def update_movie_popularity(movieId, popularity):
    '''
    update_movie_popularity: updates the popularity field of a Movie object matching movieId
    parameters: movieId(int), popularity(int)
    returns: updated Movie object
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_popularity.py 24492, 165000000
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.popularity = $popularity
            RETURN m
            """,
            movieId=str(movieId),
            popularity=int(popularity)
        )
        return result.single()


def update_movie_release_date(movieId, releaseDate):
    '''
    update_movie_release_date: updates the release date field of a given movieId
    parameters: movieId(int), releaseDate(str)
    returns: updated Movie object
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_release_date.py 24492 2019-08-12
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.release_date = $release_date
            RETURN m
            """,
            movieId=str(movieId),
            release_date=date.fromisoformat(release_date)
        )
        return result.single()


def update_movie_original_language(movieId, original_language):
    '''
    update_movie_original_language: updates the originalLanguage field of a given movieId
    parameters: movieId(int), releaseDate(str)
    returns: updated release date
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_release_date.py 24492 2019-08-12
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.original_language = $original_language
            RETURN m
            """,
            movieId=str(movieId),
            originalLanguage=str(original_language)
        )
        return result.single()


def update_movie_title(movieId, movie_title):
    '''
    update_movie_title: updates the movie title field of a given movieId
    parameters: movieId(int), movie_title(str)
    returns: updated Movie object
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_title.py 24492 Star-Wars: Episode 4 
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.title = $movie_title
            RETURN m
            """,
            movieId=str(movieId),
            movieTitle=str(movie_title)
        )
        return result.single()


def update_movie_vote_average(movieId, vote_average):
    '''
    update_movie_vote_average: updates the vote_average field of a given movieId
    parameters: movieId(int), voteAverage(str)
    returns: updated release date
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 update_movie_release_date.py 24492 2019-08-12
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.vote_average = $vote_average
            RETURN m
            """,
            movieId=str(movieId),
            voteAverage=float(vote_average)
        )
        return result.single()


def get_actor_performances(castId):
    '''
    get_actor_performances: returns the movies a given actor has performed in
    parameters: castId(str)
    returns: list of movies the castId has performed in
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_actor_performances.py Daniel' 'Craig
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH (c:Cast) - [r:`PERFORMED IN`] -> (m:Movie)
            WHERE toLower(c.castID) = toLower($castId)
            RETURN m.title,r.role
            ORDER BY m.title
            """,
            castId=str(castId)
        )
        return result.data()


def get_movies_with_keyword(keyword):
    '''
    get_movies_with_keyword: given a keyword, returns all movies matching keyword
    parameters: keyword(str)
    returns: dictionary of matching movies
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_movies_with_keyword.py adventure
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie) - [r:HAS_KEYWORD] -> (k:Keywords)
            WHERE k.keywordID = $keyword
            RETURN m.title
            """,
            keyword=str(keyword)
        )
        return result.data()


def acted_together(first_cast_id, second_cast_id):
    '''
    acted_together: shows what movies two actors worked together in, if any.
    parameters: first_cast_id(int), second_cast_id(int)
    returns: List of Movies where first_cast_id and second_cast_id both performed in
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 acted_together.py Daniel' 'Craig Judi' 'Dench
    '''
    with db.session() as session:
        result = session.run(
            '''
            MATCH (c:Cast) - [r:`PERFORMED IN`] -> (m:Movie) <- [r2:`PERFORMED IN`] - (c2:Cast)
            WHERE toLower(c.castID) = toLower($first_cast_id) AND toLower(c2.castID) = toLower($second_cast_id)
            RETURN c,c2,m,r,r2
            ''',
            first_cast_id=str(first_cast_id),
            second_cast_id=str(second_cast_id)
        )
        return result.data()


# Complex Queries
def get_movies_and_actors_with_role(role):
    '''
    get_movies_and_actors_with_keyword: returns all actors who have played a given role in any movie
    parameters: role(str)
    returns: Movie.title and 'PERFORMED IN'.role
    example query: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_movies_and_actors_with_role.py James' 'Bond
    '''
    with db.session() as session:
        result = session.run(
            '''
            MATCH (c:Cast) - [r:`PERFORMED IN`] -> (m:Movie)
            WHERE toLower(r.role) = toLower($role)
            RETURN c,r,m
            ORDER BY m.release_date DESC
            ''',
            role=str(role)
        )
        return result.data()


def get_movies_and_directors_with_keyword(keyword):
    '''
    get_movies_and_directors_with_keyword: returns the title and director of movies with a given keyword.
    parameters: keyword(str)
    returns: Movie.title and Crew.job (where the job is director)
    example query: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 get_movies_and_directors_with_keyword.py love
    '''
    with db.session() as session:
        result = session.run(
            '''
            MATCH (c:Crew) - [r:`WORKED ON` {job:"Director"}] -> (m:Movie)
            MATCH (m) - [r2:HAS_KEYWORD] -> (k:Keywords {keywordID:$keyword})
            RETURN r2,k,m,r,c
            ORDER BY m.popularity
            ''',
            keyword=str(keyword)
        )
        return result.data()

# TRANSACTION


def link_actor_with_two_movies(actor, movies_and_roles):
    '''
    link_actor_with_two_movies: given an actor, creates relationships with attribute roles linking to specified movies
    parameters: actor(str), movies_and_roles(list of tuples, where first index is movie, second index role)
    returns: relationships created, None if failed.
    example: DB_URL=neo4j://localhost DB_PASSWORD=4949 python3 link_actor_with_two_movies.py Daniel' 'Craig 24 Dancer 18360 The' 'Car

    '''
    with db.session() as session:
        result = session.run(
            '''
            MATCH (c:Cast) 
            MATCH (first_movie:Movie {movieId: $movie})
            MATCH (second_movie:Movie {movieId: $second_movie})
            WHERE toLower(c.castID) = toLower($actor)
            CREATE (c) - [first_role:`PERFORMED IN` {role:$role}] -> (first_movie)
            CREATE (c) - [second_role:`PERFORMED IN` {role:$second_role}] -> (second_movie)
            RETURN c,first_role,first_movie,second_role,second_movie
            ''',
            actor=str(actor),
            movie=str(movies_and_roles[0][0]),
            role=str(movies_and_roles[0][1]),
            second_movie=str(movies_and_roles[1][0]),
            second_role=str(movies_and_roles[1][1])
        )
        return result.single()

#
# HELPERS
#


def does_id_exist(movieId):
    '''
    does_id_exist: given a movieId, returns if the movie exists in the database or not.
    parameters: movieId(int)
    returns: boolean value of the MovieIDs status in our database
    '''
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie {movieId: $movieId})
            RETURN m
            """,
            movieId=str(movieId),
        )
        return True if result.single() else False
