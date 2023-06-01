# Koffie Labs Backend Coding Challenge

[Challenge README here](https://github.com/KoffieLabs/backend-challenge/tree/4717c93869846789432c273755f77a43c28d009d)

Also copied the text from that README to the project [here](original_challenge_readme.md).

## Test It Yourself

Assuming you have Python 3:

```
git clone [this]
cd koffie-project
python3 -m pip install -r requirements.txt
python3 -m uvicorn main:app --reload
```

From here I would recommend using [the Postman collection included here](koffie-project.postman_collection.json).

## Tradeoffs

I made a few tradeoffs in the interest of my own time.

- Few automatable tests
- Light error handling or validation
- Code structure and file/directory structure very basic
- No throttling, circuit-breaking, or other abuse protection and mitigation

### Few automatable tests

I did add a `models_test.py` file to ensure I understood pytest at a surface level. If this were headed to production, I would want to more rigorously test the Vehicle model in particular, including its class methods for finding records either via cache or the vPIC API. I might circle back to learn the mocking/stubbing story in pytest, but I'm going to leave it alone for now.

### Light error handlign or validation

I added Pydantic per the FastAPI docs to go alongside SQLAlchemy, but I did not do much with it. I would start there for validation, and then add more robust handling of validation errors and the like.

### Code structure and file/directory structure very basic

I don't love having a single `models.py`, `schemas.py`, etc. If this were going to be long-lived, I would add some structure, and separate out models, schemas, etc into seperate files.

I think I could also go another step in refactoring some things, perhaps, but for such a small project, I am relatively happy with it.

### No throttling, circuit-breaking, or other abuse protection and mitigation

If this were going into production, we would want to put in place some protection against bad actors hitting our API (not to mention authentication and authorization). We might also want to create a circuit breaker scenario for the third-party API so that when it's down it doesn't appear as if we are also down. (We can continue to serve from our cache.)