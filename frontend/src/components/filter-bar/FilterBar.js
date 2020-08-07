import React, { useState } from "react";
import { Input, Checkbox, Row, Col } from "antd";
import "./FilterBar.css";
import { useDispatch } from 'react-redux';
import { FILTER_REMINDERS, SEARCH_REMINDERS } from '../../store/types';

const FilterTab = (props) => {
    const dispatch = useDispatch();

    const options = ["All", "Active", "Done"];
    const [show, setShow] = useState(["Active"]);
    let filter = "Active";

    const handleShowChange = (e) => {
        const isChecked = e.length > show.length;
        let current = "";
        if (isChecked) {
            current = e.filter(selected => !show.includes(selected))[0];
        } else {
            current = show.filter(selected => !e.includes(selected))[0];
        }
        if (current === "All" && isChecked) {
            setShow([...options]);
            filter = "All";
        } else if (current === "All" && !isChecked) {
            setShow([]);
            filter = "";
        } else if (e.length === 2) {
            if (isChecked) {
                setShow([...e, "All"]);
                filter = "All";
            } else {
                setShow([...e.filter(selected => selected !== "All")]);
                filter = e.filter(selected => selected !== "All")[0]
            }
        } else {
            setShow(e);
            filter = e[0];
        }

        handleFilterChange(filter);

    };

    const handleFilterChange = filter => {
        dispatch({
            type: FILTER_REMINDERS,
            filter
        });
    };

    const handleSearch = (e) => {
        const searchText = e.target.value;
        dispatch({
            type: SEARCH_REMINDERS,
            searchText
        });
    };

    return (
        <Row className="filter">
            <Col span={8}>
                <Checkbox.Group options={options} value={show} onChange={e => handleShowChange(e)} />
            </Col>
            <Col span={8}>
                <Input size="large" placeholder="Search..." onChange={e => handleSearch(e)} />
            </Col>
        </Row>
    );
};

export default FilterTab;