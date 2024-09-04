import sys
import os
import unittest
from unittest.mock import MagicMock

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models import VideoScript
from api_manager import get_chatgpt_response

class TestAPIManager(unittest.TestCase):
    def setUp(self):
        # Mock OpenAI client
        self.mock_client = MagicMock()

        # Sample response
        self.sample_response = VideoScript(
            title="Sample Title",
            description="Sample Description",
            hashtags="#Sample #Test",
            opening_scene={"description": "Opening scene", "visual_prompt": "Opening visual"},
            scenes=[
                {"description": "Scene 1", "visual_prompt": "Visual 1"},
                {"description": "Scene 2", "visual_prompt": "Visual 2"},
            ],
            closing_scene={"description": "Closing scene", "visual_prompt": "Closing visual"}
        )

        # Mock the API call
        self.mock_client.beta.chat.completions.parse.return_value.choices[0].message.parsed = self.sample_response

    def test_get_chatgpt_response(self):
        initial_prompt = "This is an initial prompt."
        name = "Test Name"
        response = get_chatgpt_response(initial_prompt, name, self.mock_client)
        
        # Assertions to check if the response matches the sample response
        self.assertEqual(response.title, "Sample Title")
        self.assertEqual(response.description, "Sample Description")
        self.assertEqual(response.hashtags, "#Sample #Test")
        self.assertEqual(len(response.scenes), 2)
        self.assertEqual(response.scenes[0].description, "Scene 1")
        self.assertEqual(response.closing_scene.description, "Closing scene")

if __name__ == '__main__':
    unittest.main()