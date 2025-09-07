import React from 'react'

export function Tabs({ children, value, onValueChange, className = '' }) {
  return <div className={className}>{children}</div>
}

export function TabsList({ children, className = '' }) {
  return <div className={className} style={{display:'flex', gap:8}}>{children}</div>
}

export function TabsTrigger({ children, value }) {
  return <button className="btn" data-value={value}>{children}</button>
}

export function TabsContent({ children, value, className = '' }) {
  return <div className={className}>{children}</div>
}
