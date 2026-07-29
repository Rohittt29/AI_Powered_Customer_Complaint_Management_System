import { api } from './api';

export interface ComplaintData {
  id?: string;
  customer_name?: string;
  email?: string;
  product_name?: string;
  batch_number?: string;
  complaint_description?: string;
  status?: string;
}

export const complaintService = {
  getComplaints: async () => {
    const response = await api.get('/complaints');
    return response.data;
  },
  
  getComplaintById: async (id: string) => {
    const response = await api.get(`/complaints/${id}`);
    return response.data;
  },
  
  createComplaint: async (data: ComplaintData) => {
    const response = await api.post('/complaints', data);
    return response.data;
  },
  
  updateComplaint: async (id: string, data: ComplaintData) => {
    const response = await api.put(`/complaints/${id}`, data);
    return response.data;
  },
};
