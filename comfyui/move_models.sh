#!/bin/bash

SOURCE="./models"
DEST="./ComfyUI/models"

shopt -s dotglob nullglob

for dir in "$SOURCE"/*; do
    if [ -d "$dir" ]; then
        folder_name=$(basename "$dir")

        if [ -d "$DEST/$folder_name" ]; then
            for file in "$dir"/*; do
                filename=$(basename "$file")

                # Only move if file does NOT already exist
                if [ ! -e "$DEST/$folder_name/$filename" ]; then
                    mv "$file" "$DEST/$folder_name/"
                    echo "Moved: $folder_name/$filename"
                # else
                #     echo "Skipped (exists): $folder_name/$filename"
                fi
            done
        else
            echo "Skipping $folder_name (no matching folder in destination)"
        fi
    fi
done