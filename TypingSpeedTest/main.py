from time import time
import random as r

def mistake(paragraph, user_input):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != user_input[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(start, end, user_input):
    total_time = end - start
    speed = len(user_input.split()) / (total_time / 60)  # words per minute
    return round(speed)

text = [
    "Artificial intelligence is transforming the way we live and work, with new applications in healthcare, finance, education, and many other fields around the world today.",
    "The quick brown fox jumps over the lazy dog while the sun sets behind the mountains, casting long shadows over the valley filled with flowers and tall green trees.",
    "Learning Python programming opens up a wide range of possibilities for data science, automation, game development, web applications, and scripting tasks across all platforms.",
    "Climate change remains a critical global issue, and it is essential for nations to collaborate on sustainable solutions involving clean energy, conservation, and responsible industry practices.",
    "A successful morning routine often includes exercise, a healthy breakfast, setting clear intentions for the day, and avoiding distractions like social media or excessive news consumption.",
    "Books offer a gateway into different worlds, allowing us to explore new ideas, understand diverse cultures, and gain knowledge and inspiration from the experiences of others.",
    "Space exploration has advanced rapidly in recent years, with missions to Mars, private companies launching satellites, and ambitious plans for lunar bases and manned interplanetary travel.",
    "Music has the power to influence our emotions, trigger memories, and bring people together across languages, cultures, and generations through rhythm, melody, and storytelling.",
    "Effective communication involves active listening, clarity of thought, respectful dialogue, and adapting your message to the audience's needs, values, and expectations in various contexts.",
    "In today's digital age, cybersecurity is more important than ever as we rely on technology for communication, banking, work, and sharing personal information across connected devices."
]

print("***** Typing Speed Test *****\n")
paragraph = r.choice(text)
print(paragraph)
print()

start_time = time()
user_input = input("Enter here: ")
end_time = time()

print("\nResults:")
print("Speed:", speed_time(start_time, end_time, user_input), "WPM")
print("Errors:", mistake(paragraph, user_input))
