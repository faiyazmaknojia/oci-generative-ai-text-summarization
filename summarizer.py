"""
Enterprise Text Summarization Demo
Using Oracle Cloud Infrastructure (OCI) Generative AI
Author: Faiyaz Zuber Maknojia
"""

def generate_summary(text):
    """
    Simulates an OCI Generative AI text summarization call.
    In actual implementation, OCI Generative AI endpoint is used.
    """
    sentences = text.split(".")
    summary = ". ".join(sentences[:2])
    return summary


if __name__ == "__main__":
    print("OCI Generative AI - Text Summarization Demo\n")

    with open("sample_input.txt", "r") as file:
        input_text = file.read()

    result = generate_summary(input_text)

    print("Original Text:\n")
    print(input_text)

    print("\nGenerated Summary:\n")
    print(result)
