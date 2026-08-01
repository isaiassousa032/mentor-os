from app.ai_gateway.providers.base import BaseAIProvider


class GeminiProvider(BaseAIProvider):
    """Implementação inicial do provedor Google Gemini."""

    def generate(self, prompt: str) -> str:
        """
        Simula uma resposta do Gemini.

        Args:
            prompt: Texto enviado ao modelo.

        Returns:
            Resposta simulada.
        """
        return (
            "GeminiProvider inicializado com sucesso. "
            "Integração com a API será implementada nas próximas etapas."
        )