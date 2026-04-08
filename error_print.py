import traceback
try:
    raise ValueError("Error occurred")
except ValueError as e:
    print("Full Traceback:\n" + "".join(traceback.
                                        format_exception(type(e),
                                                         e,
                                                         e.__traceback__)))
    print(type(e).__name__)
