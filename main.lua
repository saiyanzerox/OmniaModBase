-- Omnia Example Lua Mod

local enableLua = false

function Settings()
    -- This Function is Just For Mod Settings...
    UI.Label("Example Mod - Lua")
    enableLua = UI.Checkbox("Enable Lua", enableLua, function(v)
        enableLua = (v > 0.5) -- Change the value to boolean (1 or 0)
        Logger.Success("ExampleMod", "Lua Logic " .. (enableLua and "Active" or "Inactive"))
    end)
end

function Boot()
    -- This Function Will be Called Only Once...
end

function Loop()
    -- This Function Will be Called Every Game Ticks...
    if enableLua then Logger.Success("ExampleMod", "Lua Enabled!") end
end

function Kill()
    -- This Function Will be Called on Mod Disable or Game Shutdown...
end