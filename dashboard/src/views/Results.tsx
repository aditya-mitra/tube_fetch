import { useEffect, useState } from "preact/hooks";
import { FlexGrid, FlexGridItem } from "baseui/flex-grid";

import YoutubeCard from "../components/card";
import fetchResults from "../lib/fetch-results";
import { YoutubeResultType } from "../types";
import PaginationBar from "../components/pagination";
import { Block } from "baseui/block";

export default function Results() {
    const [ytResults, setYtResults] = useState<YoutubeResultType[]>([]);
    const [totalCount, setTotalCount] = useState(0);
    const [currentPage, setCurrentPage] = useState(1);

    useEffect(() => {
        const offset = (currentPage - 1) * 10;
        fetchResults(offset).then((res) => {
            setYtResults(res.results);
            setTotalCount(res.count);
        });
    }, [currentPage]);

    return (
        <>
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
