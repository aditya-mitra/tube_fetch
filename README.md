# Tube Fetch

Tube Fetch is a full stack application capable of fetching the latest YouTube videos from a particular topic.
The server constantly fetches from YouTube, saves the new records in the database and repeats the process every 2 minutes.
The other functionalities like search and pagination are also featured in the server and can be used via the dashboard.




## Authors

- [@aditya-mitra](https://www.github.com/aditya-mitra)

  
## Installation

The Entire Application can be started using docker-compose
Please make sure you have [Docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) installed

Please use the below script to install, build and start the application all at once.


```bash
curl https://raw.githubusercontent.com/aditya-mitra/tube_fetch/main/bootstrap.sh | bash
```

## Features

- Latest Results being fetched every 2 minutes
- Results are paginated (10 results per page)
- Fuzzy Search API (with partial matches) to search for videos in matching title or description
- Dockerized and Scalabe
- Supports Multiple API Keys (More keys can be added at [localhost:9000/api/v1/yt-api-key](http://localhost:9000/api/v1/yt-api-key))
- Dashboard to search, sort and view the paginated results from the API


## Screenshots

### Optimized Search Results

If there are more than 50 same results (in the same sorted manner they fetched from the YouTube API), the server will stop looking for more results to prevent further consumption of the API Key

![Optimized-img](https://user-images.githubusercontent.com/55396651/134217275-132ff870-a7f3-46cc-9c29-dce0b801144e.png)

### Rotating API Keys

Before getting more results, the API Keys to be used is checked and validated

![rotating-keys](https://user-images.githubusercontent.com/55396651/134301346-506a4784-0c2c-4439-9916-27f7279d1fa6.png)

### Dockerized

![starting](https://i.ibb.co/C8SYyS0/image.png)
![ending](https://i.ibb.co/230Pg5W/image.png)

### Application Screenshots

#### Full Page

![appshots1](https://i.ibb.co/R4RDdZW/image.png)

#### Pagination, Search and Sorting

All the features of pagination, search and sorting are available at the dashboard - http://localhost:5000

![appshots2](https://user-images.githubusercontent.com/55396651/134302317-cfa052c6-02f7-42f2-9720-97c23eeeb0b4.png)
## Tech Stack

**Server:** Django, Django Rest Framework, PostgreSQL

**Client:** Vite, Preact

## License

[MIT](https://choosealicense.com/licenses/mit/)

  