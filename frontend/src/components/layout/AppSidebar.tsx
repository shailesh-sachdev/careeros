import { NavLink } from "react-router-dom";
import { navigation } from "@/config/navigation";

export default function AppSidebar() {
  return (
    <aside className="w-64 border-r bg-background">
      <div className="border-b p-6">
        <h1 className="text-2xl font-bold">
          Career<span className="text-primary">OS</span>
        </h1>
      </div>

      <nav className="flex flex-col gap-2 p-4">
        {navigation.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-3 rounded-lg px-4 py-3 transition ${
                  isActive
                    ? "bg-primary text-primary-foreground"
                    : "hover:bg-muted"
                }`
              }
            >
              <Icon size={18} />
              {item.title}
            </NavLink>
          );
        })}
      </nav>
    </aside>
  );
}