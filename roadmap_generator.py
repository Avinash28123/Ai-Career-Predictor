def generate_roadmap(predictions, user_skills, cgpa):
    roadmap = {}
    top = predictions[:3]
    for career, score in top:
        items = []
        if 'Cloud' in career or 'DevOps' in career:
            items = ["Learn AWS Cloud Practitioner", "Build 2 projects with Docker and Terraform", "Learn Linux basics"]
        elif 'Data Scientist' in career or 'Computer Vision' in career or 'Data' in career:
            items = ["Learn stats & probability basics", "Complete 2 ML projects (regression/classification)", "Hands-on with PyTorch or TensorFlow"]
        elif 'Full Stack' in career:
            items = ["Build 2 full-stack apps with React + Flask/Node", "Learn SQL and REST APIs", "Deploy apps on cloud"]
        else:
            items = ["Build 1 domain-specific project", "Learn industry tools related to role"]
        roadmap[career] = {
            'confidence': round(float(score)*100,2),
            'recommended_path': items
        }
    return roadmap
