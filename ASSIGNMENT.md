# FastAPI Assignment — *CineHub*

**Repository:** [https://github.com/mikhail2574/sdt-208-6-fastapi-core](https://github.com/mikhail2574/sdt-208-6-fastapi-core)

## How to run

```bash
pip install -r requirements.txt
./run.sh
# visit: http://127.0.0.1:8000/hello  and  http://127.0.0.1:8000/docs
```

---

## Part 1. Basic App and Hello Route (5 pts.)

**Demonstration**

**Part 1. Screenshots:**  
![Part1](screenshots/part1_hello.png)

---

## Part 2. Path and Query Parameters (5 pts.)

- `GET /greet/{name}` → `"Hello, {name}!"`  
- `GET /square?number=4` → `16`

**Part 2.1. Screenshots:**  
![Greet](screenshots/part2_greet.png)

**Part 2.2. Screenshots:**  
![Square](screenshots/part2_square.png)  
![SquareInvalid](screenshots/part2_square_invalid.png)

---

## Part 3. Create & Update Domain Objects with Pydantic Validation (10 pts.)

Domain: **Movies** (`title`, `rating`, `year`, optional `description`).

**Part 3. Screenshots:**  
![POST](screenshots/part3_post_ok.png)  
![POST Invalid](screenshots/part3_post_invalid.png)  
![PUT](screenshots/part3_put_ok.png)  
![PUT Invalid](screenshots/part3_put_invalid.png)

---

## Part 4. Routers (5 pts.)

Routers used: **Basics & Params**, **Health**, **Info**, **Movies**, **Movies HTML**, **Security**.  
Visible separation in `/docs` via tags.

**Part 4. Screenshots:**  
![OpenAPI Paths](screenshots/part4_paths.png)

---

## Part 5. Retrieve with Validation & Error Handling (10 pts.)

- `GET /movies` → active movies  
- `GET /movies/{id}` → 400/404/410 path validation & status codes  
- `DELETE /movies/{id}` → soft-delete via `archived=True`

**Part 5. Screenshots:**  
![List](screenshots/part5_list.png)  
![Get OK](screenshots/part5_get_ok.png)  
![Get 404](screenshots/part5_get_404.png)  
![Get 400](screenshots/part5_get_400.png)  
![Get 410](screenshots/part5_get_410.png)  
![Delete 204](screenshots/part5_delete_204.png)  
![Delete 410](screenshots/part5_delete_410.png)

---

## Part 6. HTML Templates (10 pts.)

Jinja2 with `templates/` and static files.  
- `GET /movies/html`
- `GET /movies/{id}/html`

**Part 6. Screenshots:**  
![HTML list](screenshots/part6_html_list.png)  
![HTML detail](screenshots/part6_html_detail.png)

---

## Part 7. Dependency Injection & Security (10 pts.)

Token: `letmein`. Pass via header `X-Token` or query `?token=`.

**Part 7. Screenshots:**  
![401](screenshots/part7_401.png)  
![200](screenshots/part7_200.png)  
![Secure Router](screenshots/part7_router.png)

---

### Notes

- Python modules are named according to the project and task numbers: `cinehub_part2_params.py`, `cinehub_part3_models.py`, etc.
- Input/output schemas for POST/PUT are distinct (`MovieCreate`, `MovieUpdate`, `MovieOut`).
- Validation is enforced via Pydantic `Field` constraints and FastAPI type hints.
