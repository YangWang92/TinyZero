import re


def extract_solution(solution_str):
    answer_pattern = r'<answer>(.*?)</answer>'
    match = re.search(answer_pattern, solution_str)
    if match:
        final_answer = match.group(1).strip()
    else:
        final_answer = None
    return final_answer


def compute_score(solution_str, ground_truth, method='strict', format_score=0.05, score=1.):
    """The scoring function for GSM8k.

    Reference: Trung, Luong, et al. "Reft: Reasoning with reinforced fine-tuning." Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2024.

    Args:
        solution_str: the solution text
        ground_truth: the ground truth
        method: the method to extract the solution, choices are 'strict' and 'flexible'
        format_score: the score for the format
        score: the score for the correct answer
    """
    answer = extract_solution(solution_str=solution_str)
    if answer is None:
        return 0
    else:
        if answer == ground_truth:
            return score
        else:
            return format_score