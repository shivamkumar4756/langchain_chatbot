import os

project_name = "langchain_chatbot"
folders = [project_name]
files = [
    "app.py",
    "data_loader.py",
    "vector_store.py",
    "chatbot.py",
    "requirements.txt",
    "README.md"
]

os.makedirs(project_name, exist_ok=True)

for file in files:
    file_path = os.path.join(project_name, file)
    with open(file_path, "w") as f:
        if file == "requirements.txt":
            f.write("flask\nopenai\nlangchain\nfaiss-cpu\nrequests\n")
        elif file == "README.md":
            f.write("# LangChain Chatbot\n\nThis project implements a chatbot using LangChain and Flask.")
        else:
            f.write("# " + file + "\n")

print(f"Project structure '{project_name}' created successfully! 🚀")
