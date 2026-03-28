#!/usr/bin/env python3
"""lorem_ipsum2 - Lorem ipsum and alternative placeholder text."""
import sys, random
LATIN="lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()
HIPSTER="artisan craft beer aesthetic vegan kombucha sustainable ethical locally sourced organic fair trade biodegradable minimalist curated bespoke handcrafted small batch cold pressed farm to table gluten free paleo keto mindful intentional slow living hygge wabi sabi kinfolk".split()
TECH="kubernetes docker microservice serverless blockchain api endpoint webhook pipeline container orchestration deployment scaling monitoring observability terraform ansible grafana prometheus redis kafka postgres nginx load balancer cdn".split()
def sentence(words, min_w=5, max_w=15):
    n=random.randint(min_w,max_w); s=" ".join(random.choices(words,k=n))
    return s[0].upper()+s[1:]+"."
def paragraph(words, min_s=3, max_s=6):
    return " ".join(sentence(words) for _ in range(random.randint(min_s,max_s)))
if __name__=="__main__":
    style=sys.argv[1] if len(sys.argv)>1 else "latin"
    n=int(sys.argv[2]) if len(sys.argv)>2 else 3
    words={"latin":LATIN,"hipster":HIPSTER,"tech":TECH}.get(style,LATIN)
    mode=sys.argv[3] if len(sys.argv)>3 else "paragraphs"
    if mode.startswith("w"): print(" ".join(random.choices(words,k=n)))
    elif mode.startswith("s"): print(" ".join(sentence(words) for _ in range(n)))
    else: print("\n\n".join(paragraph(words) for _ in range(n)))
