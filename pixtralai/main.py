import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="1"

from vllm import LLM
from vllm.sampling_params import SamplingParams

MODEL_NAME = "mistralai/Pixtral-12B-2409"

def run():
    print("Running the code")
    sampling_params = SamplingParams(max_tokens=8192)
    llm = LLM(model=MODEL_NAME, tokenizer_mode="mistral")

    prompt = "Describe the image in one sentence"
    image_url = "https://picsum.photos/id/237/200/300"

    messages = [
        {
            "role": "Describe the image in one sentence",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ]

    outputs = llm.model.chat(messages, sampling_params=sampling_params)

    return outputs[0].outputs[0].text


    




