# Novel2Script YAML Schema Design

## Design Goals

This schema is designed for AI-generated screenplay drafts.

The goals are:

1. Human-readable
2. Easy to edit
3. Structured screenplay format
4. Compatible with AI generation
5. Easy to extend

---

## Top-Level Structure

```yaml
title:
genre:
characters:
scenes:
```

---

## Character Schema

```yaml
characters:
  - name:
    role:
    description:
```

### Description

- name: character name
- role: protagonist, antagonist, supporting role
- description: brief character introduction

---

## Scene Schema

```yaml
scenes:
  - scene_id:
    location:
    time:
    summary:
    actions:
    dialogues:
```

### Description

- scene_id: unique scene identifier
- location: scene location
- time: morning, afternoon, night
- summary: short scene description
- actions: character actions
- dialogues: dialogue list

---

## Dialogue Schema

```yaml
dialogues:
  - speaker:
    content:
    emotion:
```

### Description

- speaker: character name
- content: dialogue content
- emotion: emotional state

---

## Example

```yaml
title: Night Meeting

characters:
  - name: Lin Ran
    role: protagonist

scenes:
  - scene_id: 1

    location: Street

    time: Night

    summary: Lin Ran waits for the target

    dialogues:
      - speaker: Lin Ran
        content: They are coming.
        emotion: nervous
```

---

## Design Rationale

Compared with JSON, YAML is easier for writers to read and modify.

The scene-based structure follows standard screenplay workflows.

The schema can be expanded in the future without breaking compatibility.
