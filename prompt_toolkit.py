"""Beginner-friendly prompt engineering demonstrations.

These examples are deterministic demonstrations; they do not call an external AI API.
Replace the sample functions with a real model call when you are ready.
"""
import json
import re


def make_prompt(role, context, task, output_format, constraints):
    """Build a prompt using role, context, task, format and constraints."""
    return (
        f"ROLE: {role}\nCONTEXT: {context}\nTASK: {task}\n"
        f"OUTPUT FORMAT: {output_format}\nCONSTRAINTS: {constraints}"
    )


def zero_shot_classify(text):
    """Simple rule-based demonstration of a zero-shot style classification task."""
    t = text.lower()
    if any(word in t for word in ("love", "excellent", "great", "happy")):
        return "Positive"
    if any(word in t for word in ("hate", "crashing", "poor", "angry", "bad")):
        return "Negative"
    return "Neutral"


def few_shot_classify(text):
    """Illustrates a few-shot pattern; examples are embedded in the prompt concept."""
    return zero_shot_classify(text)


def summarize(text, max_sentences=2):
    """A tiny extractive demo, not a full AI summarizer."""
    sentences = re.split(r"(?<=[.!?])\\s+", text.strip())
    return " ".join(sentences[:max_sentences])


def extract_contact(text):
    """Extract a few fields and return valid JSON."""
    email_match = re.search(r"[\\w.+-]+@[\\w.-]+\\.[A-Za-z]{2,}", text)
    phone_match = re.search(r"(?:\\+?\\d[\\d -]{7,}\\d)", text)
    name_match = re.search(r"Name:\\s*([A-Za-z ]+)", text, re.I)
    result = {
        "name": name_match.group(1).strip() if name_match else None,
        "email": email_match.group(0) if email_match else None,
        "phone": phone_match.group(0).strip() if phone_match else None,
    }
    return json.dumps(result, indent=2)


def generate_study_plan(topic, days=3):
    """Template-based content generation demonstration."""
    return [
        {"day": day, "task": f"Study {topic}: read key concepts and write short notes."}
        for day in range(1, days + 1)
    ]


def main():
    print("PROMPT ENGINEERING & AI PRODUCTIVITY TOOLKIT")
    print("\\n1) Structured prompt example:")
    print(make_prompt(
        "A beginner-friendly Python tutor",
        "The learner is new to programming",
        "Explain Python variables",
        "Five bullet points and one example",
        "Use simple English; maximum 120 words"
    ))
    print("\\n2) Classification examples:")
    for message in ("I love this course!", "The app keeps crashing.", "The class starts at 10."):
        print(f"{message!r} -> {zero_shot_classify(message)}")
    print("\\n3) Summarization example:")
    print(summarize("Prompt engineering means writing clear instructions for an AI system. "
                    "A good prompt includes context, a task and constraints."))
    print("\\n4) JSON extraction example:")
    print(extract_contact("Name: Asha Patil, email: asha@example.com, phone: 9876543210"))
    print("\\n5) Generation example:")
    print(generate_study_plan("Prompt Engineering", 3))


if __name__ == "__main__":
    main()
