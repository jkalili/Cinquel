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
        query = result.single()
        return query.get('m.title') if query else None


def does_id_exist(movieId):
    with db.session() as session:
        result = session.run(
            """
            MATCH (m:Movie {movieId: $movieId})
            RETURN m
            """,
            movieId=str(movieId),
        )
        return True if result.single() else False


def remove_movie(movieId):
    with db.session() as seson:
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
            RETURN m
            """,
            movieId=str(movieId),
            runtime=int(runtime)
        )
        return result.single()


def update_movie_budget(movieId, budget):
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
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.release_date = $releaseDate
            RETURN m
            """,
            movieId=str(movieId),
            releaseDate=date.fromisoformat(releaseDate)
        )
        return result.single()


def update_movie_original_language(movieId, originalLanguage):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.original_language = $originalLanguage
            RETURN m
            """,
            movieId=str(movieId),
            originalLanguage=str(originalLanguage)
        )
        return result.single()


def update_movie_title(movieId, movieTitle):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.title = $movieTitle
            RETURN m
            """,
            movieId=str(movieId),
            movieTitle=str(movieTitle)
        )
        return result.single()


def update_movie_vote_average(movieId, voteAverage):
    with db.session() as session:
        result = session.run(
            """
            MATCH(m:Movie {movieId: $movieId})
            SET m.vote_average = $voteAverage
            RETURN m
            """,
            movieId=str(movieId),
            voteAverage=float(voteAverage)
        )
        return result.single()


def get_actor_performances(castID):
    with db.session() as session:
        result = session.run(
            """
            MATCH (c:Cast) - [r:`PERFORMED IN`] -> (m:Movie)
            WHERE toLower(c.castID) = toLower($castID)
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


def get_id_by_title(title):
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


def acted_together(castID1, castID2):
    with db.session() as session:
        result = session.run(
            '''
            MATCH (c:Cast {castID:$castID1}) - [r:`PERFORMED IN`] -> (m:Movie) <- [r2:`PERFORMED IN`] - (c2:Cast {castID:$castID2})
            RETURN c,c2,m,r,r2
            ''',
            castID1=str(castID1),
            castID2=str(castID2)
        )
        return result.data()


# ONE OF COMPLEX QUERIES
def get_movies_and_actors_with_role(role):
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
