from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔹 Career profiles for matching
career_data = [
    {
        "career": "Data Scientist",
        "profile": "python, statistics, machine learning, logical, data, job security, research, high salary"
    },
    {
        "career": "Project Manager",
        "profile": "communication, leadership, planning, coordination, people management, organized, high responsibility"
    },
    {
        "career": "Civil Servant",
        "profile": "governance, leadership, general knowledge, stability, public service, high responsibility, ethics"
    },
    {
        "career": "Software Engineer",
        "profile": "coding, algorithms, problem-solving, remote, logical, independent, systems"
    },
    {
        "career": "UX Designer",
        "profile": "creativity, design, user experience, empathy, tech, aesthetic, communication, visual"
    },
    {
        "career": "Business Analyst",
        "profile": "data, communication, business, planning, insight, interpretation, reports"
    },
    {
        "career": "Content Creator",
        "profile": "creative, video editing, communication, social media, public speaking, online presence, entertaining, storytelling"
    },
    {
        "career": "Dance Instructor",
        "profile": "rhythm, expression, dance, body movement, teaching, creativity, performance, choreography"
    },
    {
        "career": "Public Speaker",
        "profile": "confidence, stage presence, leadership, communication, storytelling, influencing, motivation"
    },
    {
        "career": "Writer / Blogger",
        "profile": "writing, imagination, storytelling, creativity, expression, articles, blogging, content creation"
    },
    {
        "career": "Graphic Designer",
        "profile": "visuals, creativity, photoshop, illustrator, design, composition, branding, aesthetic"
    },
    {
        "career": "Music Producer",
        "profile": "music, rhythm, audio editing, creativity, instruments, production, composing, sound"
    },
    {
        "career": "Fitness Trainer",
        "profile": "sports, fitness, motivation, energy, coaching, body training, discipline, health"
    },
    {
        "career": "Event Manager",
        "profile": "planning, organizing, people skills, multitasking, leadership, execution, time management"
    }
]


# 🔹 Matching logic
def recommend_careers(user_input, top_n=3):
    profiles = [item["profile"] for item in career_data]
    career_names = [item["career"] for item in career_data]

    all_texts = profiles + [user_input]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    similarities = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    sorted_results = sorted(zip(career_names, similarities), key=lambda x: x[1], reverse=True)

    return sorted_results[:top_n]

# 🔹 Career course links
course_links = {
    "Data Scientist": "https://www.coursera.org/learn/data-science",
    "Project Manager": "https://www.coursera.org/learn/project-management",
    "Civil Servant": "https://www.edx.org/course/ethics-in-government",
    "Software Engineer": "https://www.coursera.org/learn/software-engineering",
    "UX Designer": "https://www.coursera.org/specializations/ui-ux-design",
    "Business Analyst": "https://www.edx.org/learn/business-analytics",
    "Content Creator": "https://www.coursera.org/learn/social-media-marketing",
    "Dance Instructor": "https://www.udemy.com/course/dance-instructor-course/",
    "Public Speaker": "https://www.coursera.org/learn/public-speaking",
    "Writer / Blogger": "https://www.coursera.org/specializations/content-writing",
    "Graphic Designer": "https://www.coursera.org/specializations/graphic-design",
    "Music Producer": "https://www.coursera.org/learn/music-production",
    "Fitness Trainer": "https://www.coursera.org/learn/fitness",
    "Event Manager": "https://www.udemy.com/course/event-management-course/"
}

def get_course_link(career):
    return course_links.get(career, "https://www.coursera.org")
