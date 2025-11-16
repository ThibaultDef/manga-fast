def main():
    print("Hello from manga-fast!")


"""

import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="fal-ai",
    api_key=os.environ["HF_TOKEN"],
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="Qwen/Qwen-Image",
)

"""


if __name__ == "__main__":
    main()
