from txtai import Embeddings
import os
import sys

# Initialize the Embeddings module with the specified model
emb = Embeddings({"path": "sentence-transformers/paraphrase-multilingual-mpnet-base-v2", "content": True})

'''
# Your existing code
emb.upsert([(0, {'table': 'watches', 'field': 'id', 'type': 'integer', 'references': None, 'text': 'Unique identifier for the watch'})])
emb.upsert([(1, {'table': 'watches', 'field': 'brand', 'type': 'string', 'references': None, 'text': 'Brand of the watch'})])
emb.upsert([(2, {'table': 'watches', 'field': 'model', 'type': 'string', 'references': None, 'text': 'Model name of the watch'})])
emb.upsert([(3, {'table': 'watches', 'field': 'movement', 'type': 'string', 'references': None, 'text': 'Type of movement in the watch'})])
emb.upsert([(4, {'table': 'owners', 'field': 'id', 'type': 'integer', 'references': None, 'text': 'Unique identifier for the watch owner'})])
emb.upsert([(5, {'table': 'owners', 'field': 'name', 'type': 'string', 'references': None, 'text': "Owner's full name"})])
emb.upsert([(6, {'table': 'owners', 'field': 'email', 'type': 'string', 'references': None, 'text': "Owner's email address"})])
emb.upsert([(7, {'table': 'watch_collection', 'field': 'id', 'type': 'integer', 'references': None, 'text': 'Unique identifier for the watch collection entry'})])
emb.upsert([(8, {'table': 'watch_collection', 'field': 'watch_id', 'type': 'integer', 'references': 'watches', 'text': 'Foreign key referencing the watch'})])
emb.upsert([(9, {'table': 'watch_collection', 'field': 'owner_id', 'type': 'integer', 'references': 'owners', 'text': 'Foreign key referencing the owner of the watch'})])
emb.upsert([(10, {'table': 'watch_collection', 'field': 'purchase_date', 'type': 'date', 'references': None, 'text': 'Date when the watch was purchased'})])


#tabella movie
emb.upsert([(0, {"text": "movie id", "campo": "id", "tabella": "movie"})])
emb.upsert([(1, {"text": "movie title", "campo": "title", "tabella": "movie"})])
emb.upsert([(2, {"text": "release date of movie", "campo": "release_date", "tabella": "movie"})])
emb.upsert([(3, {"text": "movie genre", "campo": "genre", "tabella": "movie"})])
emb.upsert([(4, {"text": "director's id (foreign key)", "campo": "director_id", "tabella": "movie"})])

#tabella director
emb.upsert([(5, {"text": "director id", "campo": "id", "tabella": "director"})])
emb.upsert([(6, {"text": "director name", "campo": "name", "tabella": "director"})])
emb.upsert([(7, {"text": "number of awards won by director", "campo": "awards", "tabella": "director"})])
emb.upsert([(8, {"text": "director's age", "campo": "age", "tabella": "director"})])

#tabella location
emb.upsert([(9, {"text": "location id", "campo": "id", "tabella": "location"})])
emb.upsert([(10, {"text": "nation where location is found", "campo": "nation", "tabella": "location"})])
emb.upsert([(11, {"text": "is it an openspace location? (boolean)", "campo": "openspace", "tabella": "location"})])

#tabella film_set
emb.upsert([(12, {"text": "location id (foreign key)", "campo": "id_location", "tabella": "film_set"})])
emb.upsert([(13, {"text": "movie id (foreign key)", "campo": "id_movie", "tabella": "film_set"})])

#tabella actor
emb.upsert([(14, {"text": "actor id", "campo": "actor_id", "tabella": "actor"})])
emb.upsert([(15, {"text": "number of awards won by actor", "campo": "prizes_won", "tabella": "actor"})])
emb.upsert([(16, {"text": "actor name", "campo": "actor_name", "tabella": "actor"})])
emb.upsert([(17, {"text": "actor's manager id (foreign key)", "campo": "id_manager", "tabella": "actor"})])

#tabella movie_cast
emb.upsert([(18, {"text": "movie id (foreign key)", "campo": "movie_id", "tabella": "movie_cast"})])
emb.upsert([(19, {"text": "actor id (foreign key)", "campo": "actor_id", "tabella": "movie_cast"})])

#tabella manager
emb.upsert([(20, {"text": "manager id", "campo": "manager_id", "tabella": "manager"})])
emb.upsert([(21, {"text": "manager name", "campo": "name", "tabella": "manager"})])
emb.upsert([(22, {"text": "manager age", "campo": "age", "tabella": "manager"})])


#tabella movie
emb.upsert([
    (0, {"text": "primary key, movie id", "campo": "id", "tabella": "movie"}),
    (1, {"text": "title, movie title", "campo": "title", "tabella": "movie"}),
    (2, {"text": "release date of the movie", "campo": "release_date", "tabella": "movie"}),
    (3, {"text": "genre of the movie", "campo": "genre", "tabella": "movie"}),
    (4, {"text": "foreign key referencing the director of the movie", "campo": "director_id", "tabella": "movie"})
])
#tabella director
emb.upsert([
    (5, {"text": "unique identifier of the director", "campo": "id", "tabella": "director"}),
    (6, {"text": "name of the director", "campo": "name", "tabella": "director"}),
    (7, {"text": "number of awards won by the director", "campo": "awards", "tabella": "director"}),
    (8, {"text": "age of the director", "campo": "age", "tabella": "director"})
])
#tabella location
emb.upsert([
    (9, {"text": "unique identifier of the location", "campo": "id", "tabella": "location"}),
    (10, {"text": "nation where the location is situated", "campo": "nation", "tabella": "location"}),
    (11, {"text": "boolean indicating whether it is an open space location", "campo": "openspace", "tabella": "location"})
])
#tabella film_set
emb.upsert([
    (12, {"text": "foreign key referencing the location (part of the primary key)", "campo": "id_location", "tabella": "film_set"}),
    (13, {"text": "foreign key referencing the movie (part of the primary key)", "campo": "id_movie", "tabella": "film_set"})
])
#tabella actor
emb.upsert([
    (14, {"text": "unique identifier of the actor", "campo": "actor_id", "tabella": "actor"}),
    #(15, {"text": "number of awards won by the actor", "campo": "prizes_won", "tabella": "actor"}),
    (16, {"text": "name of the actor", "campo": "actor_name", "tabella": "actor"}),
    (17, {"text": "foreign key referencing the actor's manager", "campo": "id_manager", "tabella": "actor"})
])
#tabella movie_cast
emb.upsert([
    (18, {"text": "foreign key referencing the movie (part of the primary key)", "campo": "movie_id", "tabella": "movie_cast"}),
    (19, {"text": "foreign key referencing the actor (part of the primary key)", "campo": "actor_id", "tabella": "movie_cast"})
])
#tabella manager
emb.upsert([
    (20, {"text": "unique identifier of the manager", "campo": "manager_id", "tabella": "manager"}),
    (21, {"text": "name manager", "campo": "name", "tabella": "manager"}),
    (15, {"text": "age manager", "campo": "age", "tabella": "manager"})
])
'''
#tabella movie
emb.upsert([(0, {"text": "id of the movie as primary key", "campo": "id", "tabella": "movie"})])
emb.upsert([(1, {"text": "title of the movie, name of the film", "campo": "title", "tabella": "movie"})])
emb.upsert([(2, {"text": "release date of the movie", "campo": "release_date", "tabella": "movie"})])
emb.upsert([(3, {"text": "genre of the movie", "campo": "genre", "tabella": "movie"})])
emb.upsert([(4, {"text": "foreign key of the director of the movie", "campo": "director_id", "tabella": "movie"})])
#tabella director
emb.upsert([(5, {"text": "id of the director as primary key", "campo": "id", "tabella": "director"})])
emb.upsert([(6, {"text": "name of the director", "campo": "name", "tabella": "director"})])
emb.upsert([(7, {"text": "awards won by the director", "campo": "awards", "tabella": "director"})])
emb.upsert([(8, {"text": "age of the director", "campo": "age", "tabella": "director"})])
#tabella location
emb.upsert([(9, {"text": "id of the location as primary key", "campo": "id", "tabella": "location"})])
emb.upsert([(10, {"text": "nation where the location is found", "campo": "nation", "tabella": "location"})])
emb.upsert([(11, {"text": "boolean is it a openspace location", "campo": "openspace", "tabella": "location"})])
#tabella film_set
emb.upsert([(12, {"text": "foreign key of the location, together with movie_id forms the primary key", "campo": "id_location", "tabella": "film_set"})])
emb.upsert([(13, {"text": "foreign key of the movie, together with location_id forms the primary key", "campo": "id_movie", "tabella": "film_set"})])
#tabella actor
emb.upsert([(14, {"text": "id of the actor as primary key", "campo": "actor_id", "tabella": "actor"})])
emb.upsert([(15, {"text": "awards won by the actor", "campo": "prizes_won", "tabella": "actor"})])
emb.upsert([(16, {"text": "name of the actor", "campo": "actor_name", "tabella": "actor"})])
emb.upsert([(17, {"text": "foreign key of the actor's manager", "campo": "id_manager", "tabella": "actor"})])
#tabella movie_cast
emb.upsert([(18, {"text": "foreign key of the movie,", "campo": "movie_id", "tabella": "movie_cast"})])
emb.upsert([(19, {"text": "foreign key of the actor,", "campo": "actor_id", "tabella": "movie_cast"})])
#tabella manager
emb.upsert([(20, {"text": "id of the manager", "campo": "manager_id", "tabella": "manager"})])
emb.upsert([(21, {"text": "name of the manager", "campo": "name", "tabella": "manager"})])
emb.upsert([(22, {"text": "age of the manager", "campo": "age", "tabella": "manager"})])

#Frasi per il test
#
# films directed by directors that have won more than 2 awards
# title and release date of films where the actor named Mario acted
# title and release date of films
# actors that have a dog
# will tomorrow be a sunny day
# 

# Execute a search using the txtai library
# results = emb.search("select score,table,field,type,references,text from txtai where similar('owners email') limit 2")
results = emb.search("select score,text,campo,tabella from txtai where similar ('will tomorrow be a sunny day') limit 7")
frase = 'will tomorrow be a sunny day, sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
# Print the results
print(frase, '\n') 
print(results)


