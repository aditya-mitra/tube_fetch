import { StateUpdater, useState } from "preact/hooks";

import { ButtonGroup, SHAPE, MODE } from "baseui/button-group";
import { Button } from "baseui/button";

enum TitleOrder {
    asc = "title",
    desc = "-title",
}

enum PublishedDateOrder {
    asc = "published_date",
    desc = "-published_date",
}

interface ISortBy {
    setOrder: StateUpdater<string>;
}

export default function SortBy({ setOrder }: ISortBy) {
    const [selected, setSelected] = useState(0);

    return (
        <>
            <ButtonGroup
                shape={SHAPE.pill}
                mode={MODE.radio}
                selected={selected}
                onClick={(_e, idx) => {
                    setSelected(idx);
                }}
            >
                <Button onClick={() => setOrder(PublishedDateOrder.desc)}>
                    Published Date (Descending)
                </Button>
                <Button onClick={() => setOrder(PublishedDateOrder.asc)}>
                    Published Date (Ascending)
                </Button>
                <Button onClick={() => setOrder(TitleOrder.desc)}>
                    Title (Descending)
                </Button>
                <Button onClick={() => setOrder(TitleOrder.asc)}>
                    Title (Ascending)
                </Button>
            </ButtonGroup>
        </>
    );
}
