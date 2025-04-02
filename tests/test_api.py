import unittest
import json
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.base_url = '/api/v1/prompt'

    def test_successful_post_request(self):
        """正常なPOSTリクエストのテスト"""
        data = {
            "mood": "casual",
            "length": 1.0
        }
        response = self.client.post(
            self.base_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'success')
        self.assertEqual(json_data['code'], 200)
        self.assertIn('data', json_data)

    def test_invalid_mood(self):
        """無効なmoodパラメータのテスト"""
        data = {
            "mood": "invalid_mood",
            "length": 1.0
        }
        response = self.client.post(
            self.base_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'error')
        self.assertEqual(json_data['code'], 400)
        self.assertIn('Invalid mood value', json_data['message'])
        self.assertIn('Must be one of:', json_data['message'])

    def test_invalid_length(self):
        """無効なlengthパラメータのテスト"""
        data = {
            "mood": "casual",
            "length": 4.0
        }
        response = self.client.post(
            self.base_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'error')
        self.assertEqual(json_data['code'], 400)

    def test_missing_parameters(self):
        """パラメータが不足している場合のテスト"""
        data = {}
        response = self.client.post(
            self.base_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'error')
        self.assertEqual(json_data['code'], 400)
        self.assertIn('example', json_data)

    def test_method_not_allowed(self):
        """GETメソッドが許可されていないことのテスト"""
        response = self.client.get(self.base_url)
        
        self.assertEqual(response.status_code, 405)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'error')
        self.assertEqual(json_data['code'], 405)
        self.assertEqual(json_data['message'], 'Method Not Allowed')
        self.assertIn('example', json_data)

    def test_invalid_length_value(self):
        """無効なlength値のテスト"""
        data = {
            "mood": "casual",
            "length": 4.0
        }
        response = self.client.post(
            self.base_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'error')
        self.assertIn('Invalid length value', json_data['message'])

    def test_non_numeric_length(self):
        """数値でないlength値のテスト"""
        data = {
            "mood": "casual",
            "length": "invalid"
        }
        response = self.client.post(
            self.base_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'error')
        self.assertIn('Length must be a number', json_data['message'])

if __name__ == '__main__':
    unittest.main() 