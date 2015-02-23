# PlaytRate
Sentiment analysis on tweets about restuarants.

Enter a search query and location to poll the yelp API for restaurants and businesses in the area.

Choose a result from the list of results to pull twitter data about the restaurant, and then analyze the emotions towards the restaurant using sentiment analysis provided by alchemyAPI.

The system will store all tweets in a "twitterball" and store important yelp information in an embedded SQLite Database.

The final results of the sentiment analysis will be displayed in a series of golden plates (five being the most positive, zero being entirely negative).


