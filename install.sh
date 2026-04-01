#!/usr/bin/env bash
set -e

PLUGIN_NAME="prompt-optimizer"
VERSION="2.0.0"
CACHE_DIR="$HOME/.claude/plugins/cache/$PLUGIN_NAME/$PLUGIN_NAME/$VERSION"
COMMANDS_DIR="$HOME/.claude/.claude/commands"
INSTALLED_PLUGINS="$HOME/.claude/plugins/installed_plugins.json"
SETTINGS="$HOME/.claude/settings.json"

echo "🚀 Installing $PLUGIN_NAME v$VERSION..."

# 1. Clean previous installations
rm -rf "$HOME/.claude/plugins/cache/$PLUGIN_NAME"
rm -f "$COMMANDS_DIR"/build.md "$COMMANDS_DIR"/chain.md "$COMMANDS_DIR"/debug.md \
  "$COMMANDS_DIR"/env.md "$COMMANDS_DIR"/flags.md "$COMMANDS_DIR"/inject.md \
  "$COMMANDS_DIR"/mode.md "$COMMANDS_DIR"/pipeline.md "$COMMANDS_DIR"/refactor.md \
  "$COMMANDS_DIR"/sharpen.md "$COMMANDS_DIR"/super.md "$COMMANDS_DIR"/swarm.md \
  "$COMMANDS_DIR"/tune.md "$COMMANDS_DIR"/verify.md "$COMMANDS_DIR"/yolo.md

# 2. Copy plugin to Claude Code cache
mkdir -p "$CACHE_DIR"
cp -R "$(dirname "$0")"/* "$CACHE_DIR/"

# 3. Symlink commands to user commands directory
mkdir -p "$COMMANDS_DIR"
for cmd in "$CACHE_DIR"/commands/*.md; do
  ln -s "$cmd" "$COMMANDS_DIR/$(basename "$cmd")"
done

# 4. Register in installed_plugins.json
python3 <<PY
import json, os

path = os.path.expanduser("$INSTALLED_PLUGINS")
with open(path, "r") as f:
    data = json.load(f)

data.setdefault("plugins", {})["$PLUGIN_NAME@$PLUGIN_NAME"] = [
    {
        "scope": "user",
        "installPath": "$CACHE_DIR",
        "version": "$VERSION",
        "installedAt": "2026-04-01T00:00:00.000Z",
        "lastUpdated": "2026-04-01T00:00:00.000Z"
    }
]

with open(path, "w") as f:
    json.dump(data, f, indent=2)
PY

# 5. Enable in settings.json
python3 <<PY
import json, os

path = os.path.expanduser("$SETTINGS")
with open(path, "r") as f:
    data = json.load(f)

data.setdefault("enabledPlugins", {})["$PLUGIN_NAME@$PLUGIN_NAME"] = True

# Remove any broken marketplace entries if they exist
if "extraKnownMarketplaces" in data:
    data["extraKnownMarketplaces"].pop("$PLUGIN_NAME", None)
    if not data["extraKnownMarketplaces"]:
        del data["extraKnownMarketplaces"]

with open(path, "w") as f:
    json.dump(data, f, indent=2)
PY

echo "✅ $PLUGIN_NAME v$VERSION installed successfully!"
echo ""
echo "📝 Available commands:"
echo "  /build /chain /debug /env /flags /inject /mode /pipeline"
echo "  /refactor /sharpen /super /swarm /tune /verify /yolo"
echo ""
echo "🪝 Active hooks:"
echo "  SessionStart + PostToolUse"
echo ""
echo "🔄 Restart Claude Code to load everything:"
echo "  exit && claude"
