[README.txt](https://github.com/user-attachments/files/29830288/README.txt)
# Jester King Market Lord Android

This was converted from the uploaded Tkinter Python version into a Kivy Android project.

## Files

- main.py
- buildozer.spec
- .github/workflows/build-android.yml

## How to build the APK with GitHub

1. Create a new GitHub repo.
2. Upload these files to the root of the repo.
3. Go to Actions.
4. Run the Build Android APK workflow.
5. Download the APK from the workflow artifacts.

## How to build locally on Linux or WSL

```bash
pip install buildozer
buildozer android debug
```

The APK appears in the bin folder.
