from typing import List, Dict, Any

def merge_responses(responses: List[Dict[str, Any]]) -> str:
    """
    Merges and ranks responses from multiple AI models.

    Args:
        responses (List[Dict[str, Any]]): A list of responses from different AI models.
            Each response should be a dictionary containing 'model_name' and 'text'.

    Returns:
        str: The final merged response.
    """
    # Sort responses based on a simple ranking criteria, e.g., length of response
    sorted_responses = sorted(responses, key=lambda x: len(x['text']), reverse=True)

    # Merge the top responses intelligently
    merged_response = " ".join(response['text'] for response in sorted_responses)

    return merged_response.strip()