import os
import openai
OPENAI_API_KEY = "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"
openai.organization = "org-iT97wlI5m4glS3KXH4Q1IyIT"
openai.api_key = os.getenv(OPENAI_API_KEY)
openai.Model.list()


def get_space_itinerary():
    # Send a prompt to the OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt="Recommend a space travel itinerary for a week-long trip.",
        max_tokens=200
    )

    # Return the generated content
    return response.choices[0].text.strip()


if __name__ == "__main__":
    itinerary = get_space_itinerary()
    print("Recommended Space Travel Itinerary:\n", itinerary)
