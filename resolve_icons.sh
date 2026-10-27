cd KDE/breeze-icons

find . -type l | while read -r link; do
  if [ -e "$link" ]; then
    target=$(readlink -f "$link")
    
    rm "$link"
    
    cp -rP "$target" "$link"
  else
    echo "Broken link: $link"
  fi
done
