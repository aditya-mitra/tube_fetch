import { useEffect, useState } from "preact/hooks";
import { FlexGrid, FlexGridItem } from "baseui/flex-grid";

import YoutubeCard from "../components/card";
import fetchResults from "../lib/fetch-results";
import { YoutubeResultType } from "../types";

export default function Results() {
    const [ytResults, setYtResults] = useState<YoutubeResultType[]>([]);

    useEffect(() => {
        fetchResults().then((res) => setYtResults(res.results));
    }, []);

    return (
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
    );
}
