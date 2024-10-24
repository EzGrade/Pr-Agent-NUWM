from typing import List, Dict
import openai
from openai import api_key

import config


class AiRequest:
    def __init__(
            self,
            context: List[Dict[str, str]],
            model: str = config.OPENAI_MODEL,
    ):
        self.context = context
        self.model = model

    def get_response(
            self,
    ) -> str:
        """
        Get response from OpenAI
        :return response: OpenAI response
        """
        openai.api_key = api_key
        response = openai.chat.completions.create(
            model=self.model,
            messages=self.context,
            stream=False
        )
        return response.choices[0].message.content
