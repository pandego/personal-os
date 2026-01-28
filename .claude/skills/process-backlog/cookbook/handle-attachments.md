# Cookbook: Handle Attachments

Safely process Todoist tasks that contain images, files, or other attachments by downloading locally and extracting content.

**Principle:** ALWAYS download and analyze attachments BEFORE modifying tasks. Extract all useful content and save it to the task.

---

## When to Use

Dispatch here from `sync.md` when a task has:
- Image attachments (screenshots, photos)
- File attachments (PDFs, documents)
- Any `fileAttachment` in task comments

---

## Detection

When fetching tasks, check comments for attachments:

```
Use mcp__claude_ai_todoist__find-comments with taskId
```

**Attachment present if:**
- Response contains `fileAttachment` object
- `fileAttachment.resourceType` is "image", "file", etc.

---

## Workflow

### 1. Create Temp Directory

Ensure `./tmp/` exists in repository root:

```bash
mkdir -p ./tmp
```

**Note:** `./tmp/` should be in `.gitignore`

### 2. Download Attachment

Use curl to download the file locally:

```bash
curl -L -o ./tmp/{filename} "{fileUrl}"
```

- Use `-L` to follow redirects (Todoist CDN redirects)
- Preserve original filename from `fileAttachment.fileName`
- If auth required, inform user to download manually

### 3. Analyze Content

Use the Read tool to analyze the downloaded image:

```
Read ./tmp/{filename}
```

**For images, identify:**
- Is it a screenshot of a tweet/post? → Extract the text, author, date
- Is it a diagram/chart? → Describe what it shows
- Is it a photo? → Describe relevant details
- Is it a document screenshot? → Extract key text

### 4. Extract and Format Content

Based on content type, create structured extraction:

**For tweet/social post screenshots:**
```markdown
**Original post extracted from image:**
- Author: @username
- Platform: Twitter/LinkedIn/etc.
- Content: "[exact text of the post]"
- Engagement: [likes, retweets if visible]
- Date: [if visible]

**Source image saved:** ./tmp/{filename}
```

**For other images:**
```markdown
**Image content:**
[Description of what the image contains]

**Source image saved:** ./tmp/{filename}
```

### 5. Update Task with Extracted Content

Use `mcp__claude_ai_todoist__update-tasks` to add extracted content to description:

```
Update task description to include:
1. Original description (if any)
2. Extracted content from attachment
3. Reference to local file path
```

**Or** add as a comment using `mcp__claude_ai_todoist__add-comments`:

```
Add comment with extracted content to preserve original description
```

### 6. Safe to Process

Only AFTER content is extracted and saved to the task:
- Task can be moved between sections
- Task can be reformatted for DoR
- Original attachment URL preserved as reference

---

## File Organization

```
./tmp/
├── todoist-{taskId}-{filename}    # Downloaded attachments
└── ...
```

Use task ID in filename to track origin.

---

## Example Flow

**Input:** Task "Check this out… nice LinkedIn / twitter post" with image attachment

**Step 1:** Detect attachment
```json
{
  "fileAttachment": {
    "resourceType": "image",
    "fileName": "image.png",
    "fileUrl": "https://files.todoist.com/...",
    "imageWidth": 1170,
    "imageHeight": 2532
  }
}
```

**Step 2:** Download
```bash
curl -L -o ./tmp/todoist-6frJ3GHw2gj2JPvg-image.png "https://files.todoist.com/..."
```

**Step 3:** Analyze with Read tool
```
Read ./tmp/todoist-6frJ3GHw2gj2JPvg-image.png
```
→ "This is a screenshot of a tweet by @username saying '...'"

**Step 4:** Update task description
```
Original post extracted from image:
- Author: @elonmusk
- Platform: Twitter
- Content: "The best code is no code at all"
- Likes: 42K

Source image: ./tmp/todoist-6frJ3GHw2gj2JPvg-image.png
```

**Step 5:** Now safe to process/move task

---

## Error Handling

| Error | Action |
|-------|--------|
| Download fails (401/403) | Ask user to manually download to ./tmp/ |
| Image unreadable | Preserve URL and filename, ask user to describe |
| Content unclear | Preserve URL, add note "image content unclear" |

**NEVER proceed with task deletion if attachment content was not preserved.**

---

## Anti-Patterns

### DO NOT:
- Delete tasks before downloading and analyzing attachments
- Skip attachment processing to save time
- Assume you'll be able to access the URL later
- Rely solely on the URL without local backup

### DO:
- Always download to ./tmp/ first
- Extract ALL text content from screenshots
- Update the task with extracted content before any modifications
- Keep the local file as backup
