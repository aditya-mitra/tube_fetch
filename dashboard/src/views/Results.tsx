import { useEffect, useState } from "preact/hooks";
import { FlexGrid, FlexGridItem } from "baseui/flex-grid";

import YoutubeCard from "../components/card";
import fetchResults from "../lib/fetch-results";
import { YoutubeResultType } from "../types";
import PaginationBar from "../components/pagination";
import { Block } from "baseui/block";
import SearchBar from "../components/search-bar";

export default function Results() {
    const [ytResults, setYtResults] = useState<YoutubeResultType[]>([]);
    const [totalCount, setTotalCount] = useState(0);
    const [currentPage, setCurrentPage] = useState(1);
    const [searchInput, setSearchInput] = useState("");

    useEffect(() => {
        const offset = (currentPage - 1) * 10;
        fetchResults(offset, searchInput).then((res) => {
            setYtResults(res.results);
            setTotalCount(res.count);
        });
    }, [currentPage, searchInput]);

    return (
        <>
            <Block>
                <SearchBar value={searchInput} setValue={setSearchInput} />
            </Block>
            <Block margin="2rem 0">
                <PaginationBar
                    totalCount={totalCount}
                    currentPage={currentPage}
                    setCurrentPage={setCurrentPage}
                />
            </Block>
            <Block>
                <FlexGrid
                    flexGridColumnCount={3}
                    flexGridColumnGap="scale800"
                    flexGridRowGap="scale800"
                >
                    {ytResults.map((result) => (
                        <FlexGridItem>
                            <YoutubeCard
                                key={result.id}
                                thumbnailUrl={result.thumbnail_url}
                                description={result.description}
                                title={result.title}
                                videoId={result.video_id}
                                publishedDate={result.published_date}
                            />
                        </FlexGridItem>
                    ))}
                </FlexGrid>
            </Block>
        </>
    );
}
