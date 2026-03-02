import pywhatkit as pw

txt = """Python is an interpreted high-level general-purpose programming language. 
Its design philosophy emphasizes code readability with its use of significant indentation."""

pw.text_to_handwriting(txt, "demo12.png", [255, 0, 0])

print("END")