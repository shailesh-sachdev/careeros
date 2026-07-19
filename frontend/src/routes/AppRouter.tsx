import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "@/layouts/MainLayout";
import DashboardPage from "@/features/dashboard/DashboardPage";

function Placeholder({ title }: { title: string }) {
  return (
    <div className="space-y-2">
      <h1 className="text-3xl font-bold">{title}</h1>
      <p className="text-muted-foreground">
        Coming soon...
      </p>
    </div>
  );
}

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route
            path="/"
            element={<DashboardPage />}
          />

          <Route
            path="/jobs"
            element={<Placeholder title="Jobs" />}
          />

          <Route
            path="/applications"
            element={<Placeholder title="Applications" />}
          />

          <Route
            path="/resume"
            element={<Placeholder title="Resume" />}
          />

          <Route
            path="/ai"
            element={<Placeholder title="AI Tools" />}
          />

          <Route
            path="/settings"
            element={<Placeholder title="Settings" />}
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}