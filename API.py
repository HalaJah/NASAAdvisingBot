import openai

# Initialize the OpenAI API client
openai.api_key = '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'


def get_space_itinerary():
    # Send a prompt to the OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt="Recommend a space travel itinerary for a week-long trip., including how long to stay in each planet, how to get there, and what to do once you are on the planet here are some criteria to keep in mind:".Criteria."",
        max_tokens=200
    )

    # Return the generated content
    return response.choices[0].text.strip()


if __name__ == "__main__":
    itinerary = get_space_itinerary()
    print("Recommended Space Travel Itinerary in our solar system \n", itinerary)
