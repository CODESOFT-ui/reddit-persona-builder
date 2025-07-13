import random

class RedditPersona:
    """
    RedditPersona simulates a Reddit user's style, tone, and typical behaviors
    for use in chatbots, NPCs, or testing conversational AI.
    """

    def __init__(self, username=None, subreddit=None, karma=None):
        self.username = username or self.generate_username()
        self.subreddit = subreddit or random.choice([
            "r/AskReddit", "r/funny", "r/science", "r/worldnews", "r/gaming"
        ])
        self.karma = karma if karma is not None else random.randint(100, 10000)
        self.comment_templates = [
            "I totally agree with you.",
            "Can you provide a source?",
            "This has been posted before.",
            "Upvoted for visibility!",
            "OP, thanks for sharing.",
            "Lol, this made my day.",
            "As someone who works in {subreddit}, I can confirm.",
            "This reminds me of another post I saw here.",
        ]

    def generate_username(self):
        adjectives = ["Cool", "Funny", "Serious", "Random", "Helpful"]
        nouns = ["Cat", "Dog", "Fox", "User", "Coder"]
        return f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(10, 9999)}"

    def generate_comment(self):
        template = random.choice(self.comment_templates)
        if "{subreddit}" in template:
            return template.format(subreddit=self.subreddit)
        return template

    def introduce(self):
        return (f"Hey, I'm u/{self.username} from {self.subreddit}. "
                f"I have about {self.karma} karma. Ask me anything!")

if __name__ == "__main__":
    persona = RedditPersona()
    print(persona.introduce())
    for _ in range(3):
        print(persona.generate_comment())
