from app.ai_gateway.providers.base import BaseAIProvider
from app.ai_gateway.providers.gemini import GeminiProvider


class AIGateway:
    """Gateway responsável pela comunicação com provedores de IA."""

    def __init__(self, provider: BaseAIProvider | None = None):
        """
        Inicializa o gateway.

        Args:
            provider:
                Provedor de IA.
                Caso não informado, utiliza GeminiProvider.
        """

        self.provider = provider or GeminiProvider()

    def generate(self, prompt: str) -> str:
        """
        Gera uma resposta utilizando o provedor configurado.

        Args:
            prompt:
                Prompt enviado ao modelo.

        Returns:
            Texto retornado pelo provedor.
        """

        return self.provider.generate(prompt)