# emotionalai.org: content converted from Squarespace

Made from the Squarespace WordPress export of 10 Nov 2026.

- content/news/: 69 news posts (Jul 2019 to Oct 2026). Each keeps its old address in `url:`, so no redirects are needed for posts.
- content/projects/: the 9 project pages, old addresses kept.
- content/pages/: 11 other pages (Team, Contact, Writing/talks, IEEE 7014.1, film, Issues, What is it?, Reading list, Companies, the older Projects page, and the old homepage text for reference).
- static/images/legacy/: empty until you run `bash tools/get-images.sh` on your own computer. It downloads the 140 images from Squarespace into place. Do this before cancelling Squarespace.
- Every converted file has `legacy: true` so the theme can treat old content differently if needed.
- YouTube and Vimeo embeds use Hugo's built-in shortcodes. One SlideShare embed (COVID-19 risk post) is left as raw HTML, so it needs `markup.goldmark.renderer.unsafe = true`, or it can be swapped for a plain link.

Left out: 2 empty drafts, about 20 template pages ending in "-mentor", template stock images, a template "Home" page, and the empty /papers-and-reports stub.

## Viewing it in your browser

1. Unzip, then open Terminal in the `site` folder.
2. Run `hugo server`. If Hugo isn't installed: `brew install hugo` on a Mac.
3. Open http://localhost:1313

Optional first: `bash tools/get-images.sh` so the images show up.
The layouts and CSS here are a temporary preview shell, not the final design.
