import { Pagination, SIZE } from "baseui/pagination";
import { StateUpdater } from "preact/hooks";

interface IPaginationBar {
    totalCount: number;
    currentPage: number;
    setCurrentPage: StateUpdater<number>;
}

export default function PaginationBar({
    totalCount,
    currentPage,
    setCurrentPage,
}: IPaginationBar) {
    return (
        <Pagination
            numPages={Math.ceil(totalCount / 10)}
            size={SIZE.large}
            currentPage={currentPage}
            onPageChange={({ nextPage }) => {
                setCurrentPage(nextPage);
            }}
        />
    );
}
