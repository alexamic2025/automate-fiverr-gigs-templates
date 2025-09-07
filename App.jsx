import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  LineChart,
  Line,
  PieChart,
  Pie,
  Cell
} from 'recharts'
import { 
  DollarSign, 
  Users, 
  FileText, 
  TrendingUp, 
  Clock, 
  CheckCircle, 
  AlertCircle,
  Settings,
  MessageSquare,
  BarChart3,
  Zap,
  Target,
  Calendar,
  Mail,
  Download,
  Plus,
  Edit,
  Eye
} from 'lucide-react'
import './App.css'

// Mock data for demonstration
const dashboardData = {
  stats: {
    totalRevenue: 12450,
    activeProjects: 8,
    completedProjects: 24,
    totalClients: 15,
    responseTime: '1.2 hours',
    satisfactionRate: 98
  },
  revenueData: [
    { month: 'Jan', revenue: 2400 },
    { month: 'Feb', revenue: 3200 },
    { month: 'Mar', revenue: 2800 },
    { month: 'Apr', revenue: 4100 },
    { month: 'May', revenue: 3600 },
    { month: 'Jun', revenue: 4200 }
  ],
  projectTypes: [
    { name: 'Market Research', value: 45, color: '#8884d8' },
    { name: 'Data Analysis', value: 30, color: '#82ca9d' },
    { name: 'BI Dashboards', value: 15, color: '#ffc658' },
    { name: 'Consulting', value: 10, color: '#ff7300' }
  ],
  recentProjects: [
    { id: 1, title: 'E-commerce Market Analysis', client: 'TechStart Inc.', status: 'In Progress', dueDate: '2025-08-10', progress: 75 },
    { id: 2, title: 'Customer Behavior Dashboard', client: 'RetailCorp', status: 'Completed', dueDate: '2025-08-05', progress: 100 },
    { id: 3, title: 'Financial Data Analysis', client: 'FinanceFlow', status: 'Active', dueDate: '2025-08-15', progress: 25 },
    { id: 4, title: 'Strategic Consulting', client: 'GrowthCo', status: 'Pending', dueDate: '2025-08-20', progress: 0 }
  ],
  templates: [
    { id: 1, name: 'Market Research Gig', category: 'Gig Description', usage: 15 },
    { id: 2, name: 'Initial Inquiry Response', category: 'Communication', usage: 42 },
    { id: 3, name: 'Project Kickoff', category: 'Communication', usage: 28 },
    { id: 4, name: 'Delivery Notification', category: 'Communication', usage: 24 }
  ]
}

function StatCard({ title, value, icon: Icon, trend, trendValue }) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        <Icon className="h-4 w-4 text-muted-foreground" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
        {trend && (
          <p className="text-xs text-muted-foreground">
            <span className={trend === 'up' ? 'text-green-600' : 'text-red-600'}>
              {trend === 'up' ? '+' : '-'}{trendValue}%
            </span>
            {' '}from last month
          </p>
        )}
      </CardContent>
    </Card>
  )
}

function ProjectCard({ project }) {
  const getStatusColor = (status) => {
    switch (status) {
      case 'Completed': return 'bg-green-100 text-green-800'
      case 'In Progress': return 'bg-blue-100 text-blue-800'
      case 'Active': return 'bg-yellow-100 text-yellow-800'
      case 'Pending': return 'bg-gray-100 text-gray-800'
      default: return 'bg-gray-100 text-gray-800'
    }
  }

  return (
    <Card className="mb-4">
      <CardHeader>
        <div className="flex justify-between items-start">
          <div>
            <CardTitle className="text-lg">{project.title}</CardTitle>
            <CardDescription>Client: {project.client}</CardDescription>
          </div>
          <Badge className={getStatusColor(project.status)}>
            {project.status}
          </Badge>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>Progress</span>
            <span>{project.progress}%</span>
          </div>
          <Progress value={project.progress} className="w-full" />
          <div className="flex justify-between items-center text-sm text-muted-foreground">
            <span>Due: {project.dueDate}</span>
            <div className="flex space-x-2">
              <Button size="sm" variant="outline">
                <Eye className="h-3 w-3 mr-1" />
                View
              </Button>
              <Button size="sm" variant="outline">
                <Edit className="h-3 w-3 mr-1" />
                Edit
              </Button>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

function TemplateCard({ template }) {
  return (
    <Card className="mb-4">
      <CardHeader>
        <div className="flex justify-between items-start">
          <div>
            <CardTitle className="text-lg">{template.name}</CardTitle>
            <CardDescription>{template.category}</CardDescription>
          </div>
          <Badge variant="secondary">
            Used {template.usage} times
          </Badge>
        </div>
      </CardHeader>
      <CardContent>
        <div className="flex space-x-2">
          <Button size="sm" variant="outline">
            <Eye className="h-3 w-3 mr-1" />
            Preview
          </Button>
          <Button size="sm" variant="outline">
            <Edit className="h-3 w-3 mr-1" />
            Edit
          </Button>
          <Button size="sm" variant="outline">
            <Download className="h-3 w-3 mr-1" />
            Export
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}

function App() {
  const [activeTab, setActiveTab] = useState('dashboard')

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b bg-card">
        <div className="container mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <Zap className="h-8 w-8 text-primary" />
                <h1 className="text-2xl font-bold">Fiverr Automation Dashboard</h1>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Button variant="outline" size="sm">
                <Settings className="h-4 w-4 mr-2" />
                Settings
              </Button>
              <Button size="sm">
                <Plus className="h-4 w-4 mr-2" />
                New Project
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-6">
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-5">
            <TabsTrigger value="dashboard">
              <BarChart3 className="h-4 w-4 mr-2" />
              Dashboard
            </TabsTrigger>
            <TabsTrigger value="projects">
              <FileText className="h-4 w-4 mr-2" />
              Projects
            </TabsTrigger>
            <TabsTrigger value="templates">
              <MessageSquare className="h-4 w-4 mr-2" />
              Templates
            </TabsTrigger>
            <TabsTrigger value="automation">
              <Zap className="h-4 w-4 mr-2" />
              Automation
            </TabsTrigger>
            <TabsTrigger value="analytics">
              <TrendingUp className="h-4 w-4 mr-2" />
              Analytics
            </TabsTrigger>
          </TabsList>

          {/* Dashboard Tab */}
          <TabsContent value="dashboard" className="space-y-6">
            {/* Stats Grid */}
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
              <StatCard
                title="Total Revenue"
                value={`$${dashboardData.stats.totalRevenue.toLocaleString()}`}
                icon={DollarSign}
                trend="up"
                trendValue="12.5"
              />
              <StatCard
                title="Active Projects"
                value={dashboardData.stats.activeProjects}
                icon={FileText}
                trend="up"
                trendValue="8.2"
              />
              <StatCard
                title="Total Clients"
                value={dashboardData.stats.totalClients}
                icon={Users}
                trend="up"
                trendValue="15.3"
              />
              <StatCard
                title="Satisfaction Rate"
                value={`${dashboardData.stats.satisfactionRate}%`}
                icon={CheckCircle}
                trend="up"
                trendValue="2.1"
              />
            </div>

            {/* Charts Row */}
            <div className="grid gap-4 md:grid-cols-2">
              {/* Revenue Chart */}
              <Card>
                <CardHeader>
                  <CardTitle>Revenue Trend</CardTitle>
                  <CardDescription>Monthly revenue over the last 6 months</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={dashboardData.revenueData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="month" />
                      <YAxis />
                      <Tooltip />
                      <Line type="monotone" dataKey="revenue" stroke="#8884d8" strokeWidth={2} />
                    </LineChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>

              {/* Project Types Chart */}
              <Card>
                <CardHeader>
                  <CardTitle>Project Distribution</CardTitle>
                  <CardDescription>Breakdown by service type</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <PieChart>
                      <Pie
                        data={dashboardData.projectTypes}
                        cx="50%"
                        cy="50%"
                        labelLine={false}
                        label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                        outerRadius={80}
                        fill="#8884d8"
                        dataKey="value"
                      >
                        {dashboardData.projectTypes.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={entry.color} />
                        ))}
                      </Pie>
                      <Tooltip />
                    </PieChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>

            {/* Recent Projects */}
            <Card>
              <CardHeader>
                <CardTitle>Recent Projects</CardTitle>
                <CardDescription>Your latest project activities</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4 md:grid-cols-2">
                  {dashboardData.recentProjects.map((project) => (
                    <ProjectCard key={project.id} project={project} />
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Projects Tab */}
          <TabsContent value="projects" className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-3xl font-bold">Project Management</h2>
              <Button>
                <Plus className="h-4 w-4 mr-2" />
                Create New Project
              </Button>
            </div>
            
            <div className="grid gap-4">
              {dashboardData.recentProjects.map((project) => (
                <ProjectCard key={project.id} project={project} />
              ))}
            </div>
          </TabsContent>

          {/* Templates Tab */}
          <TabsContent value="templates" className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-3xl font-bold">Template Management</h2>
              <Button>
                <Plus className="h-4 w-4 mr-2" />
                Create New Template
              </Button>
            </div>
            
            <div className="grid gap-4 md:grid-cols-2">
              {dashboardData.templates.map((template) => (
                <TemplateCard key={template.id} template={template} />
              ))}
            </div>
          </TabsContent>

          {/* Automation Tab */}
          <TabsContent value="automation" className="space-y-6">
            <h2 className="text-3xl font-bold">Automation Center</h2>
            
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center">
                    <Mail className="h-5 w-5 mr-2" />
                    Email Automation
                  </CardTitle>
                  <CardDescription>Automated client communications</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    <div className="flex justify-between">
                      <span className="text-sm">Active Rules</span>
                      <Badge>8</Badge>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-sm">Messages Sent</span>
                      <span className="text-sm font-medium">142</span>
                    </div>
                    <Button className="w-full" variant="outline">
                      Manage Rules
                    </Button>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center">
                    <FileText className="h-5 w-5 mr-2" />
                    Report Generation
                  </CardTitle>
                  <CardDescription>Automated report creation</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    <div className="flex justify-between">
                      <span className="text-sm">Templates</span>
                      <Badge>4</Badge>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-sm">Generated</span>
                      <span className="text-sm font-medium">28</span>
                    </div>
                    <Button className="w-full" variant="outline">
                      Generate Report
                    </Button>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center">
                    <Calendar className="h-5 w-5 mr-2" />
                    Task Scheduling
                  </CardTitle>
                  <CardDescription>Automated task management</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    <div className="flex justify-between">
                      <span className="text-sm">Scheduled Tasks</span>
                      <Badge>12</Badge>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-sm">Completed</span>
                      <span className="text-sm font-medium">89%</span>
                    </div>
                    <Button className="w-full" variant="outline">
                      View Schedule
                    </Button>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Analytics Tab */}
          <TabsContent value="analytics" className="space-y-6">
            <h2 className="text-3xl font-bold">Business Analytics</h2>
            
            <div className="grid gap-4 md:grid-cols-2">
              <Card>
                <CardHeader>
                  <CardTitle>Performance Metrics</CardTitle>
                  <CardDescription>Key business indicators</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span>Average Response Time</span>
                      <Badge variant="secondary">{dashboardData.stats.responseTime}</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span>Project Completion Rate</span>
                      <Badge variant="secondary">94%</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span>Client Retention Rate</span>
                      <Badge variant="secondary">87%</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span>Average Project Value</span>
                      <Badge variant="secondary">$518</Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>Growth Trends</CardTitle>
                  <CardDescription>Business growth indicators</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={200}>
                    <BarChart data={dashboardData.revenueData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="month" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="revenue" fill="#8884d8" />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>
      </main>
    </div>
  )
}

export default App

