
FROM postgres

ENV POSTGRES_PASSWORD=567234
EXPOSE 5432
CMD ["postgres", "-c", "listen_addresses=0.0.0.0"]


# docker build -t my_postgres_image .
# docker run --name quotesapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres

