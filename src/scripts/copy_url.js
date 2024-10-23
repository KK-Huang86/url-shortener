import Alpine from "alpinejs";
Alpine.data("copy_url", () => ({
  init() {
    console.log("hi"); // 在模型初始化時印出 "hi"
  },
  async copyToClipboard(url) {
    try {
      await navigator.clipboard.writeText(url); // 使用 Clipboard API 複製文本
      console.log("複製成功: " + url); // 提示成功消息
    } catch (err) {
      console.log("複製失敗: " + err); // 提示失敗消息
    }
  },
}));

window.Alpine = Alpine;
