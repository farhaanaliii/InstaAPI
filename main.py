from InstaAPI import InstaAPI
from config import RAPIDAPI_KEY

def run_test():
    try:
        api = InstaAPI(key=RAPIDAPI_KEY)

        # Example Instagram post URL
        post_url = "https://www.instagram.com/coding.np/p/DCyqv53Sa8R/"

        posts = api.get_links(post_url)

        for post in posts:
            print("Thumbnail:", post.thumbnail)
            print("Download Link:", post.download)
            print("-" * 30)

    except Exception as e:
        print("Oh no! Something went wrong: 😢", e)


if __name__ == "__main__":
    run_test()
