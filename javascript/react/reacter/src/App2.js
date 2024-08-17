import React, {Component} from "react";
import ReactDOM from "react-dom/client";
import {App3} from "./App3";

export class App2 extends React.Component{
    render() {
        return (
            <div>
                Hello App2.js
                <App3 />
            </div>
        )
    }
}

export default App2