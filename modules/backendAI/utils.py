import ollama
import sys
# It ensures the selected local LLM is available 
def ensureLLM(LLM):
    response = ollama.list()
    available = [m.model.split(":")[0] for m in response.models]
    if LLM not in available:
        try:
            for progress in ollama.pull(LLM,stream=True):
                completed = progress.completed
                total = progress.total
                if isinstance(completed,int) and isinstance(total,int) and total > 0:
                    percentage = (completed/total) * 100
                    print(f'\r{progress.status}: {percentage:6.2f}% completed',end="",flush=True)
                if progress.status == "success":
                    print("completed pulling")
        except Exception as e:
            print(f"\nFailed to download the Model: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"{LLM} already available to use")