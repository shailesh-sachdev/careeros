import { Bell, Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";

export default function AppHeader() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-background px-6">
      <div className="relative w-80">
        <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
        <Input placeholder="Search..." className="pl-10" />
      </div>

      <div className="flex items-center gap-4">
        <Bell className="h-5 w-5 cursor-pointer text-muted-foreground" />

        <Avatar>
          <AvatarFallback>SS</AvatarFallback>
        </Avatar>
      </div>
    </header>
  );
}