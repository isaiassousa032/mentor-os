from abc import ABC, abstractmethod


class BaseAIProvider(ABC):
    """Interface base para todos os provedores de IA."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Envia um prompt ao modelo e retorna a resposta.

        Args:
            prompt: Texto enviado ao modelo.

        Returns:
            Resposta gerada pelo modelo.
        """
        pass