FROM mongo:latest
COPY ./init-db.js /docker-entrypoint-initdb.d/init-db.js
VOLUME [ "/docker-entrypoint-initdb.d/init-db.js:ro" ] 
# ENV MONGO_INITDB_DATABASE=animal_db
# ENV MONGO_INITDB_ROOT_USERNAME=root
# ENV MONGO_INITDB_ROOT_PASSWORD=pass
EXPOSE 27017