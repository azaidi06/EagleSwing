from fastai.vision.all import *
from IPython.display import Video


def get_swing_df():
    all_file_paths = get_files('../../../data')

    swing_paths = [fp for fp in all_file_paths if str(fp).split('/')[-1][-3:] == 'mp4']
    full_vid_paths = [fp for fp in all_file_paths if str(fp).split('/')[-1][-3:] != 'mp4']
    swing_meta = [str(swing_paths[x]).split('.')[-2].split('/')[-1] for x in range(len(swing_paths))]


    video_origin = [('_').join(swing_meta[x].split('_')[:2]) for x in range(len(swing_paths))]
    og_vid_num = [swing_meta[x].split('_')[1] for x in range(len(swing_paths))]
    swing = [swing_meta[x].split('_')[3] for x in range(len(swing_paths))]
    score = [swing_meta[x].split('_')[-1] for x in range(len(swing_paths))]
    swing_dict = {'origin_video': video_origin,
                  'swing_index': swing,
                  'score': score,
                  'swing_path': swing_paths,
                  'og_vid_num': og_vid_num}
    swing_df = pd.DataFrame(swing_dict)
    return swing_df