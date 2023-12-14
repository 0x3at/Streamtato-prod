import os
import re
import json
import subprocess


def get_video_metadata(video_path):
    """
    Extracts metadata from a video file using ffprobe.
    """
    cmd = f"ffprobe -v quiet -print_format json -show_format \"{video_path}\""
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return json.loads(result.stdout)['format']


def extract_episode_number(filename):
    """
    Extracts episode number from the file name.
    If the file name contains 'sp', it's marked as a special.
    """
    special = 'sp' in filename.lower()
    episode_num = re.findall(r'\d+', filename)
    return int(episode_num[0]) if episode_num else None, special


def create_media_objects(video_folder, thumbnail_folder="thumbnails", output_file="media_objects.json"):
    media_objects = []

    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(video_folder, filename)
            metadata = get_video_metadata(video_path)

            episode_number, special = extract_episode_number(filename)

            media_object = {
                "show_name": "DragonBall(1986)",
                "episode_number": episode_number,
                "special": special,
                "name": filename,
                "title": metadata.get("tags", {}).get("title", None),
                "length": int(float(metadata.get("duration", 0))),
                "year": None,
                "genre": None,
                "rating": None,
                "image_url": f"dragonball/{thumbnail_folder}/{episode_number}_thumbnail.jpg",
                "video_url": f"https://streamtato.sfo2.cdn.digitaloceanspaces.com/dragonball/{filename}"
            }
            media_objects.append(media_object)

    with open(output_file, 'w') as f:
        json.dump(media_objects, f, indent=4)


def main():
    video_folder = input("Enter the path of the folder containing MP4s: ")
    create_media_objects(video_folder)


if __name__ == "__main__":
    main()
