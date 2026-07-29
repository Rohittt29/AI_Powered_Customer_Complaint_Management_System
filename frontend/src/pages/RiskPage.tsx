import React, { useEffect } from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent, CardHeader, CardTitle } from '../components/common/Card';
import { ShieldAlert, Activity, CheckCircle, Loader2 } from 'lucide-react';
import { Button } from '../components/common/Button';
import { useAppDispatch, useAppSelector } from '../redux/hooks';
import { generateRisk } from '../redux/slices/riskSlice';
import { addToast } from '../redux/slices/uiSlice';

export function RiskPage() {
  const dispatch = useAppDispatch();
  const { assessment, status } = useAppSelector(state => state.risk);
  
  // Use a mock complaint ID for demonstration
  const activeComplaintId = "00000000-0000-0000-0000-000000000000";

  const handleGenerate = async () => {
    try {
      await dispatch(generateRisk(activeComplaintId)).unwrap();
      dispatch(addToast({ type: 'success', message: 'Risk assessment generated successfully.' }));
    } catch (err: any) {
      dispatch(addToast({ type: 'error', message: err.message || 'Failed to generate assessment.' }));
    }
  };

  useEffect(() => {
    // Optionally fetch automatically on mount
    if (!assessment && status === 'idle') {
      handleGenerate();
    }
  }, []);

  return (
    <PageContainer>
      <div className="space-y-6 max-w-5xl mx-auto">
        <div className="flex justify-between items-end">
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Risk Assessment</h1>
            <p className="text-slate-500">AI-generated pharmaceutical risk profile for the active complaint.</p>
          </div>
          <Button onClick={handleGenerate} disabled={status === 'loading'}>
            {status === 'loading' && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            Regenerate Assessment
          </Button>
        </div>

        {status === 'loading' && !assessment ? (
           <div className="flex justify-center p-12"><Loader2 className="w-10 h-10 animate-spin text-indigo-500" /></div>
        ) : assessment ? (
          <>
            <div className="grid grid-cols-3 gap-6">
              <Card className="col-span-1 border-red-200 bg-red-50/30">
                <CardHeader className="pb-2">
                  <CardTitle className="flex items-center text-red-700">
                    <ShieldAlert className="w-5 h-5 mr-2" /> Overall Risk
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-4xl font-bold text-red-600">{assessment.overall_risk?.toUpperCase() || 'HIGH'}</div>
                </CardContent>
              </Card>
              
              <Card className="col-span-1 border-amber-200 bg-amber-50/30">
                <CardHeader className="pb-2">
                  <CardTitle className="flex items-center text-amber-700">
                    <Activity className="w-5 h-5 mr-2" /> Probability
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-4xl font-bold text-amber-600">{assessment.probability?.toUpperCase() || 'MEDIUM'}</div>
                </CardContent>
              </Card>

              <Card className="col-span-1 border-red-200 bg-red-50/30">
                <CardHeader className="pb-2">
                  <CardTitle className="flex items-center text-red-700">
                    <ShieldAlert className="w-5 h-5 mr-2" /> Severity
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-4xl font-bold text-red-600">{assessment.severity?.toUpperCase() || 'HIGH'}</div>
                </CardContent>
              </Card>
            </div>

            <Card>
              <CardHeader>
                <CardTitle>AI Reasoning & Recommendations</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div>
                  <h3 className="font-semibold text-slate-800 mb-2">Reasoning</h3>
                  <p className="text-slate-600 text-sm leading-relaxed bg-slate-50 p-4 rounded-lg border">
                    {assessment.ai_reasoning || "Pending AI Analysis"}
                  </p>
                </div>
                
                <div>
                  <h3 className="font-semibold text-slate-800 mb-2">Recommended Actions</h3>
                  <ul className="space-y-2">
                    {(assessment.recommended_actions || ["Pending Analysis"]).map((action: string, i: number) => (
                      <li key={i} className="flex items-start text-sm text-slate-600 bg-slate-50 p-3 rounded border">
                        <CheckCircle className="w-4 h-4 text-indigo-500 mr-3 mt-0.5" />
                        {action}
                      </li>
                    ))}
                  </ul>
                </div>
              </CardContent>
            </Card>
          </>
        ) : (
          <div className="text-center text-slate-500 p-12">Failed to load risk assessment data.</div>
        )}
      </div>
    </PageContainer>
  );
}
