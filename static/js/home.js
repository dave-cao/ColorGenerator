const loaderFunction = (event) => {
  let loader = document.querySelector(".loader");
  let loaderDescription = document.querySelector(".loader-description");
  loader.style.display = "block";
  loaderDescription.style.display = "block";
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
