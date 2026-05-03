 Friendship Compatibility Index (Bestie Meter)

A simple and fun Python GUI project that calculates compatibility between two users based on their answers to personal preference questions.



  Description

This application allows two users to answer a set of questions one by one. After collecting responses from both users, the program compares their answers and calculates a compatibility percentage.

Based on the result, a message is displayed indicating how well the two users match.


 Features

* Two-user interactive system
* Custom name input
* Turn-based question answering
* Automatic compatibility calculation
* Result displayed with percentage and message
* Simple and colorful GUI using Tkinter



  Built With

* Python 3
* Tkinter (built-in GUI library)



 How to Run

1. Install Python (if not already installed)
2. Download or clone this repository
3. Run the file:

```bash
python friendship_compatibility.py
```

  How It Works

* Both users answer the same 5 questions
* Answers are compared one by one
* Matching answers increase the score
* Compatibility is calculated using:


Compatibility (%) = (Matching Answers / Total Questions) × 100
```



  Result Criteria

* **80% and above** → ❤️ Highly compatible
* **50% to 79%** → 😊 Moderately compatible
* **Below 50%** → 💔 Not compatible



  Limitations

* Exact answer matching only
* No support for similar words (e.g., "coffee" ≠ "cafe")
* Fixed set of questions


  Future Improvements

* Add multiple choice buttons instead of text input
* Improve answer matching using smarter logic
* Enhance UI design with better styling
* Add animations or sound effects
* Save previous results



  File Structure

```
friendship_compatibility.py
README.md
```



 Authors
Marium Bint-e- Tahir\n
Maria

---

 📜 License

This project is open-source and free to use for educational purposes.
