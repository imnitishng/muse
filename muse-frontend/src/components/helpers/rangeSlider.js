import React, { useState,useEffect } from 'react'

const RangeSlider = ({ trackProperty, sliderFn }) => {
  const [value, onChange] = useState(5)

  useEffect(() => {
    const ele = document.querySelector('.sliderVal')
    if (ele) {
      ele.style.left = `${Number(value / 4)}px`
    }
  })

  return (
    <div className="slider-parent">
      <div className="sliderVal text-xs">
        {trackProperty}
      </div>
      <input className="sliderok"
        type="range" min="0" max="10" value={value}
        onChange={
          ({ target: { value: radius } }) => {
            onChange(radius)
            sliderFn()
          }
        }
      />
    </div>
  )
}

export default RangeSlider
