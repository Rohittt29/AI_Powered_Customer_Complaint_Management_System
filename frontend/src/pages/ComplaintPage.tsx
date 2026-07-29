import React, { useState } from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent, CardHeader, CardTitle } from '../components/common/Card';
import { Input } from '../components/common/Input';
import { Label } from '../components/common/Label';
import { Button } from '../components/common/Button';
import { useAppDispatch, useAppSelector } from '../redux/hooks';
import { createComplaint } from '../redux/slices/complaintSlice';
import { addToast } from '../redux/slices/uiSlice';
import { Loader2 } from 'lucide-react';

export function ComplaintForm() {
  const dispatch = useAppDispatch();
  const { status } = useAppSelector(state => state.complaint);
  
  const [formData, setFormData] = useState({
    customer_name: '', email: '', product_name: '', batch_number: '', complaint_description: ''
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await dispatch(createComplaint(formData)).unwrap();
      dispatch(addToast({ type: 'success', message: 'Complaint saved successfully.' }));
      setFormData({ customer_name: '', email: '', product_name: '', batch_number: '', complaint_description: '' });
    } catch (err: any) {
      dispatch(addToast({ type: 'error', message: err.message || 'Failed to save complaint.' }));
    }
  };

  return (
    <form className="space-y-6" onSubmit={handleSubmit}>
      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="customer_name">Customer Name</Label>
          <Input id="customer_name" value={formData.customer_name} onChange={e => setFormData({...formData, customer_name: e.target.value})} />
        </div>
        <div className="space-y-2">
          <Label htmlFor="email">Email</Label>
          <Input id="email" type="email" value={formData.email} onChange={e => setFormData({...formData, email: e.target.value})} />
        </div>
        <div className="space-y-2">
          <Label htmlFor="product_name">Product Name</Label>
          <Input id="product_name" value={formData.product_name} onChange={e => setFormData({...formData, product_name: e.target.value})} />
        </div>
        <div className="space-y-2">
          <Label htmlFor="batch_number">Batch Number</Label>
          <Input id="batch_number" value={formData.batch_number} onChange={e => setFormData({...formData, batch_number: e.target.value})} />
        </div>
      </div>

      <div className="space-y-2">
        <Label htmlFor="description">Complaint Description</Label>
        <textarea 
          id="description" 
          rows={4}
          value={formData.complaint_description}
          onChange={e => setFormData({...formData, complaint_description: e.target.value})}
          className="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
        />
      </div>

      <div className="flex justify-end space-x-4">
        <Button variant="outline" type="button" onClick={() => setFormData({ customer_name: '', email: '', product_name: '', batch_number: '', complaint_description: '' })}>Reset</Button>
        <Button variant="secondary" type="button">Ask AI to Auto-Fill</Button>
        <Button type="submit" disabled={status === 'loading'}>
          {status === 'loading' && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
          Save Complaint
        </Button>
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
