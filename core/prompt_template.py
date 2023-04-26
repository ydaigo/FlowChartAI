mermaid_template="""
Create a simple mind map in Japanese.

use the following format:

INPUT:
the input text you must answer

ANSWER:
graph LR
  A(Programming Language)
  B(Compiled Language)
  C(Interpreted Language)
  D(JIT-compiled Language)
  A-->B
  A-->C
  A-->D

  B-->B1(C programming language)
  B-->B2(C++)
  B-->B3(Rust)

  C-->C1(Python)
  C-->C2(JavaScript)
  C-->C3(Ruby)

  D-->D1(Java)
  D-->D2(C#)
  D-->D3(Kotlin)

INPUT:
{input}

ANSWER:
"""
