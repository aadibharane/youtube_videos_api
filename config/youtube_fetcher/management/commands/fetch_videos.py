import asyncio
import aiohttp
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from videos.models import Video

API_KEYS = ["YOUR_API_KEY1", "YOUR_API_KEY2"]
SEARCH_QUERY = "official"
INTERVAL = 10  # seconds

class Command(BaseCommand):
    help = 'Fetch latest videos from YouTube API'

    def handle(self, *args, **kwargs):
        asyncio.run(self.fetch_videos_continuously())

    async def fetch_videos_continuously(self):
        while True:
            for api_key in API_KEYS:
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&order=date&q={SEARCH_QUERY}&key={api_key}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            data = await response.json()
                            for item in data.get('items', []):
                                snippet = item['snippet']
                                video, created = Video.objects.get_or_create(
                                    title=snippet['title'],
                                    description=snippet['description'],
                                    published_at=datetime.strptime(snippet['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                                    thumbnail_url=snippet['thumbnails']['high']['url']
                                )
            await asyncio.sleep(INTERVAL)
