import React from 'react'

export function Card({ children, className = '' }) {
  return <div className={`card ${className}`}>{children}</div>
}

export function CardHeader({ children, className = '' }) {
  return <div className={`p-2 ${className}`}>{children}</div>
}

export function CardContent({ children, className = '' }) {
  return <div className={`p-2 ${className}`}>{children}</div>
}

export function CardTitle({ children, className = '' }) {
  return <div className={`font-bold ${className}`}>{children}</div>
}

export function CardDescription({ children, className = '' }) {
  return <div className={`text-sm text-muted-foreground ${className}`}>{children}</div>
}
