import Alpine from "alpinejs";
Alpine.data("combinedFunction", () => ({
  init() {
    console.log("hi");
  },
  async copyToClipboard(url) {
    try {
      await navigator.clipboard.writeText(url);
      console.log("複製成功: " + url);
    } catch (err) {
      console.log("複製失敗: " + err);
    }
  },

  fetchPageInfo() {
    const shortUrl = this.$refs.short_url.value;
    console.log(shortUrl);
    fetch(shortUrl)
      .then((data) => {
        this.pageInfo = this.parseHTML(data);
      })
      .then((response) => {
        if (!response.ok) throw new Error("無法取得網站資訊");
        // return response.text();
      })
      .catch((error) => {
        console.error("Error fetching page:", error);
      });
  },
  parseHTML(html) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    console.log(html);
    return doc.querySelector("title").innerText;
  },
}));

window.Alpine = Alpine;
