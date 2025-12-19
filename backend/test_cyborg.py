from services.cyborg import get_cyborg_service
import traceback

def test_service():
    print("Initializing Service...")
    try:
        service = get_cyborg_service()
        print("Service Initialized.")
        
        print("Testing Register User...")
        try:
            service.register_user("test@example.com", "test@example.com", "hash123", "Test User")
            print("Register Success.")
        except Exception as e:
            print(f"Register Failed: {e}")
            traceback.print_exc()

    except Exception as e:
        print(f"Service Init Failed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    test_service()
