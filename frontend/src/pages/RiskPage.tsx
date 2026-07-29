import React from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent, CardHeader, CardTitle } from '../components/common/Card';
import { ShieldAlert, Activity, CheckCircle } from 'lucide-react';
import { Button } from '../components/common/Button';

export function RiskPage() {
  return (
    <PageContainer>
      <div className="space-y-6 max-w-5xl mx-auto">
        <div className="flex justify-between items-end">
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Risk Assessment</h1>
            <p className="text-slate-500">AI-generated pharmaceutical risk profile for the active complaint.</p>
          </div>
          <Button>Regenerate Assessment</Button>
        </div>

        <div className="grid grid-cols-3 gap-6">
          <Card className="col-span-1 border-red-200 bg-red-50/30">
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center text-red-700">
                <ShieldAlert className="w-5 h-5 mr-2" /> Overall Risk
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-4xl font-bold text-red-600">HIGH</div>
            </CardContent>
          </Card>
          
          <Card className="col-span-1 border-amber-200 bg-amber-50/30">
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center text-amber-700">
                <Activity className="w-5 h-5 mr-2" /> Probability
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-4xl font-bold text-amber-600">MEDIUM</div>
            </CardContent>
          </Card>

          <Card className="col-span-1 border-red-200 bg-red-50/30">
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center text-red-700">
                <ShieldAlert className="w-5 h-5 mr-2" /> Severity
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-4xl font-bold text-red-600">HIGH</div>
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
                The complaint describes broken tablets in batch BT24051. While the probability of recurrence is medium (based on historical batch records), the severity is high due to potential dosage inconsistency leading to adverse patient effects. This warrants immediate investigation of the packaging line and transportation logs.
              </p>
            </div>
            
            <div>
              <h3 className="font-semibold text-slate-800 mb-2">Recommended Actions</h3>
              <ul className="space-y-2">
                {["Quarantine remaining stock of batch BT24051.", "Initiate CAPA for packaging line B.", "Request samples from distributor for physical inspection."].map((action, i) => (
                  <li key={i} className="flex items-start text-sm text-slate-600 bg-slate-50 p-3 rounded border">
                    <CheckCircle className="w-4 h-4 text-indigo-500 mr-3 mt-0.5" />
                    {action}
                  </li>
                ))}
              </ul>
            </div>
          </CardContent>
        </Card>
      </div>
    </PageContainer>
  );
}
