# fastapi-kickstart-guide
A repository which contains beautiful notes and steps which can help beginners of FastAPI to kickstart with the FastAPI very faster. It contains bunch of beautiful examples, learning notes, references etc. Images have been attached too. The README.md will help any newbies to FastAPI learn the things faster and better.

# Cloning Github project and dependencies installation in the virtualenv

```bash
ip-172-16-0-62:prod hygull$ git clone https://github.com/hygull/fastapi-kickstart-guide.git
Cloning into 'fastapi-kickstart-guide'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (5/5), done.
ip-172-16-0-62:prod hygull$ 
```

```bash
ip-172-16-0-62:prod hygull$ cd fastapi-kickstart-guide/
ip-172-16-0-62:fastapi-kickstart-guide hygull$ 
```

```
ip-172-16-0-62:fastapi-kickstart-guide hygull$ python3.11 -m virtualenv ../venv-fastapi-kickstart
created virtual environment CPython3.11.2.final.0-64 in 588ms
  creator CPython3Posix(dest=/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/prod/venv-fastapi-kickstart, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/hygull/Library/Application Support/virtualenv)
    added seed packages: pip==23.3.2, setuptools==69.0.3, wheel==0.42.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
ip-172-16-0-62:fastapi-kickstart-guide hygull$ 
ip-172-16-0-62:fastapi-kickstart-guide hygull$ source ../venv-fastapi-kickstart/bin/activate
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ 
```

```bash
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ pip install uvicorn fastapi
Collecting uvicorn
  Using cached uvicorn-0.25.0-py3-none-any.whl.metadata (6.4 kB)
Collecting fastapi
  Using cached fastapi-0.108.0-py3-none-any.whl.metadata (24 kB)
Collecting click>=7.0 (from uvicorn)
  Using cached click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting h11>=0.8 (from uvicorn)
  Using cached h11-0.14.0-py3-none-any.whl (58 kB)
Collecting pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 (from fastapi)
  Using cached pydantic-2.5.3-py3-none-any.whl.metadata (65 kB)
Collecting starlette<0.33.0,>=0.29.0 (from fastapi)
  Using cached starlette-0.32.0.post1-py3-none-any.whl.metadata (5.8 kB)
Collecting typing-extensions>=4.8.0 (from fastapi)
  Using cached typing_extensions-4.9.0-py3-none-any.whl.metadata (3.0 kB)
Collecting annotated-types>=0.4.0 (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi)
  Using cached annotated_types-0.6.0-py3-none-any.whl.metadata (12 kB)
Collecting pydantic-core==2.14.6 (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi)
  Using cached pydantic_core-2.14.6-cp311-cp311-macosx_10_7_x86_64.whl.metadata (6.5 kB)
Collecting anyio<5,>=3.4.0 (from starlette<0.33.0,>=0.29.0->fastapi)
  Using cached anyio-4.2.0-py3-none-any.whl.metadata (4.6 kB)
Collecting idna>=2.8 (from anyio<5,>=3.4.0->starlette<0.33.0,>=0.29.0->fastapi)
  Using cached idna-3.6-py3-none-any.whl.metadata (9.9 kB)
Collecting sniffio>=1.1 (from anyio<5,>=3.4.0->starlette<0.33.0,>=0.29.0->fastapi)
  Using cached sniffio-1.3.0-py3-none-any.whl (10 kB)
Using cached uvicorn-0.25.0-py3-none-any.whl (60 kB)
Using cached fastapi-0.108.0-py3-none-any.whl (92 kB)
Using cached click-8.1.7-py3-none-any.whl (97 kB)
Using cached pydantic-2.5.3-py3-none-any.whl (381 kB)
Using cached pydantic_core-2.14.6-cp311-cp311-macosx_10_7_x86_64.whl (1.9 MB)
Using cached starlette-0.32.0.post1-py3-none-any.whl (70 kB)
Using cached typing_extensions-4.9.0-py3-none-any.whl (32 kB)
Using cached annotated_types-0.6.0-py3-none-any.whl (12 kB)
Using cached anyio-4.2.0-py3-none-any.whl (85 kB)
Using cached idna-3.6-py3-none-any.whl (61 kB)
Installing collected packages: typing-extensions, sniffio, idna, h11, click, annotated-types, uvicorn, pydantic-core, anyio, starlette, pydantic, fastapi
Successfully installed annotated-types-0.6.0 anyio-4.2.0 click-8.1.7 fastapi-0.108.0 h11-0.14.0 idna-3.6 pydantic-2.5.3 pydantic-core-2.14.6 sniffio-1.3.0 starlette-0.32.0.post1 typing-extensions-4.9.0 uvicorn-0.25.0
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ 
```

```
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ ls
LICENSE		README.md
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ pip freeze > requirements.txt
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ 
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ ls
LICENSE			README.md		requirements.txt
(venv-fastapi-kickstart) ip-172-16-0-62:fastapi-kickstart-guide hygull$ 
```