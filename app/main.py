def health_check():
    return {
        "status": "healthy",
        "service": "cicd-lab"
    }

def get_version():
    return "1.0.0"