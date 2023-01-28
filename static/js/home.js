const loaderFunction = (event) => {
  let loader = document.querySelector(".loader");
  let loaderDescription = document.querySelector(".loader-description");
  loader.style.display = "block";
  loaderDescription.style.display = "block";

  // After 10 seconds update message
  const second = 1000;
  setTimeout(() => {
    loaderDescription.innerHTML =
      "Since this is hosted for free, it may take ~10-20 seconds to generate your pallette 😅.";
  }, second * 5);

  setTimeout(() => {
    loaderDescription.innerHTML = "Nice weather today isn't it? Hehe...😫";
  }, second * 20);

  setTimeout(() => {
    loaderDescription.innerHTML =
      "Hmmmm, it shouldn't take this long to generate...try refreshing the page. Or the server is just being doo doo right now.";
  }, second * 35);
};

const copyColor = (event) => {
  // Get's current clicked element
  let colorDiv = event.target;
  let hexCode = null;
  let colorToolTip = null;

  // catches if user clicks on inner text element rather than outter div element
  try {
    // Outer div element
    hexCode = colorDiv.querySelector(".my-hex").innerHTML;
    colorToolTip = colorDiv.querySelector(".tooltiptext");
  } catch (err) {
    // inner text element
    hexCode = colorDiv.innerHTML;
    colorToolTip = colorDiv.parentElement.querySelector(".tooltiptext");
  }

  // copy to cliboard
  navigator.clipboard.writeText(hexCode);

  // reset tooltips for all other colours
  let alltooltips = document.querySelectorAll(".tooltiptext");
  alltooltips.forEach((tooltip) => {
    tooltip.innerHTML = "Click to copy color!";
  });

  // display copied!
  colorToolTip.innerHTML = `Copied: ${hexCode}`;

  // change background color
  const body = document.querySelector("h1");
  body.style.color = hexCode;
};

const loadFile = (event) => {
  file = event.target.files[0];
  let reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = function () {
    localStorage.setItem("imageData", reader.result);
  };
};

window.onload = function () {
  let image_store = localStorage.getItem("imageData");
  if (image_store !== null) {
    document.getElementById("output").src = image_store;
  }
};
