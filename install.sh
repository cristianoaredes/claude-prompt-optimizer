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

# 4. Clean up any old plugin registration that causes marketplace errors
python3 <<PY
import json, os

# Remove from installed_plugins.json to avoid "not found in marketplace" errors
inst_path = os.path.expanduser("$INSTALLED_PLUGINS")
if os.path.exists(inst_path):
    with open(inst_path, "r") as f:
        data = json.load(f)
    data.get("plugins", {}).pop("$PLUGIN_NAME@$PLUGIN_NAME", None)
    with open(inst_path, "w") as f:
        json.dump(data, f, indent=2)

# Remove from settings.json enabledPlugins
settings_path = os.path.expanduser("$SETTINGS")
if os.path.exists(settings_path):
    with open(settings_path, "r") as f:
        data = json.load(f)
    data.get("enabledPlugins", {}).pop("$PLUGIN_NAME@$PLUGIN_NAME", None)
    with open(settings_path, "w") as f:
        json.dump(data, f, indent=2)
PY

echo "✅ $PLUGIN_NAME v$VERSION installed successfully!"
echo ""
echo "📝 Available commands:"
echo "  /build /chain /debug /env /flags /inject /mode /pipeline"
echo "  /refactor /sharpen /super /swarm /tune /verify /yolo"
echo ""
echo "🔄 Restart Claude Code to load commands:"
echo "  exit && claude"
