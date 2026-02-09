# Installation (and tool motiviation)

I will be using `uv` as the dependency manager and build tool for this project (replacing pip). The touted benefits of `uv` are that it's faster, provides a `cargo`-like interface, etc. But the real benefit is that `pip`, `conda`, `poetry`, etc. have all given me a variety of pains which `uv` has completely solved. If you haven't yet installed `uv`, you can [**find instructions to install `uv` here**](https://docs.astral.sh/uv/getting-started/installation/).

`uv` uses `pyproject.toml`, so `uv` is not *necessarily* required. But I'll provide only `uv` commands.

This project is implemented in a [*Jupyter Notebook*](https://jupyter.org/), which is a web interface for . This is *the* tool for the job when the job requires rapid, iterative prototyping like this assignment. As a bonus, Jupyter supports mixing cells of code with cells of Markdown (+ LaTeX, etc).

Without further ado, to run this on your machine:

To **open the Jupyter notebook**:

```sh
uv sync
uv run --with jupyter jupyter lab
```

There are two Jupyter notebooks, `main_rough_draft.ipynb` which contains stream-of-consciousness iterative development, and `main.ipynb` which is the nearly-completed script

To **run the `main.py`**:

```sh
gzip -c -d 2026-02-01_anthem_index.json.gz > anthem_index.json
# this is unzipped as part of the ipynb 
uv sync
uv run main.py
```

---

# Pre-development timeline

> **tldr**: Interview on Wednesday, looked closer at the assignment on Saturday, and I frontloaded this README on Monday morning.

I had a short interview with Salman on Wednesday, February 4th. This was a busy week for me, and anticipating a much larger take-home assignment, I intended to start work on it on Saturday.

I took a look at these instructions on Saturday February 7th, and so I had time to let it 'marinate' in my head a bit. But seeing that it was intended to be completed in a ~two hour block, I decided instead to complete it in one fell swoop on Monday.

Before starting the actual development, I wrote some of this README first thing in the morning, before starting development and getting to the other activities of the day.

# Development timeline

> **tldr**:

- ~06:30 ET - Woke up, wrote most of this README

- ~13:45 ET - Set a timer, started development of solution.

    - I like to write and be verbose, so I'm writing my thoughts out a *lot* using the 2h max.

- ~15:40 ET - `main.ipynb` notebook running. It finishes in 405 seconds

I paused the timer for ~15 minutes for a coffee break :)

---

# LLM thoughts and notes

> **tldr**: Agentic code generation makes no sense here. Using LLMs to augment internet searches, StackOverflow, etc. does make sense, though.

## No 'vibe coding', because it doesn't make sense here.

> **tldr**: Not necessarily against using generated code, but 'vibe coding' and completion would just slow me down here, and I want to be able to explain the code when asked in the future.

There's kind of a storm of LLM usage going on. I spent four years in a PhD program doing deep learning, and so I have reservations  about this embrace of vibe-coding. What follows is not an exhaustive treatise on my thoughts, though.

There are responsible and useful ways to use LLMs agentically with a *positive* impact on code quality and software engineering rigor, so I'm not against them wholesale! But it's not the right tool for the job *here*. The fastest way to get this done correctly is to write it by hand, and that would still be true even if the purpose of this was not to show off my skills and thinking.

Further, I find it *easy* to navigate code I wrote myself (even if I forget ever writing it), while generated code is *harder* to navigate than code written by other humans. If the code for this project were something I were maintaining, I would benefit from writing it by hand.

I am also generally against using LLMs to write any text meant for human consumption, (except for reasons like translation, or OCR, transcribing, image description, etc.) So, all of this text is written by hand.

I'm someone who has been writing Markdown for years, and I am  a big fan of lists, summaries, and the Table-of-Contents-as-summary (as seen in [this 2015 SEC report on the Equifax breach](https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/FINAL%20Equifax%20Report.pdf) of all things.) The result is that I think my writing looks a lot like AI, and so I feel motivated to write this diatribe.

## ChatGPT transcription

All that said, I have had many times where an LLM could surface an answer faster than internet searching, StackExchange, or reading documentation could. I take this with a grain of salt, since I've also been provided obviously insecure configurations, etc. in generated responses. (I benefit a lot from seeing the discussion and whatnot, so I am increasingly worried as StackExchange dies and the material there slowly becomes irrelevant!)

This is increasingly muddled as DuckDuckGo and others surface LLM-generated responses to searches anyways. For example, a DDG search for "python large json chunking" yields a generated response [similar to the top StackOverflow post on the matter recommending `pandas`](https://stackoverflow.com/questions/10238340/whats-the-best-way-to-load-large-json-lists-in-python#47561314), but omits the lower-score *accepted* answer (proposing `json`) and commentary recommending `ijson`.

In the interest of transparency, I'll provide the transcription of my LLM of choice, which is currently ChatGPT for no particular reason.

The transcript is here: https://chatgpt.com/share/698a4753-08e0-8002-8594-64de9cc16784



# Development notes

Writing this while the notebook runs:

1. I feel uncertain about my inclusion principle for what URLs do or do not correspond to Anthem PPO. Most of my healthcare experience is working with PHI data and internal contracting. If I had more time, I'd re-assess

2. I do feel confident that my general
