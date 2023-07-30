$(document).ready(function () {
  $("a.external:not([href^='https://thy'],[href^='https://thump'])").attr("target", "_blank").addClass("external_link")
})
