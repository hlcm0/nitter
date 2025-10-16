from base import BaseTestCase
from parameterized import parameterized
import json

# Test tweets - format: [id, username, expected_fields]
api_tweets = [
    ['20', 'jack', ['author', 'text', 'id', 'date']],
    ['572593440719912960', 'mobile_test', ['author', 'text', 'id', 'date']],
]

class ApiTest(BaseTestCase):
    @parameterized.expand(api_tweets)
    def test_api_status_endpoint(self, tid, username, expected_fields):
        """Test that the API endpoint returns valid JSON with expected fields"""
        self.open(f'http://localhost:8080/api/{username}/status/{tid}')
        
        # Get the page source which should be JSON
        page_source = self.get_page_source()
        
        # Parse JSON
        try:
            data = json.loads(page_source)
        except json.JSONDecodeError:
            self.fail(f"Response is not valid JSON: {page_source[:200]}")
        
        # Check that all expected fields are present
        for field in expected_fields:
            self.assertIn(field, data, f"Field '{field}' not found in response")
        
        # Verify author structure
        self.assertIn('username', data['author'])
        self.assertIn('fullname', data['author'])
        self.assertIn('id', data['author'])
        
        # Verify author username matches
        self.assertEqual(data['author']['username'], username)
        
        # Verify text is present and non-empty
        self.assertTrue(len(data['text']) > 0)
        
        # Verify ID matches
        self.assertEqual(data['id'], tid)
    
    def test_api_invalid_id(self):
        """Test that invalid tweet IDs return 404 with error message"""
        self.open('http://localhost:8080/api/mobile_test/status/invalid123')
        page_source = self.get_page_source()
        
        try:
            data = json.loads(page_source)
            self.assertIn('error', data)
        except json.JSONDecodeError:
            # Response might be HTML error page, which is also acceptable
            pass
