name: Build Release AAB

on:
  workflow_dispatch:

jobs:
  build-release-aab:
    name: Build Signed Release AAB
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Java 17
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Confirm Java version
        run: |
          java -version
          echo "JAVA_HOME=$JAVA_HOME"

      - name: Install Linux dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git \
            zip \
            unzip \
            python3 \
            python3-pip \
            python3-setuptools \
            python3-wheel \
            autoconf \
            automake \
            libtool \
            pkg-config \
            zlib1g-dev \
            libncurses5-dev \
            libncursesw5-dev \
            libtinfo5 \
            cmake \
            libffi-dev \
            libssl-dev \
            build-essential

      - name: Install Buildozer tools
        run: |
          python3 -m pip install --upgrade pip
          python3 -m pip install --upgrade buildozer cython virtualenv

      - name: Verify project files and Android settings
        run: |
          pwd
          ls -la
          test -f main.py
          test -f buildozer.spec
          grep -n "android.api\|android.minapi\|android.ndk_api\|p4a.ndk_api\|android.ndk\|android.archs\|android.release_artifact" buildozer.spec

      - name: Decode release keystore
        env:
          ANDROID_KEYSTORE_BASE64: ${{ secrets.ANDROID_KEYSTORE_BASE64 }}
        run: |
          if [ -z "$ANDROID_KEYSTORE_BASE64" ]; then
            echo "Missing GitHub secret ANDROID_KEYSTORE_BASE64"
            exit 1
          fi
          echo "$ANDROID_KEYSTORE_BASE64" | base64 --decode > release.keystore
          ls -la release.keystore

      - name: Inject signing settings
        env:
          KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}
        run: |
          if [ -z "$KEYSTORE_PASSWORD" ] || [ -z "$KEY_ALIAS" ] || [ -z "$KEY_PASSWORD" ]; then
            echo "Missing one or more signing secrets: KEYSTORE_PASSWORD, KEY_ALIAS, KEY_PASSWORD"
            exit 1
          fi
          python3 - <<'PY'
          from pathlib import Path
          import os

          path = Path("buildozer.spec")
          text = path.read_text()
          replacements = {
              "android.release_keystore": "./release.keystore",
              "android.release_keyalias": os.environ["KEY_ALIAS"],
              "android.release_storepass": os.environ["KEYSTORE_PASSWORD"],
              "android.release_keypass": os.environ["KEY_PASSWORD"],
          }

          lines = []
          found = set()
          for line in text.splitlines():
              stripped = line.strip()
              replaced = False
              for key, value in replacements.items():
                  if stripped.startswith(key + " ="):
                      lines.append(f"{key} = {value}")
                      found.add(key)
                      replaced = True
                      break
              if not replaced:
                  lines.append(line)

          missing = [key for key in replacements if key not in found]
          if missing:
              raise SystemExit(f"Missing signing keys in buildozer.spec: {missing}")

          path.write_text("\n".join(lines) + "\n")
          PY
          grep -n "android.release_keystore\|android.release_keyalias\|android.release_artifact" buildozer.spec

      - name: Hard clean old Buildozer cache
        run: |
          rm -rf .buildozer
          rm -rf bin
          rm -rf ~/.buildozer

      - name: Build signed release AAB
        run: |
          buildozer -v android release

      - name: List output
        run: |
          find bin -type f -print

      - name: Upload release artifact
        uses: actions/upload-artifact@v4
        with:
          name: jester-king-gm-simulator-release
          path: |
            bin/*.aab
            bin/*.apk
          if-no-files-found: error
