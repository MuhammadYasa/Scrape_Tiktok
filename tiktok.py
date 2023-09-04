from TikTokApi import TikTokApi
import json
import asyncio
import os

'''
sumber
https://github.com/davidteather/TikTok-Api/tree/main/TikTokApi
'''
#  msToken (ambil dari cookie tiktok.com)
ms_token = os.environ.get(
    "hhYBk6Qpfq1NnN92tduuXR0hSAt5lR-q75xh3BQZfTY5Y8QIzN0CaDbdQBGcn8L5uWk17-xevrrN-E7Kd6Qjdoz1zuWBeU4ZGKEVBDUA-GAfc96j2GN44a8pn5CQ7IgGsXidKq-4XooB1Bk=", None)


async def trending_videos():
    async with TikTokApi() as tiktok:
        await tiktok.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        async for video in tiktok.trending.videos(count=30):
            data: dict = video.as_dict
            with open("export.json", "w+") as f:
                json.dump(data, f)


if __name__ == "__main__":
    asyncio.run(trending_videos())
