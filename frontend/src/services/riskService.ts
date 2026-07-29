import { api } from './api';

export const riskService = {
  generateRiskAssessment: async (complaintId: string) => {
    const response = await api.post('/risk', { complaint_id: complaintId });
    return response.data;
  }
};
