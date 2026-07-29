import React from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent, CardHeader, CardTitle } from '../components/common/Card';
import { Input } from '../components/common/Input';
import { Label } from '../components/common/Label';
import { Button } from '../components/common/Button';

export function ComplaintForm() {
  return (
    <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="customer_name">Customer Name</Label>
          <Input id="customer_name" placeholder="John Doe" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="email">Email</Label>
          <Input id="email" type="email" placeholder="john@example.com" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="product_name">Product Name</Label>
          <Input id="product_name" placeholder="Aspirin 500mg" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="batch_number">Batch Number</Label>
          <Input id="batch_number" placeholder="BT24051" />
        </div>
      </div>

      <div className="space-y-2">
        <Label htmlFor="description">Complaint Description</Label>
        <textarea 
          id="description" 
          rows={4}
          className="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
          placeholder="Describe the issue in detail..."
        />
      </div>

      <div className="flex justify-end space-x-4">
        <Button variant="outline">Reset</Button>
        <Button variant="secondary">Ask AI to Auto-Fill</Button>
        <Button type="submit">Save Complaint</Button>
      </div>
    </form>
  );
}

export function ComplaintPage() {
  return (
    <PageContainer>
      <div className="space-y-6 max-w-4xl mx-auto">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Log Complaint</h1>
          <p className="text-slate-500">Manually enter a new complaint or use the AI Copilot to assist.</p>
        </div>
        
        <Card>
          <CardHeader>
            <CardTitle>Complaint Details</CardTitle>
          </CardHeader>
          <CardContent>
            <ComplaintForm />
          </CardContent>
        </Card>
      </div>
    </PageContainer>
  );
}
