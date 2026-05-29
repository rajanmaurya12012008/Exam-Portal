from auth import register, login, update_score
from quiz import take_exam


def main():
    """Main function to run the exam system"""
    while True:
        print("\n===== Exam Portal =====")
        print("1. register")
        print("2. login")
        print("3. exit")
        
        choice = input("choose option: ")
        
        if choice == "1":
            res = register()
            uid, email, pw = res
            
            print()
            print("--- Registration Successful ---")
            print("User ID:", uid)
            print("1. Take Exam")
            print("2. Go to Main Menu")
            ex_ch = input("choose option: ")
            
            if ex_ch == "1":
                print("Starting exam...")
                sc, tot = take_exam()
                print(f"\n--- Your Score: {sc} / {tot} ---")
                
                # Save score
                update_score(uid, sc, tot)
                print(" Score saved!")
            
            print()
            
        elif choice == "2":
            print("Logging in...")
            res = login()
            uid, sc, tot = res
            
            if uid:
                print(f"\nWelcome! Your last score: {sc} / {tot}")
                
                print("\n1. Start exam")
                print("2. exit")
                ex_ch = input("choose option: ")
                
                if ex_ch == "1":
                    print("starting exam...")
                    new_sc, new_tot = take_exam()
                    
                    # Update score
                    update_score(uid, new_sc, new_tot)
                    print(f"\n✓ Score updated! New Score: {new_sc} / {new_tot}")
                else:
                    print("exiting")
            else:
                print("login failed.")
            
            print()
            
        elif choice == "3":
            print("thank you and goodbye!")
            break
        else:
            print("invalid choice.")


if __name__ == "__main__":
    main()