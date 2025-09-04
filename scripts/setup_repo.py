import os
import json

# --- Config ---
roadmap_file = "data/roadmaps.json"
output_folder = "career-tracks"
projects_folder = "projects"
visuals_folder = "visuals"
root_readme = "README.md"

# --- Load JSON ---
with open(roadmap_file, "r") as f:
    roadmap_data = json.load(f)

# --- Step 1: Generate career-track skills.md files ---
for track, skills_list in roadmap_data.items():
    track_folder = os.path.join(output_folder, track.lower())
    os.makedirs(track_folder, exist_ok=True)
    skills_file = os.path.join(track_folder, "skills.md")
    with open(skills_file, "w") as f:
        f.write(f"# {track.capitalize()} Roadmap\n\n")
        f.write("## Skills\n")
        if isinstance(skills_list, list):
            for skill in skills_list:
                if isinstance(skill, dict):
                    name = skill.get("name", "")
                    level = skill.get("level", "")
                    f.write(f"- {name} ({level})\n" if level else f"- {name}\n")
                else:
                    f.write(f"- {skill}\n")
        f.write("\n## Suggested Projects\n- TODO: Add relevant projects\n")

print("✅ Career-track skills.md files generated!")

# --- Step 2: Create projects and README.md ---
projects = {
    "portfolio-website": ["HTML", "CSS", "JavaScript", "React"],
    "blog-api": ["Python", "Flask", "SQL"],
    "ecommerce-frontend": ["HTML", "CSS", "JavaScript", "React"]
}

os.makedirs(projects_folder, exist_ok=True)

for project, skills in projects.items():
    project_path = os.path.join(projects_folder, project)
    os.makedirs(project_path, exist_ok=True)
    readme_path = os.path.join(project_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {project.replace('-', ' ').title()}\n\n")
        f.write("## Skills Learned\n")
        for skill in skills:
            f.write(f"- {skill}\n")
        f.write("\n## Description\nBrief description of the project.\n")
        f.write("\n## Learning Goals\n- TODO: Add learning goals\n")
        f.write("\n## Folder Structure\n```\n- TODO: Add folder structure\n```\n")

print("✅ Project folders and README.md files created!")

# --- Step 3: Create visuals folder ---
os.makedirs(visuals_folder, exist_ok=True)
# Placeholder: User can add visuals/roadmaps.png manually
with open(os.path.join(visuals_folder, "placeholder.txt"), "w") as f:
    f.write("Add roadmap PNG or diagrams here.")

print("✅ Visuals folder created!")

# --- Step 4: Create/update root README.md ---
with open(root_readme, "w") as f:
    f.write("# Software Engineering Ecosystem\n\n")
    f.write("Visual roadmap of software engineering skills, career tracks, and projects.\n\n")

    f.write("## Career Tracks\n\n")
    for track in roadmap_data.keys():
        f.write(f"- [{track.capitalize()}]({output_folder}/{track.lower()}/skills.md)\n")

    f.write("\n## Projects\n\n")
    for project in projects.keys():
        f.write(f"- [{project.replace('-', ' ').title()}]({projects_folder}/{project}/README.md)\n")

    f.write("\n## Visuals\n\n")
    f.write(f"Add diagrams or roadmap images in `{visuals_folder}/`\n")

    f.write("\n## Data\n\n")
    f.write("All raw roadmap files are stored in `data/`\n")
    f.write("- roadmaps.json\n- roadmaps.md\n- roadmaps.mmd\n")

print("✅ Root README.md created/updated successfully!")
