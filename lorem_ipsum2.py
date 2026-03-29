#!/usr/bin/env python3
"""lorem_ipsum2 - Structured placeholder text."""
import sys,argparse,json,random
W="lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris".split()
def sentence(mn=5,mx=15):
    n=random.randint(mn,mx);s=" ".join(random.choice(W) for _ in range(n));return s[0].upper()+s[1:]+"."
def paragraph(s=4):return " ".join(sentence() for _ in range(s))
def bullet_list(n=5):return "\n".join(f"- {sentence(3,8)}" for _ in range(n))
def main():
    p=argparse.ArgumentParser(description="Lorem ipsum generator")
    p.add_argument("--paragraphs",type=int,default=0)
    p.add_argument("--sentences",type=int,default=0)
    p.add_argument("--list",type=int,default=0)
    p.add_argument("--heading",action="store_true")
    args=p.parse_args()
    parts=[]
    if args.heading:parts.append("# "+sentence(2,5).rstrip("."))
    if args.paragraphs:parts.extend(paragraph() for _ in range(args.paragraphs))
    if args.sentences:parts.append(" ".join(sentence() for _ in range(args.sentences)))
    if args.list:parts.append(bullet_list(args.list))
    if not parts:parts.append(paragraph(3))
    print("\n\n".join(parts))
if __name__=="__main__":main()
