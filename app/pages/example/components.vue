<template>
    <view class="wrap">
        <page-nav :desc="desc" title="TTS 语音合成"></page-nav>

        <view class="container">
            <!-- 文本输入框 -->
            <input class="input-box" v-model="text" placeholder="请输入文本" />

            <!-- 按钮触发 TTS -->
            <button class="btn" @click="fetchTTS">播放语音</button>
        </view>

    </view>
</template>

<script>
import list from "./components.config.js";

// 定义常量
const TTS_SERVER_URL = "http://127.0.0.1:8000/tts";
const REQUEST_HEADER = { "Content-Type": "application/json" };

export default {
    data() {
        return {
            list: list,
            text: "你好，欢迎使用语音合成！", // 默认文本
            audioSrc: "" // 存储音频 URL
        };
    },
    computed: {
        desc() {
            return this.$t('components.desc');
        }
    },
    onShow() {
        uni.setNavigationBarTitle({
            title: this.$t('nav.components')
        });
    },
    methods: {
        async fetchTTS() {
            // 检查输入文本是否为空
            if (!this.text.trim()) {
                uni.showToast({ title: "请输入文本", icon: "none" });
                return;
            }

            // 显示加载提示
            uni.showLoading({ title: "正在生成语音..." });

            try {
                // 发送 POST 请求到服务器进行语音合成
                const res = await uni.request({
                    url: TTS_SERVER_URL,
                    method: "POST",
                    header: REQUEST_HEADER,
                    data: { text: this.text }
                });

                // 从返回数组中获取响应数据
                const { data, statusCode } = res[1];

                // 隐藏加载提示
                uni.hideLoading();

                // 检查响应状态码和数据是否正常
                if (statusCode === 200 && data) {
                    this.playAudio(data);
                } else {
                    uni.showToast({ title: "语音生成失败或数据不完整", icon: "none" });
                }
            } catch (err) {
                // 隐藏加载提示
                uni.hideLoading();
                // 显示详细错误信息
                uni.showToast({ title: `请求失败: ${err.errMsg || err.message}`, icon: "none" });
                console.error("TTS 请求错误:", err);
            }
        },
        playAudio(base64Audio) {
            // 创建音频上下文
            const audioContext = uni.createInnerAudioContext();
            // 设置音频源
            audioContext.src = `data:audio/wav;base64,${base64Audio}`;

            // 监听音频播放事件
            audioContext.onPlay(() => {
                console.log('Playing audio...');
            });

            // 监听音频错误事件
            audioContext.onError((err) => {
                console.error('Audio error:', err);
                if (err && err.errMsg) {
                    console.error('Detailed error:', err.errMsg);
                }
                // 销毁音频上下文
                audioContext.destroy();
            });

            // 监听音频播放完成事件
            audioContext.onEnded(() => {
                // 销毁音频上下文
                audioContext.destroy();
            });

            // 播放音频
            audioContext.play();
        }
    }
};
</script>

<style lang="scss" scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.input-box {
    width: 80%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 15px;
}

.btn {
    background-color: #007aff;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
}
</style>