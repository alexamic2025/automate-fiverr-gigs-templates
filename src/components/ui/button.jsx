import React from 'react'

export function Button({ children, className = '', size, variant, ...props }) {
  const cls = `btn ${variant === 'outline' ? 'btn-outline' : ''} ${className}`
  return (
    <button className={cls} {...props}>{children}</button>
  )
}

export default Button
