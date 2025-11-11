from app.__main__ import app


def main():
    try:
        from granian import Granian

        server = Granian(
            "app.__main__:app",
            interface="asgi",
        )

        if hasattr(server, "serve"):
            server.serve()
        else:
            raise RuntimeError("Granian has no serve() in this version")

    except Exception as exc:
        print(f"Granian is not available or incompatible: {exc}")
        import uvicorn

        uvicorn.run("app.__main__:app", host="0.0.0.0", port=5000, reload=True)


if __name__ == "__main__":
    main()
