
def evaluate_transcript(data):
    text = data.get("raw_text", "")
    mock_result = {
        "student_name": "Demo Student",
        "total_credits": 60,
        "gpa": 3.2,
        "top_matches": [
            {"program": "BBA Business Admin", "credits_remaining": 30, "salary": 55000, "employability_score": "★★★★☆"},
            {"program": "BA Psychology", "credits_remaining": 35, "salary": 41000, "employability_score": "★★★☆☆"}
        ]
    }
    return mock_result
