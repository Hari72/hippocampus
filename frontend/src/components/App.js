import React, { Component } from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import Dashboard from "../components/dashboard/Dashboard";
import store from "../store";
import "./ant-styles.css";
import "./App.css";
import Hippo from '../../assets/hippo.svg';
import { Row, Col } from 'antd';
import Icon from '@ant-design/icons';

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        {/* <div className="page-header">
          <Row style={{ width: "100%" }}>
            <Col span={2} offset={7}><Icon component={Hippo} className="hippo" /></Col>
          </Row>
        </div> */}
        <Dashboard />
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.querySelector("#app"));
