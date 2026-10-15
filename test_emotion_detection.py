"""Validate all five required emotions using the live Watson model."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the required statement and dominant-emotion pairs."""
    def check_emotion(self, text, expected):
        """Assert the model's dominant emotion for one statement."""
        result = emotion_detector(text)
        print(text, result)
        self.assertEqual(result['dominant_emotion'], expected)

    def test_joy(self):
        """Recognize joy."""
        self.check_emotion('I am glad this happened', 'joy')

    def test_anger(self):
        """Recognize anger."""
        self.check_emotion('I am really mad about this', 'anger')

    def test_disgust(self):
        """Recognize disgust."""
        self.check_emotion('I feel disgusted just hearing about this', 'disgust')

    def test_sadness(self):
        """Recognize sadness."""
        self.check_emotion('I am so sad about this', 'sadness')

    def test_fear(self):
        """Recognize fear."""
        self.check_emotion('I am really afraid that this will happen', 'fear')


if __name__ == '__main__':
    unittest.main()
