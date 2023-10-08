import openai

# Initialize the OpenAI API client
openai.api_key = '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'


def get_space_itinerary():
    # Gather preferences from the user
    destination = input("What space destination would you prefer? (e.g. Moon, Mars, ISS): ")
    duration = input("How many days do you plan to stay? ")
    travel_mode = input("Preferred mode of space travel? (e.g. shuttle, capsule, spacecraft): ")

    # Construct the prompt for OpenAI based on user input
    prompt_text = f"Provide a space travel itinerary for a trip to {destination} lasting {duration} days using a {travel_mode}. Only include actual travel details."

    # Send the constructed prompt to the OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        max_tokens=200
    )

    # Return the generated content
    return response.choices[0].text.strip()


if __name__ == "__main__":
    itinerary = get_space_itinerary()
    print("\nRecommended Space Travel Itinerary based on your preferences:\n", itinerary)