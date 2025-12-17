import inspect
try:
    from cyborgdb import Client
    print("Found cyborgdb.Client")
    sig = inspect.signature(Client.__init__)
    print(f"Signature: {sig}")
    print(f"Docstring: {Client.__doc__}")
    print(f"Attributes: {dir(Client)}")
except Exception as e:
    print(f"Error inspecting: {e}")
