import openai

# Initialize the OpenAI API client
openai.api_key = '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'


def get_space_itinerary():
    # Send a prompt to the OpenAI API
    response = openai.Completion.create(
        engine="Davinci",
        prompt="Recommend a space travel itinerary for a week-long trip.",
        max_tokens=200
    )

    # Return the generated content
    return response.choices[0].text.strip()


if __name__ == "__main__":
    itinerary = get_space_itinerary()
    print("Recommended Space Travel Itinerary:\n", itinerary)
