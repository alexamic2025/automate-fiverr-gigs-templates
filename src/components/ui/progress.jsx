import React from 'react'
import PropTypes from 'prop-types'

/**
 * Progress component that displays a progress bar
 * @param {Object} props - Component props
 * @param {number} [props.value] - Current progress value
 * @param {number} [props.min=0] - Minimum value
 * @param {number} [props.max=100] - Maximum value
 * @param {string} [props.label] - Accessible label for the progress bar
 * @param {boolean} [props.isIndeterminate=false] - Whether the progress is indeterminate
 * @param {string} [props.className] - Additional CSS classes
 * @returns {React.ReactElement} Progress bar component
 */
export function Progress({ 
  value,
  min = 0,
  max = 100,
  label,
  isIndeterminate = false,
  className = ''
}) {
  // Handle invalid min/max
  if (min >= max) {
    console.error('Progress: min must be less than max')
    return null
  }

  // Calculate percentage
  const range = max - min
  const normalizedValue = value === undefined ? min : Math.max(min, Math.min(max, value))
  const percentage = range ? ((normalizedValue - min) / range) * 100 : 0

  // Build className
  const rootClassName = [
    'progress',
    isIndeterminate && 'progress--indeterminate',
    className
  ].filter(Boolean).join(' ')

  return (
    <div 
      className={rootClassName}
      role="progressbar"
      aria-label={label}
      aria-valuemin={min}
      aria-valuemax={max}
      aria-valuenow={isIndeterminate ? undefined : normalizedValue}
      aria-valuetext={isIndeterminate ? 'Loading...' : `${Math.round(percentage)}%`}
    >
      <div 
        className="progress-indicator"
        style={isIndeterminate ? undefined : { inlineSize: `${percentage}%` }}
      />
    </div>
  )
}

Progress.propTypes = {
  value: PropTypes.number,
  min: PropTypes.number,
  max: PropTypes.number,
  label: PropTypes.string.isRequired,
  isIndeterminate: PropTypes.bool,
  className: PropTypes.string
}

export default Progress
