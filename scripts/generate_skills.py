import json
import os

# --- Config ---
roadmap_file = "data/roadmaps.json"  # path to your JSON
output_folder = "career-tracks"      # where to create career-track folders

# --- Load JSON ---
with open(roadmap_file, "r") as f:
    data = json.load(f)

# --- Generate skills.md for each track ---
for track, skills_list in data.items():
    # Create folder for track
    track_folder = os.path.join(output_folder, track.lower())
    os.makedirs(track_folder, exist_ok=True)

    skills_file = os.path.join(track_folder, "skills.md")
    with open(skills_file, "w") as f:
        f.write(f"# {track} Roadmap\n\n")
        f.write("## Skills\n")

        # Check if skills_list is a list
        if isinstance(skills_list, list):
            for skill in skills_list:
                # Handle dict or string
                if isinstance(skill, dict):
                    name = skill.get("name", "")
                    level = skill.get("level", "")
                    if level:
                        f.write(f"- {name} ({level})\n")
                    else:
                        f.write(f"- {name}\n")
                else:
                    f.write(f"- {skill}\n")
        else:
            f.write(f"- {skills_list}\n")

        f.write("\n## Suggested Projects\n")
        f.write("- TODO: Add relevant projects\n")

print("✅ Skills.md files generated successfully!")
