import React from 'react';
import { Sidebar } from './Sidebar';
import { Header } from './Header';

interface PageContainerProps {
  children: React.ReactNode;
}

export function PageContainer({ children }: PageContainerProps) {
  return (
    <div className="min-h-screen bg-slate-50/50 flex">
      <Sidebar />
      <div className="flex-1 ml-64 flex flex-col">
        <Header />
        <main className="flex-1 p-8">
          {children}
        </main>
      </div>
    </div>
  );
}
