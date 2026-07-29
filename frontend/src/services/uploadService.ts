import { api } from './api';

export const uploadService = {
  uploadDocument: async (file: File, complaintId?: string) => {
    const formData = new FormData();
    formData.append('file', file);
    if (complaintId) {
      formData.append('complaint_id', complaintId);
    }
    
    const response = await api.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;
  }
};
