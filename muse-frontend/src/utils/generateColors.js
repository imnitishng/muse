var red = 0
var green = parseInt('AB', 16)
var blue = parseInt('66', 16)

var rankColorsMap = []

for (let i = 0; i < 20; i++) {
  green -= 7
  red += 9
  blue -= 5
  var pr = red.toString(16)
  var pg = green.toString(16)
  var pb = blue.toString(16)
  pg = pg.length > 1 ? pg : `0${pg}`
  pr = pr.length > 1 ? pr : `0${pr}`
  pb = pb.length > 1 ? pb : `0${pb}`
  rankColorsMap.push(`#${pr}${pg}${pb}`)
}

exports.rankColorsMap = rankColorsMap
