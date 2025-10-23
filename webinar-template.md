<!--
WEBINAR TEMPLATE

Instructions:
1. Copy this file to docs/webinars/[webinar-slug].en.md
2. Fill in all the empty values in the front matter
3. Add the webinar to the navigation in mkdocs.yml
4. Delete this comment block

Required fields:
- title: Display name of the webinar
- date: When the webinar was recorded (format: "Month DD, YYYY")
- youtube_id: The video ID from the YouTube URL
- presenter: Name of the person presenting
- description: Brief overview of the webinar content
- about_the_author: Bio information about the presenter
-->

---
webinar:
  title: ""
  date: ""
  youtube_id: ""
  video_width_max: "720"
  presenter: ""
  description: ""
  about_the_author: ""
---

# {{ webinar.title }}

**Presenter:** {{ webinar.presenter }}  
**Date:** {{ webinar.date }}

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: {{ webinar.video_width_max }}px; margin: 0 auto;">
  <iframe
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube-nocookie.com/embed/{{ webinar.youtube_id }}?controls=1&start=0"
    title="{{ webinar.title }}"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen>
  </iframe>
</div>

## **Description:**

{{ webinar.description }}

## **About the Author:**

{{ webinar.about_the_author }}
