import Alpine from "alpinejs";
Alpine.data("combinedFunction", () => ({
  pageInfo: {
    title: "",
    description: "",
  },
  pageInfoString: "",

  init() {},
  async copyToClipboard(url) {
    try {
      await navigator.clipboard.writeText(url);
    } catch (err) {}
  },

  async fetchPageInfo() {
    const shortUrl = this.$refs.short_url.value.trim();

    if (shortUrl) {
      try {
        let response = await fetch(shortUrl);

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        let data = await response.text();
        this.pageInfo = this.parseHTML(data);
        this.pageInfoString = JSON.stringify(this.pageInfo, null, 2);
      } catch (error) {
        console.error("Error fetching page:", error);
      }
    } else {
      console.error("Invalid URL");
    }
  },

  parseHTML(html) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    const title = doc.querySelector("title")
      ? doc.querySelector("title").innerText
      : "無法取得標題";
    const metaDescription = doc.querySelector('meta[name="description"]')
      ? doc.querySelector('meta[name="description"]').getAttribute("content")
      : "無法取得描述";

    return {
      網站標題: title,
      網站敘述: metaDescription,
    };
  },
}));

window.Alpine = Alpine;
