# Reusable Prompt Templates

## 1. General task prompt
**Role:** You are a [role/expert].  
**Context:** [Explain the situation and audience.]  
**Task:** [State exactly what you want.]  
**Output format:** [Bullets/table/JSON/email/etc.]  
**Constraints:** [Length, tone, language, exclusions.]  
**Quality check:** Mention assumptions and information that needs verification.

## 2. Zero-shot prompt
You are a helpful study assistant. Explain [TOPIC] to a beginner in simple English.
Use one definition, five key points and one practical example. Keep the answer under 150 words.

## 3. Few-shot prompt
Classify each message as Positive, Negative or Neutral.
Examples:
- "I love this course." -> Positive
- "The app keeps crashing." -> Negative
- "The meeting starts at 3 PM." -> Neutral
Now classify: "[NEW MESSAGE]"
Return only the label.

## 4. Summarization prompt
Summarize the text below for [AUDIENCE].
Return:
1. Main idea (one sentence)
2. Five important points
3. Two action items
Do not add facts that are not in the source.
Text: [PASTE TEXT]

## 5. Classification prompt
Classify the input into one of these categories: [CATEGORY LIST].
Return the category and a one-sentence reason. If the information is insufficient, return "Needs review".
Input: [TEXT]

## 6. Structured JSON prompt
Extract the requested fields from the supplied text.
Return valid JSON only, using these keys: [KEYS].
Use null when a value is missing. Do not add comments or Markdown fences.
Text: [TEXT]

## 7. Content generation prompt
Create [CONTENT TYPE] for [AUDIENCE] about [TOPIC].
Tone: [TONE]. Length: [LENGTH].
Include [REQUIRED ITEMS]. Avoid [EXCLUSIONS].
