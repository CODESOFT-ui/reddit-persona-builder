# RedditPersona

A simple Python class to simulate a Reddit user's style, tone, and typical behaviors. This persona can be used for chatbots, NPCs, or for testing conversational AI systems with Reddit-like interactions.

## Features

- Randomized username, subreddit, and karma points.
- Generates common Reddit-style comments.
- Provides a brief self-introduction.

## Usage

```python
from reddit_persona import RedditPersona

persona = RedditPersona()
print(persona.introduce())
print(persona.generate_comment())
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

See [`requirements.txt`](requirements.txt).

## License

MIT License
