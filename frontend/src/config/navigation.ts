import {
  LayoutDashboard,
  Briefcase,
  FileText,
  FileEdit,
  MessageSquareText,
  Brain,
  Settings,
} from "lucide-react";

export const navigation = [
  {
    title: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    title: "Jobs",
    path: "/jobs",
    icon: Briefcase,
  },
  {
    title: "Applications",
    path: "/applications",
    icon: FileText,
  },
  {
    title: "Resume",
    path: "/resume",
    icon: FileEdit,
  },
  {
    title: "AI Tools",
    path: "/ai",
    icon: Brain,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: Settings,
  },
];