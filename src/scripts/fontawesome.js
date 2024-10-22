import Alpine from "alpinejs";
import { library, dom } from "@fortawesome/fontawesome-svg-core";
import { faCopy } from "@fortawesome/free-regular-svg-icons";

library.add(faCopy);
dom.i2svg();

Alpine.data("copy_icon", () => ({
  init() {
    dom.i2svg();
  },
}));
