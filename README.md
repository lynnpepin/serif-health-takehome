# Installation (and tool motiviation)

We will be using `uv` as the dependency manager and build tool for this project (replacing pip). The touted benefits of `uv` are that it's faster, provides a `cargo`-like interface, etc. But the real benefit is that `pip`, `conda`, `poetry`, etc. have all given me a variety of pains which `uv` has completely solved. If you haven't yet installed `uv`, you can [**find instructions to install `uv` here**](https://docs.astral.sh/uv/getting-started/installation/).

This project is implemented in a [*Jupyter Notebook*](https://jupyter.org/), which is a web interface for . This is *the* tool for the job when the job requires rapid, iterative prototyping like this assignment. As a bonus, Jupyter supports mixing cells of code with cells of Markdown (+ LaTeX, etc).


# Development timeline

> **tldr**: Started work Monday morning

I had a short interview with Salman on Wednesday, February 4th. I anticipated a much larger take-home assignment, and I intended to start work on it that day.

I took a look at these instructions on Saturday February 7th, and so I had time to let it 'marinate' in my head a bit. But seeing that it was intended to be completed in a ~two hour block, I decided instead to complete it in one fell swoop on Monday morning.

Before starting the actual development, I wrote some of this README first thing in the morning.

# No 'vibe coding', because it doesn't make sense here.

> **tldr**: Not necessarily against using LLMs, but that would just slow me down here, and I want to be able to explain the code when asked in the future.

There's kind of a storm of LLM usage going on. I spent four years in a deep learning PhD program, and so I have many well-informed reservations about the embrace of vibe-coding. This is not an exhaustive list!

There are responsible and useful ways to use LLMs with a *positive* impact on code quality and software engineering rigor, so I'm not against them wholesale! But it's not the right tool for the job *here*. The fastest way to get this done correctly is to write it by hand, even if the purpose of this was not to show off my skills and thinking.

Further, I find it *easy* to navigate code I wrote myself (even if I forget ever writing it), while LLM generated code is *harder* to navigate than 

I am also generally against using LLMs to write any text meant for human consumption, like this text here (except for reasons like translation, or OCR, transcribing, and image description.) So, all of this text is written by hand.

This is a problem for me, since I'm someone who has been writing Markdown for years, uses a lot of formatting, and who is a big fan of lists, summaries, and the Table-of-Contents-as-summary (as exemplified in [this 2015 SEC report on the Equifax breach](https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/FINAL%20Equifax%20Report.pdf)). The result is that I think my writing looks a lot like AI!
