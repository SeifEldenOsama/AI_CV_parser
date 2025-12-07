def simple_parse_cv(raw_text):
    parsed = {
        "Name": "Unknown",
        "Email": "Unknown",
        "Phone": "Unknown",
        "Skills": [],
        "Experience": []
    }

    lines = raw_text.split("\n")

    for line in lines:
        l = line.lower()

        if "name" in l:
            parsed["Name"] = line.split(":")[-1].strip()
        if "email" in l or "gmail" in l:
            parsed["Email"] = line.strip()
        if "phone" in l or "+2" in l:
            parsed["Phone"] = line.strip()

        if any(skill in l for skill in ["python", "java", "ml"]):
            parsed["Skills"].append(line.strip())

    parsed["Experience"] = [
        {"Company": "ABC Corp", "Role": "Intern", "Years": "2023 - 2024"}
    ]

    return parsed
