import React from 'react';
import { PageContainer } from '../components/layout/PageContainer';
import { Card, CardContent, CardHeader, CardTitle } from '../components/common/Card';
import { UploadCloud, File, Trash2 } from 'lucide-react';
import { Button } from '../components/common/Button';

export function UploadPage() {
  return (
    <PageContainer>
      <div className="space-y-6 max-w-4xl mx-auto">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Upload Documents</h1>
          <p className="text-slate-500">Upload PDF documents for automatic OCR and AI extraction.</p>
        </div>

        <Card>
          <CardContent className="p-12">
            <div className="border-2 border-dashed border-slate-300 rounded-xl bg-slate-50 hover:bg-slate-100 transition-colors cursor-pointer flex flex-col items-center justify-center py-16">
              <div className="h-16 w-16 bg-white rounded-full flex items-center justify-center shadow-sm border mb-4">
                <UploadCloud className="h-8 w-8 text-indigo-500" />
              </div>
              <h3 className="text-lg font-semibold text-slate-700">Click or drag file to this area to upload</h3>
              <p className="text-slate-500 mt-2 text-sm">Support for a single or bulk upload. Strictly PDF files only.</p>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Uploaded Files</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[1, 2].map((i) => (
                <div key={i} className="flex items-center p-4 border rounded-lg bg-white">
                  <File className="h-8 w-8 text-indigo-400 mr-4" />
                  <div className="flex-1">
                    <p className="text-sm font-medium">complaint_report_scan_0{i}.pdf</p>
                    <p className="text-xs text-slate-500">1.2 MB • Ready for Extraction</p>
                  </div>
                  <Button variant="ghost" size="icon" className="text-slate-400 hover:text-red-500">
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </PageContainer>
  );
}
