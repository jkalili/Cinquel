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
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie {movieId: $movieId})
            RETURN m.title
            """,
            movieId=str(movieId),
        )
        return result.single().get('m.title')


def does_id_exist(movieId):
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie {movieId: $movieId})
            RETURN m.title
            """,
            movieId=str(movieId),
        )
        return False if result.single() is None else True


def remove_movie(movieId):
    with db.session() as session:
        result = session.run(
            """
            MATCH (removedMovie:Movie { movieId: $movieId})
            DETACH DELETE removedMovie
            """,
            movieId=str(movieId)
        )


def get_average_rating(movieId):
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
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.runtime = $runtime
            """,
            movieId=str(movieId),
            runtime=int(runtime)
        )


def update_movie_budget(movieId, budget):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.budget = $budget
            """,
            movieId=str(movieId),
            budget=int(budget)
        )


def update_movie_popularity(movieId, popularity):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.popularity = $popularity
            """,
            movieId=str(movieId),
            popularity=int(popularity)
        )


def update_movie_release_date(movieId, releaseDate):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.release_date = $releaseDate
            """,
            movieId=str(movieId),
            releaseDate=date.fromisoformat(releaseDate)
        )


def update_movie_original_language(movieId, originalLanguage):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.original_language = $originalLanguage
            """,
            movieId=str(movieId),
            originalLanguage=str(originalLanguage)
        )


def update_movie_title(movieId, movieTitle):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.title = $movieTitle
            """,
            movieId=str(movieId),
            movieTitle=str(movieTitle)
        )


def update_movie_vote_average(movieId, voteAverage):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.vote_average = $voteAverage
            """,
            movieId=str(movieId),
            voteAverage=float(voteAverage)
        )


def get_actor_performances(castID):
    with db.session() as session:
        result = session.run(
            """
            MATCH (c:Cast {castID:$castID}) - [r:`PERFORMED IN`] -> (m:Movie)
            RETURN m.title,r.role
            ORDER BY m.title
            """,
            castID=str(castID)
        )
        return result.data()


def get_movies_with_keyword(keyword):
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
