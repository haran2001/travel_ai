import praw
from helper_functions import (
    get_llm_answer,
    build_prompt,
    add_logo,
    make_data,
    handle_query,
    display_conversation,
    response_generator,
    get_video_id,
    fetch_transcripts,
    create_youtube_df,
)

# reddit = praw.Reddit(
#     client_id="0JcC87gD56ov9dcPQoUHwA",
#     client_secret="D_oQnOAqnzum7Mn5pGP6_YZ9siwi4A",
#     user_agent="your_user_agent",
# )

# subreddit = reddit.subreddit("Shoestring")

# for submission in subreddit.hot(limit=10):
#     print(submission.title)
#     print(submission.body)
#     print(submission.url)


def get_transcripts(video_urls_or_ids):
    video_ids = [get_video_id(url_or_id) for url_or_id in video_urls_or_ids]
    transcripts = fetch_transcripts(video_ids)
    result_transcripts = []
    result_video_ids = []

    for video_id, transcript in transcripts.items():
        if transcript is not None:
            print(f"\nTranscript for {video_id}:\n")
            result_transcripts.append(transcript)
            result_video_ids.append(video_id)
        else:
            print(f"No transcript available for {video_id}")
    return result_video_ids, result_transcripts


if __name__ == "__main__":
    # Replace these with your own list of video URLs or IDs
    video_urls_or_ids = [
        "https://www.youtube.com/watch?v=00ZXaXIABMY",
        # "https://www.youtube.com/watch?v=KuJwC9gTYhw",
        # Add more video URLs or IDs here
    ]
    result_video_ids, result_transcripts = get_transcripts(video_urls_or_ids)
    for i in zip(result_video_ids, result_transcripts):
        response = response_generator("Summarize the important points in : " + str(i))
        # print(response["choices"][0]["message"]["content"])
        print(response)
