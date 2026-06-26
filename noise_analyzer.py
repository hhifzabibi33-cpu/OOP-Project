class NoiseAnalyzer:

    def __init__(self, threshold=50):
        self.threshold = threshold

    def analyze_noise(self, noise_level):

        if noise_level < 30:
            return "LOW"

        elif noise_level < self.threshold:
            return "MODERATE"

        else:
            return "HIGH"

    def is_dangerous(self, noise_level):

        return noise_level >= self.threshold