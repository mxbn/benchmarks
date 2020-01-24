#include "crow.h"

int main() {
    crow::SimpleApp app;

    app.loglevel(crow::LogLevel::ERROR);

    CROW_ROUTE(app, "/")([](){
        return "hello from c++ \nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
    });

    app.port(8080).multithreaded().run();
}
