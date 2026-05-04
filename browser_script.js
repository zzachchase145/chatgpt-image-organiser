// Get ChatGPT uploaded images only
const images = [...document.querySelectorAll('img')]
  .map(img => img.src)
  .filter(src => src.includes('/backend-api/estuary/content'));

console.log(`Found ${images.length} ChatGPT uploaded images`);

// Download them
images.forEach((url, index) => {
  const a = document.createElement('a');
  a.href = url;
  a.download = `chatgpt_image_${index + 1}.png`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
});