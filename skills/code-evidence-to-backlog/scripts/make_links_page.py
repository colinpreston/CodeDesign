"""Write '_Open files.html' into a project folder: a local page linking every file and folder.
Office files open in the desktop app (ms-excel/ms-word/ms-powerpoint :ofe|u| + SharePoint URL);
other files and folders use relative links (folders show as a list; browsers can't open Finder).
Usage (run on the user's device, inside the project folder):
  python3 make_links_page.py "https://<tenant>-my.sharepoint.com/personal/<user>/Documents/<path to project folder>/"
Find the SharePoint base by grepping the project's Office files:
  unzip -p file.xlsx | grep -aoE 'https://[a-z0-9-]+\\.sharepoint\\.com/personal/[a-z_]+'
"""
import os,sys,html,urllib.parse,datetime
SP=sys.argv[1].rstrip("/")+"/" if len(sys.argv)>1 else ""
APPS={"xlsx":("ms-excel","Excel"),"xlsm":("ms-excel","Excel"),"xls":("ms-excel","Excel"),"docx":("ms-word","Word"),"doc":("ms-word","Word"),"pptx":("ms-powerpoint","PowerPoint"),"ppt":("ms-powerpoint","PowerPoint")}
enc=lambda p:"/".join(urllib.parse.quote(x) for x in p.split("/"))
skip=lambda n:n.startswith(".") or n.startswith("~$") or n=="_Open files.html"
def flink(rel):
    ext=rel.rsplit(".",1)[-1].lower() if "." in rel else "";name=html.escape(os.path.basename(rel))
    if SP and ext in APPS:a=APPS[ext];return f'<a href="{a[0]}:ofe|u|{SP}{enc(rel)}">{name}</a> <span class="t">opens in {a[1]}</span>'
    return f'<a href="{enc(rel)}">{name}</a>'
def walk(d):
    rows=[]
    for n in sorted(os.listdir(d)):
        if skip(n):continue
        p=os.path.join(d,n);rel=os.path.relpath(p,".")
        if os.path.isdir(p):inner=walk(p);rows.append(f'<li class="d"><a href="{enc(rel)}/">📂 {html.escape(n)}</a>'+(f"<ul>{inner}</ul>" if inner else ' <span class="t">empty</span>')+"</li>")
        else:rows.append(f"<li>📄 {flink(rel)}</li>")
    return "".join(rows)
title=os.path.basename(os.getcwd())
secs="".join(f'<section><h2><a href="{enc(s)}/">{html.escape(s)}</a></h2><ul>{walk(s)}</ul></section>' for s in sorted(os.listdir(".")) if os.path.isdir(s) and not skip(s))
top="".join(f"<li>📄 {flink(n)}</li>" for n in sorted(os.listdir(".")) if os.path.isfile(n) and not skip(n))
css="body{font:14px/1.5 -apple-system,Segoe UI,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;color:#1d1d3a;background:#F3F4F6}h1{font-size:20px;color:#000050}h2{font-size:16px;margin:0 0 6px}section{background:#fff;border:1px solid #DDE1E6;border-radius:12px;padding:12px 16px;margin:12px 0}ul{list-style:none;padding-left:16px;margin:2px 0}a{color:#3D3DFF}.t{color:#777;font-size:12px}li.d>a{font-weight:600;color:#000050}"
open("_Open files.html","w").write(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}: open files</title><style>{css}</style></head><body><h1>{html.escape(title)}: open files</h1><p class="t">Office files open in the desktop app. PDFs and notes open here. Folders show their files as a list (a browser can\'t open Finder). Updated {datetime.date.today():%d %b %Y} by Claude.</p>'+(f"<section><ul>{top}</ul></section>" if top else "")+secs+"</body></html>")
print("wrote _Open files.html")
