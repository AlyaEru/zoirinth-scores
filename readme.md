# Zoirinth Scores

This is a REST API for managing Zoirinth high scores. There is only one endpoint, `/scores`, with `GET` and `POST` allowed. `GET` returns the top 20 highscores, sorted first by level achieved and then by points. `POST` adds a new highscore.
**The score object:**
|Property|Type|Note|
|--|--|--|
|`user`|string|
|`points`|integer|
|`level`|integer|
|`date`|date|Always set to current date on `POST`|

