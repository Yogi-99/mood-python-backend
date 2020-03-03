class Tone:
    def __init__(self, score, tone_id, tone_name):
        self.score = score
        self.tone_id = tone_id
        self.tone_name = tone_name
        # self.emotions = emotions

    def __repr__(self):
        return f'<Tone {self.tone_id} {self.score}>'
