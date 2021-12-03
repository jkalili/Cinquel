# TMDB Dataset

<a href = "https://www.kaggle.com/tmdb/tmdb-movie-metadata">TMDB 5000 Movie Dataset Link </a>

## What the dataset contains:

This dataset contains data from about 5000 well known American movies, with unique json values for each specific movie.

## What applications would find the dataset useful?

Applications that might find this dataset useful could be film review sites that need to list movies organized by a particular genre, cast member, producer, director, year, etc. We may even be able to predict which films may be highly rated in the future, given the popularity score, and revenue.

## What kinds of questions might such applications ask of this dataset?

Our datasets could answer questions such as, "How many movies are about pirates?" or "How many movie titles contain the word 'dog' that are in the action genre? Given a wide variety of questions, our application will return accurate results to the user.

# Schema

<center><img src="./assets/schema.png" style="width: 100%" ></img></center>

<br>

# Rationale

**Why we chose the logical data model for this dataset and application—why was it the best fit? What features/characteristics were in its favor? What weren’t in its favor (but clearly wasn’t enough to overturn it)?**

We decided to use the Neo4j graph database model for our full database sdk partially because it was most fresh in our minds, but also because we found the graph databse model to fit our dataset well. The nodes, relations, and properties we made, made it very easy to understand the returned data subsets. It seemed like it was the best of both worlds (document/relational). We also like how similar cypher and sql were. Something we were concerned about was the scalability issued that come with a graph database, but given the managable size of our dataset, we decided to move forward with it anyways.

# Assessment—now that the assignment is done, how does your group feel about this choice?

Overall, our group was happy with the decision to use a graph database model. The movies in our database had a number of different types relationships, `HAS_KEYWORD`,

# Populating the Database

## This process assumes you have already gotten a fresh neo4j database running on your machine

1. Run loader.py
2. run:

```
NEO4J_CONF=<PATH TO CONF> neo4j-admin import --database=neo4j --delimiter="|" --nodes=Movie=<PATH TO movies.csv> --nodes=Genre=<PATH TO genres.csv> --nodes=Cast=<PATH TO cast.csv> --nodes=Crew=<PATH TO crew.csv> —nodes=Keywords=<PATH TO keywords.csv> --relationships=<PATH TO genre_relations.csv> --relationships=<PATH TO cast_relations.csv> --relationships=<PATH TO keyword_relations.csv> --relationships=<PATH TO crew_relations.csv>
```

3. start your, now populated, neo4j server with this command:

```
NEO4J_CONF=<PATH TO CONF> neo4j console
```
