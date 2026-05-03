def messageGenerator(systemPrompt, history, message):
    context_text = "\n".join(
        [f"{h.get('role', 'user').upper()}: {h.get('content', '')}" for h in history]
    )

    systemPromptMessage = {
        "role": "system",
        "content": (
            f"{systemPrompt}\n"
            "Use <CONTEXT> only as background memory. "
            "Answer only the content inside <ACTIVE_QUESTION>."
        ),
    }
    contextMessage = {
        "role": "user",
        "content": f"<CONTEXT>\n{context_text}\n</CONTEXT>",
    }
    activeQuestion = {
        "role": "user",
        "content": f"<ACTIVE_QUESTION>\n{message}\n</ACTIVE_QUESTION>",
    }
    return [systemPromptMessage, contextMessage, activeQuestion]
