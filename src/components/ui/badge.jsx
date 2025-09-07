import React from 'react'

export function Badge({ children, className = '' , variant}) {
  return <span className={`badge ${className}`}>{children}</span>
}

export default Badge
