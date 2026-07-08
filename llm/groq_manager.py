from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

import config


class GroqManager:
    """
    Handles interactions with the Groq LLM.
    """

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=config.GROQ_API_KEY,
            model_name=config.LLM_MODEL,
            temperature=0
        )

        # --------------------------------------------------
        # Prompt for Answer Generation
        # --------------------------------------------------

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an AI assistant for enterprise document question answering.

Your job is to answer ONLY using the retrieved document context.

The conversation history is provided only to understand follow-up questions
such as "it", "they", "those", or "that section".

Never answer using your own knowledge.

If the answer is not found in the document context, reply exactly:

"I couldn't find that information in the uploaded document."

========================
Conversation History
========================
{chat_history}

========================
Document Context
========================
{context}

========================
Current Question
========================
{question}

Answer:
"""
        )

        # --------------------------------------------------
        # Prompt for Question Rewriting
        # --------------------------------------------------

        self.rewrite_prompt = ChatPromptTemplate.from_template(
            """
You are an AI assistant that rewrites follow-up questions.

Using the conversation history, rewrite the user's latest question into a
complete standalone question.

Do NOT answer the question.

Only return the rewritten standalone question.

Conversation History:
{chat_history}

Current Question:
{question}

Standalone Question:
"""
        )

    def rewrite_question(
        self,
        question: str,
        chat_history: str = ""
    ) -> str:
        """
        Rewrites follow-up questions into standalone questions.
        """

        messages = self.rewrite_prompt.format_messages(
            question=question,
            chat_history=chat_history
        )

        response = self.llm.invoke(messages)

        return response.content.strip()

    def generate_answer(
        self,
        question: str,
        context: str,
        chat_history: str = ""
    ) -> str:
        """
        Generates an answer using the retrieved document context.
        """

        messages = self.prompt.format_messages(
            context=context,
            question=question,
            chat_history=chat_history
        )

        response = self.llm.invoke(messages)

        return response.content