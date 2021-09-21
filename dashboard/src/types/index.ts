export type YoutubeResultType = {
    id: number;
    video_id: string;
    title: string;
    thumbnail_url: string;
    description: string;
    published_date: string;
};

export type ApiResultType = {
    count: number;
    next: string | null;
    previous: string | null;
    results: Array<YoutubeResultType>;
};
