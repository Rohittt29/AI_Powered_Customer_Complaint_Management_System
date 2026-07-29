import React, { useEffect } from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent, CardHeader, CardTitle } from '../components/common/Card';
import { AlertCircle, CheckCircle2, Clock, FileText, Loader2 } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../redux/hooks';
import { fetchComplaints } from '../redux/slices/complaintSlice';

const stats = [
  { title: "Total Complaints", value: "1,248", icon: FileText, trend: "+12%" },
  { title: "Open Complaints", value: "142", icon: Clock, trend: "-4%" },
  { title: "High Risk", value: "18", icon: AlertCircle, trend: "+2", color: "text-red-500" },
  { title: "Resolved (30d)", value: "384", icon: CheckCircle2, trend: "+18%", color: "text-green-500" },
];

export function Dashboard() {
  const dispatch = useAppDispatch();
  const { complaints, status } = useAppSelector(state => state.complaint);

  useEffect(() => {
    if (status === 'idle') {
      dispatch(fetchComplaints());
    }
  }, [status, dispatch]);

  return (
    <PageContainer>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Overview</h1>
          <p className="text-slate-500">Monitor pharmaceutical complaint metrics and AI risk assessments.</p>
        </div>

        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          {stats.map((stat, i) => (
            <Card key={i}>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium text-slate-600">
                  {stat.title}
                </CardTitle>
                <stat.icon className={`h-4 w-4 ${stat.color || 'text-slate-400'}`} />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{stat.value}</div>
                <p className="text-xs text-slate-500 mt-1">
                  <span className={stat.trend.startsWith('+') ? 'text-green-600' : 'text-slate-600'}>
                    {stat.trend}
                  </span> from last month
                </p>
              </CardContent>
            </Card>
          ))}
        </div>

        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
          <Card className="col-span-4">
            <CardHeader>
              <CardTitle>Recent Complaints</CardTitle>
            </CardHeader>
            <CardContent>
              {status === 'loading' ? (
                <div className="flex justify-center p-8"><Loader2 className="w-8 h-8 animate-spin text-indigo-500" /></div>
              ) : (
                <div className="space-y-4">
                  {complaints.length > 0 ? complaints.slice(0,4).map((c: any, i) => (
                    <div key={i} className="flex items-center p-4 border rounded-lg hover:bg-slate-50 transition-colors cursor-pointer">
                      <div className="w-2 h-2 rounded-full bg-amber-500 mr-4"></div>
                      <div className="flex-1 space-y-1">
                        <p className="text-sm font-medium leading-none">{c.id || `CMP-2026-${4589 + i}`}</p>
                        <p className="text-sm text-slate-500">{c.complaint_description || `Packaging defect reported in Batch BT2405${i}`}</p>
                      </div>
                    </div>
                  )) : (
                    <div className="text-sm text-slate-500 text-center py-4">No recent complaints available. (API returned empty or failed)</div>
                  )}
                </div>
              )}
            </CardContent>
          </Card>

          <Card className="col-span-3">
            <CardHeader>
              <CardTitle>AI Copilot Activity</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {[1, 2, 3].map((i) => (
                  <div key={i} className="flex items-center space-x-4">
                    <div className="h-8 w-8 rounded-full bg-indigo-100 flex items-center justify-center">
                      <FileText className="h-4 w-4 text-indigo-600" />
                    </div>
                    <div className="flex-1 space-y-1">
                      <p className="text-sm font-medium leading-none">Automated Risk Assessment</p>
                      <p className="text-xs text-slate-500">Generated for CMP-2026-{4589 + i}</p>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </PageContainer>
  );
}
