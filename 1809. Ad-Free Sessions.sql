select session_id from Playback p 
left join Ads a on
    p.customer_id = a.customer_id and
    p.start_time <= a.timestamp and
    a.timestamp <= p.end_time
where a.ad_id is NULL
