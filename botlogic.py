from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper
import openai
import sys
import os

# Initialize the OpenAI API client
os.environ["OPENAI_API_KEY"] = ''


# Load planet data from .txt files into a dictionary
def createVectorIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 0.6

    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size)

    def openai_predictor(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=tokens,
            temperature=0
        )
        return response.choices[0].text

    llmPredictor = LLMPredictor(llm=openai_predictor)
    docs = SimpleDirectoryReader(path).load_data()

    vectorIndex = GPTVectorStoreIndex(documents=docs, nodes=docs,  llm_predictor=llmPredictor, prompt_helper=prompt_helper)

    vectorIndex.storage_context.persist()

    return vectorIndex

vectorIndex = createVectorIndex('knowledge')

def answerMe(vectorIndex):
    vIndex = GPTVectorStoreIndex.from_documents(vectorIndex)
    while True:
        prompt = input('Please ask: ')
        response =  vIndex.query(prompt, response_mode="compact")
        print(f"Response: {response} \n")

answerMe(vectorIndex)
